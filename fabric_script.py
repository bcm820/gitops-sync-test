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

for key, val in js.items():
    if key == "shared_rules":
        key = "rules"
    elif key == "zone":
        key = "zones"

    folder = Path(os.path.join(wd, key))

    if folder.exists():
        shutil.rmtree(folder)

    folder.mkdir(exist_ok=True)
    if key == 'zones':
        path = os.path.join(val["checksum"]+".json")
        with open(folder/path, "w") as file:
            val['checksum'] = ''
            file.write(json.dumps(val, indent=2))
    else:
        if val != None:
            for obj in val:
                path = f'{obj["checksum"]}.json'
                with open(folder/path, "w") as file:
                    obj['checksum'] = ''
                    file.write(json.dumps(obj, indent=2))
