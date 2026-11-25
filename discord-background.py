#!/usr/bin/env python3
"""Embed the selected wallpaper in a generated Discord theme."""
import base64
import subprocess
import sys
from pathlib import Path

theme = Path(sys.argv[1]).expanduser()
wallpaper_path = Path.home() / ".local/state/quickshell/user/generated/wallpaper/path.txt"
try:
    wallpaper = Path(wallpaper_path.read_text().strip()).expanduser()
    # Keep the embedded URL small enough for Chromium to load reliably.
    image = subprocess.run(
        ["magick", str(wallpaper), "-resize", "1920x1080>", "-quality", "80", "jpeg:-"],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout
    encoded = base64.b64encode(image).decode("ascii")
    with theme.open("a") as output:
        output.write(f"\nbody {{ --background-image-url: url('data:image/jpeg;base64,{encoded}'); }}\n")
except (OSError, ValueError, subprocess.CalledProcessError) as error:
    print(f"Discord wallpaper could not be embedded: {error}", file=sys.stderr)
    sys.exit(1)
