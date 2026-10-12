#!/usr/bin/env python3
"""Records asciiverse/blightmud.cast, Blightmud's catalog preview, at 100x30
(hub/RECORDING.md): `blightmud --connect batmud.bat.org:2022 --tls`, showing
BatMUD's greeting, then /quit. Nothing is sent to the MUD beyond connecting.
Usage: python3 asciiverse/record-preview.py [path to blightmud binary]"""
import os, pty, shutil, struct, fcntl, select, sys, tempfile, termios, time

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
binary = sys.argv[1] if len(sys.argv) > 1 else f"{root}/target/release/blightmud"
home = tempfile.mkdtemp()
env = dict(os.environ, HOME=home, XDG_CONFIG_HOME=f"{home}/.config", XDG_DATA_HOME=f"{home}/.local/share",
           TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8")
keys = [(9.0, b"/quit\r"), (2.0, b"")]

pid, fd = pty.fork()
if pid == 0:
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q", "-i", "2",
        "--capture-env", "TERM,COLORTERM,LANG",
        "-c", f"{binary} --no-update-check --connect batmud.bat.org:2022 --tls",
        f"{root}/asciiverse/blightmud.cast"], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))
for wait, key in keys:
    end = time.time() + wait
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.05)
        if r:
            try: os.read(fd, 65536)
            except OSError: break
    if key: os.write(fd, key)
try: os.waitpid(pid, 0)
except ChildProcessError: pass
shutil.rmtree(home)
