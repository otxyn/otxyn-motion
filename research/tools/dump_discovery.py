import json, pathlib
d = pathlib.Path(__file__).resolve().parent.parent / '.discovery'
for name in ['composition.json','particles.json','transitions.json','typography.json','liquid.json','3d-shaders.json','handbook.json']:
    p = d / name
    if not p.exists():
        print('missing', name); continue
    j = json.loads(p.read_text(encoding='utf-8'))
    print('===', name, len(j['candidates']))
    for c in j['candidates']:
        repo = (c.get('repository_url') or '').replace('https://github.com/','')
        lic = (c.get('licensing') or {}).get('license','unverified')
        si = 'S' if (c.get('inspection') or {}).get('source_inspected') else '-'
        bi = 'B' if (c.get('inspection') or {}).get('browser_inspected') else '-'
        sub = c.get('subcategory') or c.get('final_subcategory')
        print("%s [%s] %s | %s | %s | src:%s br:%s" % (c['id'], sub, str(c['name'])[:56], repo, lic, si, bi))
