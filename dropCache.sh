#! /bin/bash

sync
su -c "echo 3 > /proc/sys/vm/drop_caches" && printf '%s\n' 'Ram Cache & Swap cleared'

