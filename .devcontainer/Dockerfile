# syntax=docker/dockerfile:1
# Adapted from https://hub.docker.com/r/noneabove1182/lmstudio-cuda/tags

# Latest ubuntu
FROM ubuntu:24.04

# Install dependencies
RUN apt-get update \
    && apt-get -y install sudo \
    && apt-get -y install git \
    && apt-get -y install htop \
    && apt-get -y install tmux \
    && apt-get -y install wget \
    && apt-get -y install unzip \
    && apt-get -y install python3 \
    && apt-get -y install python3-pip \
    # To test GUI applications
    && apt-get -y install x11-apps \
    # Dependencies for LM-Studio
    && apt-get -y install libfuse2 libglib2.0-0 libnss3-dev libdbus-1-3 libgtk-3-dev libgtk2.0-0t64 libgtk-3-0t64 libgbm-dev libnotify-dev libnss3 libxss1 libasound2t64 libxtst6 xauth xvfb \
    && apt-get clean 

# Set user and group IDs
ARG USERNAME=default_user
ARG USER_UID=2000
ARG USER_GID=$USER_UID

RUN groupadd --gid "$USER_GID" "$USERNAME" \
    && useradd --uid "$USER_UID" --gid "$USER_GID" -m "$USERNAME" \
    # Add sudo support. Omit if you don't need to install software after connecting.
    && echo "$USERNAME" ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/"$USERNAME" \
    && chmod 0440 /etc/sudoers.d/"$USERNAME" \
    && chsh -s /bin/bash "$USERNAME"

USER $USERNAME

# Set working directory
WORKDIR /home/$USERNAME

# Copy files to working directory
ARG PROJECT_DIR="$PROJECT_DIR"
COPY . "$PROJECT_DIR"

# Alias python3 to python
RUN echo "alias python=/usr/bin/python3" >> ~/.bashrc \
    && echo "alias pip=/usr/bin/pip3" >> ~/.bashrc

# Get LM-Studio
RUN wget -O LM-Studio.AppImage https://installers.lmstudio.ai/linux/x64/0.3.11-1/LM-Studio-0.3.11-1-x64.AppImage

# Update permissions
RUN chmod u+x LM-Studio.AppImage

# Extract LM-Studio
RUN ./LM-Studio.AppImage --appimage-extract \
    && mv squashfs-root lm-studio
    # && echo '{"path":"/lm-studio","argv":["/lm-studio"],"cwd":"'$HOME'"}' > ~/.lmstudio/.internal/app-install-location.json
