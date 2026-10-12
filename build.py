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


def build_glossary():
    gdir = os.path.join(ROOT, 'glossary')
    units = []
    for line in open(os.path.join(gdir, 'units.txt'), encoding='utf-8'):
        if ':' in line:
            n, t = line.split(':', 1); units.append({'n': int(n), 'title': t.strip()})
    entries = [e for e in (read_entry(p) for p in sorted(glob.glob(os.path.join(gdir, 'entries', '*.md')))) if e]
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
    tpl = open(os.path.join(ROOT, 'templates', 'glossary.html'), encoding='utf-8').read()
    page = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="description" content="A plain-language glossary of AGI strategy terms, organized by the units of BlueDot Impact\'s AGI Strategy course.">'
            '</head><body>\n' + tpl.replace('__DATA__', data) + '\n</body></html>\n')
    os.makedirs(os.path.join(OUT, 'glossary'), exist_ok=True)
    open(os.path.join(OUT, 'glossary', 'index.html'), 'w', encoding='utf-8').write(page)
    return len(entries)


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
