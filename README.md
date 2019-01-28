# gscn_pioneer_mission

With `nix-build`:

```sh
nix-build -I airapkgs/ -A de_dev
source result/setup.bash
roslaunch gscn_pioneer_mission mission.launch
```

With `nix-shell`:

```sh
mkdir ~/ws/src -p && cd ~/ws/src && catkin_init_workspace
git clone https://github.com/tuuzdu/gscn_pioneer_mission.git
cd ..
nix-shell -p gcc
catkin_make
exit
source devel/setup.bash
roslaunch gscn_pioneer_mission mission.launch
```
