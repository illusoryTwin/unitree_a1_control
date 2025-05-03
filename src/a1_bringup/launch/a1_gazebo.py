from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    pkg_a1_description = FindPackageShare(package='a1_description')
    return LaunchDescription([
        IncludeLaunchDescription(
            Node(
                package='teleop_twist_joy',
                executable='teleop_node',
                name='teleop_twist_joy',
                output='screen'
            ),
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([pkg_a1_description, 'launch', 'test.launch.py'])
            )
        )
    ])
