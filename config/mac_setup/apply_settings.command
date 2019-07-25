#!/usr/bin/env bash



# Test idea of opening a shell script...

cd ${HOME}/_git/_os-x/config/mac_setup/apply_settings.dist
echo "I am here: $PWD"

echo
echo "    About to optimize some settings for your account."
echo "    Any changes are displayed on screen and written to a log file. "
echo "    Use the Console utility to view the log file."
echo

read -p "Do you want to proceed? [y/n] " answer
case $answer in
   [yY]* ) echo "..."
           ./apply_settings
           ;;

   [nN]* ) exit;;

   * )     echo "Please enter Y or N."
           ;;
esac



