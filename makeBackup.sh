#!/bin/bash

cd $1

cp History.txt History_backups/$(date +"%Y-%m-%dT%H:%M:%S")_History.txt
