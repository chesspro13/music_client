#!/bin/bash

on_pi="Is this being ran on a Raspberry Pi?"

function installDependancies {
  echo "Installing dependancies..."

  sudo apt-get install python3-smbus -y
  sudo apt-get install python3-vlc -y
  sudo apt-get install python3-bs4 -y
  sudo apt-get install python3-youtube_dl -y
  sudo apt-get install python3-requests -y
  sudo apt-get install python3-pafy -y
  sudo apt-get install python3-django -y
  sudo apt-get install vlc -y

  echo ''
  echo ''
  echo "Are you running this on a Raspberry Pi?"
  while true; do
      read -p "[y/n]: " yn
      case $yn in
          [Yy]*)
            echo "on_pi:__true__;;" >> config/general_config.conf;
            sudo apt-get install RPi.gpio -y;
            return 0  ;;
          [Nn]*)
            echo "on_pi:__false__;;" >> config/general_config.conf
            return  1 ;;
      esac
  done
}

function setConfig {

  > config/working_directory.conf
  echo "working_directory:__"$PWD"__\;\;" >> config/general_config.conf
}

function startServer() {
  echo "Install finished."
  echo ''
  echo ''
  echo "Do you want to start the server now?"
  while true; do
      read -p "[y/n]: " yn
      case $yn in
          [Yy]*)
            python3 homeWreker/manage.py runserver 0.0.0.0:8000
            python3 music_client/main.py
            return 0  ;;
          [Nn]*)
            return  1 ;;
      esac
  done
}

function onStartup() {
  echo ''
  echo ''
  echo "Do you want this to run on startup?"
  while true; do
      read -p "[y/n]: " yn
      case $yn in
          [Yy]*)
            > /etc/rc.local
            echo "#!/bin/sh -e" >> /etc/rc.local
            echo "python3 " $PWD"/music_client/main.py" >> /etc/rc.local
            echo "exit 0" >> /etc/rc.local


            sudo chmod +x /etc/rc.local

            echo ""
            echo ""
            echo ""
            echo "Instilation complete. Please run"
            echo ""
            echo 'sudo systemctl enable rc-local'
            echo ""
            echo "to enable the music_client to run on startup."

           # sudo systemctl enable rc-local
            return 0  ;;
          [Nn]*)
            return  1 ;;
      esac
  done
}

setConfig
installDependancies
startServer
onStartup