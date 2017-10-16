#!/bin/bash

## bind this with key in i3wm. 


# Path to menu application
if [[ -n $(command -v rofi) ]]; then
    menu="$(command -v rofi) -dmenu"
elif [[ -n $(command -v dmenu) ]]; then
    menu="$(command -v dmenu)"
else
    echo >&2 "Rofi or dmenu not found"
    exit
fi

answer=$(python3 i3Crypto.py $@)

action=$(echo -e "Close" | $menu -p "= $answer")

case $action in
    "Close") ;;
    *) $0 "$answer $action" ;;
esac
