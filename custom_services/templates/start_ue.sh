#!/bin/sh

ueID=1

# TODO: don't hardcode
source /home/jrmurphy/dev/openairinterface5g/oaienv

sleep 10
/home/jrmurphy/dev/openairinterface5g/cmake_targets/ran_build/build/nr-uesoftmodem -O nrUE_proxy.conf --nokrnmod 1 --ue-idx-standalone 2 --node-number 2 --nfapi STANDALONE_PNF --sa --emulate-l1 --log_config.global_log_options level,nocolor,time,thread_id | tee nrUE.log 2>&1