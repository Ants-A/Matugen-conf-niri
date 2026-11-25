# Matugen-conf-niri

## Pixie SDDM wallpaper

Matugen converts each applied wallpaper to JPEG for the Pixie login screen. Run this once to allow your user to update the assets directory and background without sudo:

```sh
sudo chown "$USER" /usr/share/sddm/themes/pixie/assets /usr/share/sddm/themes/pixie/assets/background.jpg
```

The directory and image must remain readable by SDDM. A theme reinstall may reset their ownership, requiring the command to be run again.
