#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#starting utility applications at boot time
un xfce4-power-manager &
numlockx on &
blueberry-tray &
#picom --config $HOME/.config/qtile/scripts/picom.conf &
picom --experimental-backends &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

#starting user applications at boot time
run volumeicon &
nitrogen --restore &
mullvad-vpn &
cmst &
/usr/bin/emacs --daemon &

