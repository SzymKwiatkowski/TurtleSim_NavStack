#!/bin/bash

wget https://raw.githubusercontent.com/ipa-rwu/turtlebot3/foxy-devel/turtlebot3.repos

vcs import /home/ws/src < turtlebot3.repos

sudo sh -c 'echo \
"deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main"\
> /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-key 0xAB17C654
sudo apt update && sudo apt install python3-vcstool

rosdep update
rosdep install --from-paths src --ignore-src  -y

sudo apt install ros-$ROS_DISTRO-dynamixel*
sudo apt install ros-$ROS_DISTRO-turtlebot3*

rm turtlebot3.repos