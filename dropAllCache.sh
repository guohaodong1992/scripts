#! /bin/bash

hosts=(99.48.237.167 99.48.237.169 99.48.237.170 99.48.237.172 99.48.237.173 99.48.237.174)

# Dispatch Drop Cache Script to every node
for host in ${hosts[*]}
do
    scp ./dropCache.sh ${host}:~/ 
done

# Call Script to Drop Cache
for host in ${hosts[*]}
do
    #ssh root@${host} sudo sync
    #ssh root@${host} sudo echo 3 > /proc/sys/vm/drop_caches && printf '%s\n' 'Ram Cache & Swap cleared'
    echo "-------- Before --------"
    ssh ${host} free -m
    ssh root@${host} sudo ~/dropCache.sh
    echo "-------- After --------"
    ssh ${host} free -m
    echo ${host}
done
