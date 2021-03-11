# greymatter

1. Run K3D locally, then run `./sync.sh` in the CLI repo, in `docs/axon` (update the github repo information - specifically somebody to you) - this will push the exported zone to your Github repo.
2. Run `greymatter sync plan` - it should be all UPDATE
3. Run `greymatter sync apply` - which could fail with 400 error when checksum does not match, but hopefully it will succeed.
4. Run `greymatter delete route route-edge`
5. Run `greymatter sync plan`
6. Run `greymatter sync apply`
