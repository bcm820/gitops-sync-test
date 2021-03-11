import sys
import json
import os
import shutil
from pathlib import Path

stdin = sys.stdin.read()

if stdin.isspace() or stdin == "":
    raise ValueError("stdin should have content")

js = json.loads(stdin)

wd = sys.argv[1]

folder = Path(os.path.join(wd, 'catalog-meshes'))

folder.mkdir(exist_ok=True)

js = js['configuration']

path = os.path.join(js['mesh_id']+".json")
with open(folder/path, "w") as file:
    file.write(json.dumps(js, indent=2))
