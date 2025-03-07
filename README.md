# LM-Studio

# 1 Enable GUI
1. Install and run [VcXsrv](https://sourceforge.net/projects/vcxsrv/)
2. Add `"DISPLAY": "host.docker.internal:0"` to `"containerEnv"`

# 2 Run LM-Studio
1. Navigate to home/lm-studio
2. Run `./RunApp`
3. Can also use `./LM-Studio.AppImage --appimage-extract-and-run --no-sandbox` but this requires GUI to always be open.

# 3 LM-Studio [CLI](https://lmstudio.ai/docs/cli)
1. Run `~/.lmstudio/bin/lms bootstrap`
2. Open new terminal and run `lms`