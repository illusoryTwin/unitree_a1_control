import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node

def generate_launch_description():
    twist_joy_launch_path = os.path.join(
        get_package_share_directory('teleop_twist_joy'),
        'launch',
        'teleop-launch.py'
    )

    twist_joy = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(twist_joy_launch_path),
        launch_arguments={
            'config_filepath': get_package_share_directory('a1_joystick') + '/config/joy_config.yaml'
        }.items()
    )

    return LaunchDescription([
        twist_joy
    ])
