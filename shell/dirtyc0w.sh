# This script is for learning purpose of dirty COW lab powered by SEED from Syracuse University
# Slightly modified for Johns Hopkins University homework.

#!/bin/bash

set -eu

if [[ $EUID -eq 0 ]]; then
    echo "This lab cannot be done under root"
    exit 1
fi

trap "kill 0" SIGINT

COW_FILE="/zzz"
COW_FILE_ORIG="/zzz.bak"
dirtyc0w="/home/seed/a.out"

echo "The original file content is:"
cat $COW_FILE
echo ""
# Is running?
i=0

while :;
    do
        if cmp -s $COW_FILE $COW_FILE_ORIG
            then
            echo "COW attack in progress..."
            echo ""
            if [ $i == 0 ]; then 
                $dirtyc0w &
                COW_PID=$!
                ((++i))
            else
                echo "Attack stalled!"
                exit 1
            fi
        else
            echo "SUCCESS... The file has been changed under read only mode."
            echo "The new file content is:"
            cat $COW_FILE
            echo ""
            kill -9 $COW_PID 2>/dev/null || echo "Attack cannot be performed, please check environment setup."
            exit 1
            # TODO: cleanup if needed
        fi
        sleep 1
    done
