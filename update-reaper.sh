#!/bin/sh

# Neofetch
rm -rf ./neofetch/*
cp /home/dehys/.config/neofetch/config.conf ./neofetch/config.conf

# Qtilecat
rm -rf ./qtile/*
cp -R /home/dehys/.config/qtile/* ./qtile/ 

# Picom
rm -rf ./picom/*
cp /home/dehys/.config/picom/picom.conf ./picom/picom.conf

# Kitty
rm -rf ./kitty/*
cp /home/dehys/.config/kitty/kitty.conf ./kitty/kitty.conf

git add .
if [ "$1" ]; then
	git commit -m "$1"
else
	git commit -m "Reaper update"
fi
git push

