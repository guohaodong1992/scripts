#! /bin/bash

hosts=(99.48.237.167 99.48.237.169 99.48.237.170 99.48.237.172 99.48.237.173 99.48.237.174)

# Generate RSA
for host in ${hosts[*]}
do
    ssh ${host} ssh-keygen -t rsa
    ssh ${host} cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
done

# Dispatch Authorized_keys to every node
chmod -R 600 ~/.ssh/authorized_keys
for host in ${hosts[*]}
do
    scp ~/.ssh/authorized_keys ${host}:~/.ssh/
    ssh ${host} chmod -R 600 ~/.ssh/authorized_keys 
done
