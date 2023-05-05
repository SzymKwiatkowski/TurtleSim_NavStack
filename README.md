# Turtlebot navigation stack tests
Project purpose is to test different planning methods using navigation stack and controlling turtlebot with diff_drive_controller


# Setup
To setup workspace launch docker by following instructions in ros_ws directory. Then launch:
```bash
bash ~/setup/install_dependencies.sh
```
This script will install all required dependencies. If .repos file would not download there is a backup ready in setup directory (~/setup)

Afterwards following script can be used to update .bashrc or just edit it manually or use commands every time when entering new bash.
```bash
bash ~/setup/setup_environment
```

Also replace navigation2.launch.py file with file in setup directory. Small adjustments have been made to launch tf between map and base link so nav2 will work.


Finally build project by using:
```bash
colcon build --symlink-install
```


# Running simulator
To run gazebo turtlebot3 use command (it will take long time to load fully don't panic):
```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py 
```

To run gazebo turtlebot3 use command (it will take long time to load fully don't panic):
```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py
```