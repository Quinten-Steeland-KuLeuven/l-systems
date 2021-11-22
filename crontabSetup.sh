#!/bin/bash

currentDirectory=$(pwd)

path="$currentDirectory/makeBackup.sh"

crontab -l > crontab_new

fullCommand="0 * * * * /bin/bash \"$path\" \"$currentDirectory\""

sed -i "1 i\\$fullCommand" crontab_new

crontab crontab_new

rm crontab_new
