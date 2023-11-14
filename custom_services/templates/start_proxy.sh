#!/bin/sh

numUEs=${config["numue"]}
gnb_ipaddr="127.0.0.2"
proxy_ipaddr="127.0.0.1"
ue_ipaddr="127.0.0.1" # BUG: Proxy expects all the UEs to live on same IP address

sleep 5
/home/jrmurphy/dev/proxy/build/proxy $numUEs --nr $gnb_ipaddr $proxy_ipaddr $ue_ipaddr # TODO: Don't hardcode