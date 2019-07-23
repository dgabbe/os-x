#!/usr/bin/env bash



# Test idea of opening a shell script...

cd ${HOME}/_git/_os-x/config/mac_setup/apply_settings.dist
echo "I am here: $PWD"

echo
echo "    About to optmize some settings for your account."
echo "    Any changes are displayed on screen and written to a log file "
echo "    hich the Console utitily can open. The program will display "
echo "    the location of the file."
echo

read -p "Do you want to proceed? [y/n] " answer
case $answer in
   [yY]* ) echo "Okay, just ran the cron script."
           break;;

   [nN]* ) exit;;

   * )     echo "Dude, just enter Y or N, please."; break ;;
  esac

./apply_settings

