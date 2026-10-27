# Changes from upstream

This is the Asciiverse packaging of [Blightmud](https://github.com/Blightmud/Blightmud)
by Linus Probert and contributors (GPL-3.0; Cargo.toml says "GPL3", no "or
later"), built from upstream's v5.7.1 tag. Upstream is the `upstream`
remote; the `asciiverse` branch carries the changes below.

## Code

None. Blightmud is built exactly as released, with its default features
(spellcheck and audio).

## Packaging

- `.github/workflows/asciiverse-release.yml`: av archives for Linux (glibc,
  x86-64 and ARM64) and macOS (Intel and Apple silicon) plus SHA256SUMS,
  and .deb, .rpm and Arch packages.
- Upstream's workflows (releases, CI, coverage, audits, dependabot) are
  removed on this branch: their release job would fire on our tags, and
  this repository only packages.
- `asciiverse/nfpm.yaml`: system packages named `blightmud-asciiverse`, so
  they never collide with upstream's own .deb or a distribution package.

## Why the Linux build is not static

Sound goes through ALSA. A statically linked ALSA cannot load its plugins,
and on current desktops sound reaches PipeWire or PulseAudio through
exactly those plugins, so a static build would be silent. The glibc build
links libasound, libstdc++ (hunspell) and zlib from the system and needs
glibc 2.34 or newer (Ubuntu 22.04, Debian 12, Fedora 35 and later).

The .deb depends on `libasound2t64 | libasound2`, in that order: on Ubuntu
24.04 the name libasound2 is also provided by liboss4-salsa-asound2, which
lacks symbols Blightmud needs (`snd_pcm_info_get_stream`), and apt picks it
when libasound2 comes first.

## Not built

- Windows: upstream has no native Windows support (termion); it runs under WSL.
- Alpine: a glibc build cannot use Alpine's musl libstdc++.

## Ours

- **How to play it, at the top of README.md.** A short note on installing and
  starting it with av, or from a release archive; the original text follows
  unchanged.
