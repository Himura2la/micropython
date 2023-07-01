#!/bin/bash

usage_msg="Usage: $0 file ip_addr"
file=${1:?$usage_msg}
ip=${2:?$usage_msg}

script_dir="$(readlink -f "$(dirname "$0")")"
webrepl_pass=$(cat $script_dir/webrepl_pass.txt)

python3 \
    "$script_dir/webrepl/webrepl_cli.py" \
    -p $webrepl_pass \
    $file \
    $ip:/$file
