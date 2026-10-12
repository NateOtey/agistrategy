"""Find a freely licensed image and its credit for each player card.

Called by build.py. For each card it looks up the Wikipedia article named on the
card's "wiki:" line, takes that article's main image only if it is freely
licensed, and reads the author and license from Wikimedia Commons. A card's
"image:" line overrides this with a specific Commons file (e.g.
"image: File:Sam Altman 2025.jpg"), and "image: none" turns the image off.
Any lookup that fails just leaves that card with its icon; it never stops the build.
"""
import html, json, re, urllib.parse, urllib.request

UA = 'agistrategy.app-build/1.0 (https://agistrategy.app)'
WIKI = 'https://en.wikipedia.org/w/api.php'
COMMONS = 'https://commons.wikimedia.org/w/api.php'


def _get(base, params):
    params = dict(params, format='json', formatversion='2')
    url = base + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def _chunks(xs, n=40):
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


def _plain(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def lead_images(titles):
    """Wikipedia article title -> Commons file name of its free lead image."""
    out = {}
    for batch in _chunks(sorted(set(titles))):
        d = _get(WIKI, {'action': 'query', 'prop': 'pageimages', 'piprop': 'name',
                        'pilicense': 'free', 'redirects': 1, 'titles': '|'.join(batch)})
        q = d.get('query', {})
        alias = {}
        for kind in ('normalized', 'redirects'):
            for m in q.get(kind, []):
                alias[m['from']] = m['to']
        found = {p['title']: p.get('pageimage') for p in q.get('pages', [])}
        for t in batch:
            t2 = t
            for _ in range(3):
                t2 = alias.get(t2, t2)
            if found.get(t2):
                out[t] = 'File:' + found[t2]
    return out


def file_info(files):
    """Commons file name -> thumbnail URL, page URL, author, license."""
    out = {}
    for batch in _chunks(sorted(set(files))):
        d = _get(COMMONS, {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url|extmetadata',
                           'iiurlwidth': 480, 'redirects': 1, 'titles': '|'.join(batch)})
        q = d.get('query', {})
        alias = {m['from']: m['to'] for k in ('normalized', 'redirects') for m in q.get(k, [])}
        pages = {p['title']: p for p in q.get('pages', [])}
        for f in batch:
            p = pages.get(alias.get(f, f))
            if not p or not p.get('imageinfo'):
                continue
            ii = p['imageinfo'][0]
            md = ii.get('extmetadata', {})
            val = lambda k: _plain(md.get(k, {}).get('value', ''))
            lic = val('LicenseShortName')
            # Only keep files Commons marks as free to reuse.
            if not lic or 'non-free' in lic.lower() or 'fair use' in lic.lower():
                continue
            out[f] = {
                'file': f,
                'thumb': ii.get('thumburl') or ii.get('url'),
                'page': ii.get('descriptionurl'),
                'author': val('Artist') or val('Credit') or 'Unknown',
                'license': lic,
                'licenseUrl': md.get('LicenseUrl', {}).get('value', ''),
                'attributionRequired': val('AttributionRequired') != 'false',
            }
    return out


def find_images(cards):
    """cards: list of dicts with id, wiki, image. Returns id -> image info."""
    wanted = {}
    for c in cards:
        img = (c.get('image') or '').strip()
        if img.lower() == 'none':
            continue
        if img:
            wanted[c['id']] = img if img.startswith('File:') else 'File:' + img
    try:
        leads = lead_images([c['wiki'] for c in cards if c.get('wiki') and c['id'] not in wanted
                             and (c.get('image') or '').strip().lower() != 'none'])
        for c in cards:
            if c['id'] not in wanted and c.get('wiki') in leads:
                wanted[c['id']] = leads[c['wiki']]
        info = file_info(list(wanted.values()))
    except Exception as e:  # network trouble: build without images
        print(f'  (images skipped this build: {e})')
        return {}
    return {cid: info[f] for cid, f in wanted.items() if f in info}
