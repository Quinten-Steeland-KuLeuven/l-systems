#!/bin/bash

if [[ $1 == "" ]];
then
    cd $(pwd)

else
    cd $1
fi

cp ./History/History.txt History_backups/$(date +"%Y-%m-%dT%H:%M:%S")_History.txt
