#!/usr/bin/env bash

# open -a /Applications/Utilities/Terminal.app/ macos_settings

# Test idea of opening a shell script...

cd ${HOME}/_git/_os-x/config/mac_setup/macos_settings.app/Contents/MacOS/
echo "I am here: $PWD"

echo
echo "    About to optimize some settings for your account."
echo "    Any changes are displayed on screen and written to a log file. "
echo "    Use the Console utility to view the log file."
echo

read -p "Do you want to proceed? [y/n] " answer
case $answer in
   [yY]* ) echo "..."
           ./macos_settings.py
           ;;

   [nN]* ) exit;;

   * )     echo "Please enter Y or N."
           ;;
esac



