#!/bin/bash
# https://bobcares.com/blog/docker-exec-format-error/
printf "WAIT: This container will wait forever doing nothing \n"
# while :; do sleep 1; done
tail -f /dev/null
printf "Finishing entrypoint \n"