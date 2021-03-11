#!/bin/bash

set -euxo pipefail

export GREYMATTER_CATALOG_MESH=my-mesh

mkdir -p zone-0
mkdir -p zone-1
mkdir -p my-mesh

greymatter export-zone zone-0 | python3 fabric_script.py $PWD/zone-0
greymatter export-zone zone-1 | python3 fabric_script.py $PWD/zone-1
greymatter get catalog-mesh my-mesh | python3 catalog_mesh_script.py $PWD
greymatter list catalog-service | python3 catalog_service_script.py $PWD

git add .
git commit -m 'update'
git push
