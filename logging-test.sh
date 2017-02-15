#! /usr/bin/env bash
#syslog -s -f ~/Library/Logs/test.log \

syslog -s -k Facility com.apple.console \
             Level Info \
             Sender Test_Script \
             Message "This is a test - ignore"
