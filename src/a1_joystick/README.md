ros2 run joy joy_node --ros-args -p dev:=/dev/input/js0

ros2 launch teleop_twist_joy teleop-launch.py config_filepath:=/home/ros2_ws/joy_config.yaml