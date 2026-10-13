"""Build agistrategy.app into ./public. No dependencies beyond Python 3.

Run locally with:  python3 build.py
Cloudflare Pages runs the same command on every push.
"""
import glob, html, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'public')
FIELDS = ['Definition', 'Example or analogy', 'Relevance to strategy',
          'Where people disagree', 'Related terms', 'Go deeper']
problems = []


def inline(t):
    t = t.replace('\\[', '[').replace('\\]', ']').replace('\\_', '_')
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(<?([^)>]+(?:\([^)]*\))?[^)>]*)>?\)',
               lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![*\w])\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    return t


def block_html(lines):
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        if not l.strip():
            i += 1; continue
        if l.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append('<li>' + inline(lines[i][2:]) + '</li>'); i += 1
            out.append('<ul>' + ''.join(items) + '</ul>'); continue
        if l.startswith('> '):
            out.append('<blockquote>' + inline(l[2:]) + '</blockquote>'); i += 1; continue
        out.append('<p>' + inline(l) + '</p>'); i += 1
    return ''.join(out)


def read_entry(path):
    eid = os.path.splitext(os.path.basename(path))[0]
    raw = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.S)
    if not m:
        problems.append(f'{eid}.md: missing the --- header block at the top'); return None
    meta = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            k, v = line.split(':', 1); meta[k.strip()] = v.strip()
    for k in ('title', 'unit'):
        if not meta.get(k):
            problems.append(f'{eid}.md: header needs a "{k}:" line')
    f, cur = {}, None
    for line in m.group(2).split('\n'):
        mm = re.match(r'^\*\*([^*]+):\*\*\s?(.*)$', line)
        if mm and mm.group(1) in FIELDS:
            cur = mm.group(1); f[cur] = [mm.group(2)]; continue
        if cur:
            f[cur].append(line)
    if 'Definition' not in f:
        problems.append(f'{eid}.md: no "**Definition:**" section found')
        f['Definition'] = ['']
    first = f['Definition'][0].strip()
    lede = re.split(r'(?<=[.!?])\s+(?=[A-Z"])', first)[0]
    aliases = [a.strip() for a in meta.get('aliases', '').split(';') if a.strip()]
    plain = ' '.join(sum(f.values(), []))
    text = re.sub(r'\s+', ' ', re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', plain)).lower()
    return {
        'id': eid, 'title': meta.get('title', eid), 'short': meta.get('short') or meta.get('title', eid),
        'unit': int(meta.get('unit', 0) or 0), 'order': float(meta.get('order', 999) or 999),
        'lede': re.sub(r'<[^>]+>', '', inline(lede)),
        'def': block_html(f['Definition']),
        'ex': block_html(f.get('Example or analogy', [''])),
        'rel': block_html(f.get('Relevance to strategy', [''])),
        'dis': block_html(f.get('Where people disagree', [''])),
        'deeper': block_html(f.get('Go deeper', [''])),
        'relatedRaw': [x.strip() for x in ' '.join(f.get('Related terms', [''])).split('·') if x.strip()],
        'aliases': aliases,
        'text': text + ' ' + ' '.join(a.lower() for a in aliases) + ' ' + meta.get('title', '').lower(),
    }


def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower().replace('-', ' ')).strip()


def find_files():
    """Find the site's files whether they sit in folders or all side by side."""
    found = {'units': None, 'template': None, 'entries': [], 'players': []}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in ('public', '.git', 'node_modules')]
        for name in filenames:
            path = os.path.join(dirpath, name)
            if name == 'units.txt':
                found['units'] = path
            elif name == 'glossary.html':
                found['template'] = path
            elif name.endswith('.md') and name.lower() != 'readme.md':
                head = open(path, encoding='utf-8').read(600)
                if head.startswith('---') and re.search(r'^unit:', head, re.M):
                    found['entries'].append(path)
                elif head.startswith('---') and re.search(r'^group:', head, re.M):
                    found['players'].append(path)
    if not found['units']: problems.append('could not find units.txt')
    if not found['template']: problems.append('could not find glossary.html')
    return found


def build_glossary():
    files = find_files()
    if problems:
        return 0
    units = []
    for line in open(files['units'], encoding='utf-8'):
        if ':' in line:
            n, t = line.split(':', 1); units.append({'n': int(n), 'title': t.strip()})
    entries = [e for e in (read_entry(p) for p in sorted(files['entries'])) if e]
    ids = [e['id'] for e in entries]
    for i in set(ids):
        if ids.count(i) > 1: problems.append(f'two entries are both named {i}.md')
    entries.sort(key=lambda e: (e['unit'], e['order'], e['title'].lower()))

    # Related terms can be written as an entry's title, short name, alias, or file name.
    exact, prefix = {}, []
    for e in entries:
        for name in [e['id'], e['title'], e['short']] + e['aliases']:
            exact.setdefault(norm(name), e['id'])
        prefix.append((norm(e['title']), e['id']))

    def resolve(name):
        n = norm(name)
        if n in exact: return exact[n]
        for t, i in prefix:
            if t.startswith(n): return i
        for t, i in prefix:
            if n in t: return i
        return None

    for e in entries:
        e['related'] = []
        for r in e.pop('relatedRaw'):
            rid = resolve(r)
            if not rid:
                problems.append(f'{e["id"]}.md: related term "{r}" does not match any entry')
            elif rid != e['id'] and rid not in e['related']:
                e['related'].append(rid)
        del e['order']

    data = json.dumps({'units': units, 'entries': entries}, ensure_ascii=False).replace('</', '<\\/')
    tpl = open(files['template'], encoding='utf-8').read()
    page = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="description" content="A plain-language glossary of key ideas in AGI strategy, from the race between labs to the strategies for getting through it safely.">'
            '</head><body>\n' + tpl.replace('__DATA__', data) + '\n</body></html>\n')
    os.makedirs(os.path.join(OUT, 'glossary'), exist_ok=True)
    open(os.path.join(OUT, 'glossary', 'index.html'), 'w', encoding='utf-8').write(page)
    return len(entries)


def read_meta(path):
    raw = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    m = re.match(r'^---\n(.*?)\n---\n', raw, re.S)
    meta = {}
    for line in (m.group(1).split('\n') if m else []):
        if ':' in line:
            k, v = line.split(':', 1); meta[k.strip()] = v.strip()
    meta['id'] = os.path.splitext(os.path.basename(path))[0]
    return meta


def build_player_images():
    """Look up card images and write an image review page with credits."""
    import player_images
    cards = sorted((read_meta(p) for p in find_files()['players']),
                   key=lambda c: (int(c.get('group', 0) or 0), float(c.get('order', 0) or 0)))
    if not cards:
        return 0, 0
    imgs = player_images.find_images(cards)
    os.makedirs(os.path.join(OUT, 'players', 'credits'), exist_ok=True)
    json.dump(imgs, open(os.path.join(OUT, 'players', 'images.json'), 'w'), ensure_ascii=False, indent=1)
    e = lambda s: html.escape(s or '', quote=True)
    rows = []
    for c in cards:
        i = imgs.get(c['id'])
        if i:
            lic = f'<a href="{e(i["licenseUrl"])}">{e(i["license"])}</a>' if i['licenseUrl'] else e(i['license'])
            rows.append(f'<li><img src="{e(i["thumb"])}" alt="" loading="lazy"><div><b>{e(c.get("title"))}</b>'
                        f'<span>{e(i["author"])} · {lic} · <a href="{e(i["page"])}">source</a></span>'
                        f'<code>{e(c["id"])}.md</code></div></li>')
        else:
            rows.append(f'<li class="none"><div class="ph">no image</div><div><b>{e(c.get("title"))}</b>'
                        f'<span>Icon for now. Add a Commons file on the card\'s <code>image:</code> line to use one.</span>'
                        f'<code>{e(c["id"])}.md</code></div></li>')
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1"><title>Player card images</title>'
            '<meta name="robots" content="noindex"><style>'
            'body{font:15px/1.45 system-ui,sans-serif;margin:0 auto;max-width:980px;padding:24px 16px;background:#F2F5FA;color:#1b2333}'
            'h1{font-size:22px}ul{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}'
            'li{background:#fff;border-radius:10px;padding:10px;display:flex;gap:12px;align-items:flex-start;box-shadow:0 1px 3px rgba(0,0,0,.08)}'
            'img,.ph{width:96px;height:96px;object-fit:cover;border-radius:8px;flex:none;background:#e5e9f0}'
            '.ph{display:flex;align-items:center;justify-content:center;font-size:12px;color:#667}'
            'span{display:block;font-size:12.5px;color:#4a5568;margin:4px 0}code{font-size:11.5px;color:#2B59C3}a{color:#2B59C3}'
            '</style></head><body><h1>Player card images</h1>'
            f'<p>{len(imgs)} of {len(cards)} cards have a freely licensed image from Wikimedia Commons. '
            'To change one, edit the <code>wiki:</code> line (which Wikipedia article to borrow the main image from) '
            'or the <code>image:</code> line (a specific Commons file, or <code>none</code>) in that card\'s file.</p>'
            '<ul>' + ''.join(rows) + '</ul></body></html>')
    open(os.path.join(OUT, 'players', 'credits', 'index.html'), 'w', encoding='utf-8').write(page)
    return len(imgs), len(cards)


if __name__ == '__main__':
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT)
    n = build_glossary()
    # The home page sends visitors to the glossary until there is more to show.
    open(os.path.join(OUT, '_redirects'), 'w').write('/ /glossary/ 302\n')
    if problems:
        print('Build stopped. Fix these and try again:\n  ' + '\n  '.join(problems))
        sys.exit(1)
    print(f'Built {n} glossary entries into public/')
    # The helper scripts may sit at the top level or in a folder; find them either way.
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in ('public', '.git')]
        if 'build_players.py' in filenames or 'players_data.py' in filenames or 'player_images.py' in filenames:
            sys.path.insert(0, dirpath)
    import build_players
    r = build_players.build(ROOT, os.path.join(OUT, 'players-and-incentives'))
    if r:
        print(f'Built Players and Incentives: {r[0]} cards, {r[1]} links')
    got, total = build_player_images()
    if total:
        print(f'Found images for {got} of {total} player cards (see /players/credits/)')
