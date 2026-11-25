#!/usr/bin/env python3
"""Embed the selected wallpaper in a generated Discord theme."""
import base64
import mimetypes
import sys
from pathlib import Path

theme = Path(sys.argv[1]).expanduser()
wallpaper_path = Path.home() / ".local/state/quickshell/user/generated/wallpaper/path.txt"
try:
    wallpaper = Path(wallpaper_path.read_text().strip()).expanduser()
    mime = mimetypes.guess_type(wallpaper.name)[0] or "application/octet-stream"
    if not mime.startswith("image/"):
        raise ValueError(f"Not an image: {wallpaper}")
    encoded = base64.b64encode(wallpaper.read_bytes()).decode("ascii")
    with theme.open("a") as output:
        output.write(f"\n:root {{ --background-image-url: url('data:{mime};base64,{encoded}'); }}\n")
except (OSError, ValueError) as error:
    print(f"Discord wallpaper could not be embedded: {error}", file=sys.stderr)
    sys.exit(1)
