# .files

This is a collection of all the configurations I've managed to write for different environments in Linux. Most of them use window tiling managers like qtile and dwm but there might be KDE and Gnome configurations too. This is the main branch and the main branch will always display the configuration I'm personally running myself. 

> Current: `qtile` <br>
> Branch: https://github.com/dehys/.files/tree/qtile
<br>
<br>

### Table of contents
| Configuration  | Branch | In use |
| --------  | ------------------- | --------------------- |
| qtile | [qtile](https://github.com/dehys/.files/tree/qtile) | Yes | 
| qtile-laptop | [qtile-laptop](https://github.com/dehys/.files/tree/qtile-laptop) | Yes (laptop) | 
<br>
<br>

### Installation of any configuration
```
git clone https://github.com/dehys/.files/ && cd ./.files
```
To switch to the configuration you want, replace `<branch>` with the branch name you see above
```
git checkout <branch>
```
Now use the patch executable to patch your system with the dotfiles
```
./patch
```
Optional: If you want to patch only a specific application, lets say `kitty` (see .include file for more options)
```
./patch kitty
```
<br>

> Patch and Update source code can be found in .src directory
<br>
<br>
<br>

# Qtile configuration

<img src="https://i.imgur.com/Sjhm4Pb.png">

**Software**:
- qtile (Tiling window manager written and configured in python)
- picom (Compositor for window managers)
- kitty (Feature rich terminal emulator)
- neofetch (Cli program that shows statistics of the current machine)
- ranger (Tui file explorer)
- rofi (Application launcher)

```
sudo pacman -S qtile picom kitty neofetch ranger rofi
```
