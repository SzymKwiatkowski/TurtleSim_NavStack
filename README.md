# NAV2 ros2 humble planners
Repository uses navigation2 and turtlebot3 to plan paths via different planners specified in settings. Planners implemented by default are:
- NavFn Planner
- SmacPlanner2d
- ThetaStarPlanner
  
All are described on navigation [website](https://navigation.ros.org/plugins/index.html)

## Used options
Project uses:
- map server,
- amcl with DifferentialMotionModel of robot,
- bt_navigator,
- controller server DWBLocalPlanner with simple progress and goal checker,
- waypoint_follower,
- robot_state_publisher,
- Global and local costmaps with inflation, obstacle and voxel layers.

By default rviz2 is launched so operator can use graphical tools (`Nav2 Goal`) to control robot.
# Requirements:
Necessery packages are:
- navigation2
- turtlebot3_gazebo
- nav2_bringup

All can be installed via rosdep.

# Install
To use package install requirements by using:
```bash
rosdep install --from-path src -y --rosdistro $ROS_DISTRO
```

# Usage:
Build project by:
```bash
colcon build --symlink-install
```
And then source to:
```bash
source install/setup.bash
```

In terminal use:
```bash
export TURTLEBOT3_MODEL=waffle
```

This enable turtlebot3_gazebo simulator by giving it model variable. Then to run simulator use:
```bash
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```

Afterwards you can run navigator in separate terminal:
1. Navfn
```bash
ros2 launch navigation2_turtle navigation2_navfn.launch.py
```

2. Smac 2d 
```bash
ros2 launch navigation2_turtle navigation2_smac2d.launch.py 
```

3. Theta Star
```bash
ros2 launch navigation2_turtle navigation2_theta_star.launch.py 
```

You can also use different planner by changing and configuring it in planner_server parameters in `.yaml` file in `param` directory.