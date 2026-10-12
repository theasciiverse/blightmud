# Blightmud (Asciiverse packaging)

The terminal MUD client in Rust by Linus Probert and contributors, packaged
for the Asciiverse catalog (kind `program`, topic `mud-client`) and as
system packages. Not our code: keep changes small, list every one in
PATCHES.md, and offer fixes upstream.

- Remotes: `upstream` is github.com/Blightmud/Blightmud, `origin` is
  github.com/theasciiverse/blightmud.
- Branch `asciiverse` = an upstream release tag plus our commits.
- Release: tag `v<upstream version>-av.<n>` and push it; the upstream
  version tag must be in this repository too, since build.rs reads it.
- Local build like CI: `docker run --rm -v "$PWD":/src -w /src
  rust:1-bookworm sh -c 'apt-get update && apt-get install -y
  libasound2-dev libclang-dev cmake && git config --global --add
  safe.directory /src && cargo build --release'`.
- Connect from the command line: `blightmud --connect host:port [--tls]`.
