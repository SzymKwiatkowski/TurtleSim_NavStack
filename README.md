# Turtlesim navigation stack tests
Project purpose is to test different planning methods using navigation stack and controlling turtlesim with diff_drive_controller


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

Finally build project by using:
```bash
colcon build --symlink-install
```


# Running simulator
To run gazebo turtlebot3 use command (it will take long time to load fully don't panic):
```bash
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py 
```