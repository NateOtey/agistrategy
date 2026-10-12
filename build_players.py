"""Build the Players and Incentives page. Called from build.py; also runnable alone."""
import glob, html, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import players_data as PD


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+(?:\([^)\s]*\))?[^)\s]*)\)',
               lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![*\w])\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    return t


def find(root):
    players, groups = [], None
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ('public', '.git')]
        for n in filenames:
            p = os.path.join(dirpath, n)
            if n == 'groups.txt':
                groups = p
            elif n.endswith('.md') and n.lower() != 'readme.md':
                head = open(p, encoding='utf-8').read(600)
                if head.startswith('---') and re.search(r'^group:', head, re.M):
                    players.append(p)
    return players, groups


def read_card(path):
    raw = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.S)
    meta = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            k, v = line.split(':', 1); meta[k.strip()] = v.strip()
    fields = []
    for line in m.group(2).strip().split('\n'):
        mm = re.match(r'^\*\*([^*]+):\*\*\s?(.*)$', line)
        if mm:
            fields.append([mm.group(1), inline(mm.group(2))])
        elif line.strip() and fields:
            fields[-1][1] += ' ' + inline(line.strip())
    cid = os.path.splitext(os.path.basename(path))[0]
    plain = re.sub(r'<[^>]+>', '', ' '.join(f[1] for f in fields))
    first = re.sub(r'<[^>]+>', '', fields[0][1]) if fields else ''
    lede = re.split(r'(?<=[.!?])\s+(?=[A-Z"])', first)[0]
    title = meta.get('title', cid)
    sort = re.sub(r'^(the|The)\s+', '', title).lstrip('"')
    return {'id': cid, 'title': title, 'group': int(meta.get('group', 0)), 'order': float(meta.get('order', 0)),
            'updated': meta.get('updated', ''), 'fields': fields, 'lede': html.unescape(lede),
            'text': html.unescape((title + ' ' + plain).lower()), 'sort': sort}


def build(root, out_dir, artifact_path=None):
    paths, gpath = find(root)
    if not paths:
        return 0
    cards = sorted((read_card(p) for p in paths), key=lambda c: (c['group'], c['order']))
    groups = []
    for line in open(gpath, encoding='utf-8'):
        if ':' in line:
            n, t = line.split(':', 1); groups.append({'n': int(n), 'title': t.strip()})
    ids = {c['id'] for c in cards}
    problems = []
    for e in PD.EDGES:
        for x in e[:2]:
            if x not in ids: problems.append(f'relationship mentions unknown player "{x}"')
    for f in PD.FIGHTS:
        for p in [p for s in f['sides'] for p in s['players']] + f['swing']:
            if p[0] not in ids: problems.append(f'fight "{f["id"]}" mentions unknown player "{p[0]}"')
    for t in PD.TIMELINE:
        for x in t[3]:
            if x not in ids: problems.append(f'timeline event "{t[1]}" mentions unknown player "{x}"')
    for r in PD.STACK:
        for p in r['us'] + r['cn'] + r['levers']:
            if p[0] not in ids: problems.append(f'supply chain mentions unknown player "{p[0]}"')
    if problems:
        print('Players page problems:\n  ' + '\n  '.join(sorted(set(problems))))
    data = {
        'cards': [{k: c[k] for k in ('id', 'title', 'group', 'updated', 'fields', 'lede', 'text', 'sort')} for c in cards],
        'groups': groups,
        'edges': [list(e) for e in PD.EDGES if e[0] in ids and e[1] in ids],
        'fights': PD.FIGHTS,
        'money': {'top': PD.MONEY_NODES_TOP, 'bottom': PD.MONEY_NODES_BOTTOM, 'flows': PD.MONEY_FLOWS},
        'scale': PD.SCALE,
        'stack': PD.STACK,
        'timeline': sorted(PD.TIMELINE, key=lambda t: t[0]),
    }
    blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    tpl = open(os.path.join(root, 'templates', 'players.html'), encoding='utf-8').read() if os.path.exists(os.path.join(root, 'templates', 'players.html')) else open(os.path.join(root, 'players.html'), encoding='utf-8').read()
    body = tpl.replace('__DATA__', blob)
    os.makedirs(out_dir, exist_ok=True)
    page = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="description" content="Who is shaping the transition to advanced AI, what each one wants, and who stands in its way.">'
            '</head><body>\n' + body + '\n</body></html>\n')
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(page)
    if artifact_path:
        open(artifact_path, 'w', encoding='utf-8').write(body)
    return len(cards), len(data['edges']), len(problems)


if __name__ == '__main__':
    r = build(ROOT, os.path.join(ROOT, 'public', 'players-and-incentives'), sys.argv[1] if len(sys.argv) > 1 else None)
    print('cards, links, problems:', r)
