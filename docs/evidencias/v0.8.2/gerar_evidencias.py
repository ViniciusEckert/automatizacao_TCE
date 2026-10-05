from pathlib import Path
import base64,json
from app import create_app
from src.salarial.revisao_service import extrair_para_revisao
p=Path('docs/evidencias/v0.8.2');p.mkdir(parents=True,exist_ok=True)
c=create_app().test_client()
r=c.get('/api/automacao/exemplo-financeiro');assert r.status_code==200
(p/'financeiro.xlsx').write_bytes(base64.b64decode(r.json['arquivo']['conteudo_base64']))
for name,route in [('cafezal','cafezal-do-sul-2026'),('curitiba','curitiba-administrativo-2026')]:
 d=c.get('/api/salarios/amostras/'+route).json
 for endpoint,ext in [('exportar-excel','xlsx'),('relatorio-pdf','pdf')]:
  r=c.post('/api/salarios/'+endpoint,json=d);assert r.status_code==200,(endpoint,r.json)
  (p/(name+'.'+ext)).write_bytes(r.data)
for name in ['curitiba.pdf','londrina.pdf','ponta-grossa.html','cafezal.html','maringa.html']:
 source=Path('referencias/fontes_salariais_2026_09_07')/name
 if not source.exists():continue
 d=extrair_para_revisao(name,source.read_bytes())
 (p/(name+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2))
 print(name,len(d['candidatos']))
 if name=='londrina.pdf':
  a=d['candidatos'][0];assert a['classes']==[str(i) for i in range(1,129)]
  assert a['niveis'][0]['valores'][0]==2150.79
  print('Londrina ordem 1..128 e NH inicial conferidos')
 if name=='curitiba.pdf':
  a=d['candidatos'][0];assert a['niveis'][0]['valores'][0]==2180.44
  print('Curitiba primeiro candidato:',len(a['classes']),len(a['niveis']))
print('rotas',len(list(c.application.url_map.iter_rules())))
