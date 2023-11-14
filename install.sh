#!/bin/sh

echo Adding custom_services directory to /etc/core/core.conf
# sudo grep -F "custom_config_services_dir = " /etc/core/core.conf
sudo sed -e "s|^custom_config_services_dir.*|& ${PWD}/custom_services|g" /etc/core/core.conf # Add -i to replace in place


# TODO: Need to also install custom node types (assuming we don't just add/remove services from a built-in)