# greymatter sync

## Preparation

1. Fork this repo and clone it to your machine.
2. In the [cli repo](github.com/greymatter-io/cli), checkout the branch `catalog-v2` and run `make install` to build a binary and install it to your `$GOPATH/bin` directory.
3. In the [gm-catalog repo](github.com/greymatter-io/gm-catalog), checkout the branch `feat/istio`. Go to `/docs/test/redis` and follow the `README.md` until you are able to create mesh and service entries.
4. Configure the included `.greymatter.yaml` config example with the following:
   1. `sync.configuration.url` should point to the forked repo
   2. `sync.credentials.privateKey`, `cipher.confiugration.privateKey`, and `cipher.configuration.publicKey` should point to generated keys for [connecting to Github with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).

## Backing up configs to your repo

1. Run `./sync.sh` in this directory to store the config state of the mesh in this directory and push it up to your remote repo
2. Inspect the contents of `my-mesh`, `zone-0` and `zone-1`.

## Syncing the mesh with your repo

1. Run `greymatter sync plan -c $PWD/.greymatter.yaml` - all actions should be UPDATE, since no `./cache` directory has been populated for storing applied config checksums
2. Run `greymatter sync apply -c $PWD/.greymatter.yaml` - this populates the local `./cache` directory with checksums of applied configs
3. Run `greymatter sync plan -c $PWD/.greymatter.yaml` again - all actions should be NOOP since the destination config state (in deployed mesh) matches the source config state (this repo)

## Applying new configs from repo changes

1. Open `catalog-services/my-mesh-catalog.json` and edit `"max_instances"` to `2`
2. Commit this change and push to your remote repo
3. Run `greymatter sync plan -c $PWD/.greymatter.yaml` - you should see an UPDATE action for catalog.
4. Run `greymatter sync apply -c $PWD/.greymatter.yaml` - you should see a MODIFY action
