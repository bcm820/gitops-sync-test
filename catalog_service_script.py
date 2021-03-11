import sys
import json
import os
import shutil
from pathlib import Path

stdin = sys.stdin.read()

if stdin.isspace() or stdin == "":
    raise ValueError("stdin should have content")

wd = sys.argv[1]

folder = Path(os.path.join(wd, 'catalog-services'))
    
folder.mkdir(exist_ok=True)

js = json.loads(stdin)

for service in js:
  path = os.path.join(service['mesh_id']+"-"+service['service_id']+".json")
  service.pop('mesh_type')
  service.pop('localities')
  service.pop('instances')
  service.pop('metadata')
  service.pop('status')
  with open(folder/path, "w") as file:
    file.write(json.dumps(service, indent=2))
