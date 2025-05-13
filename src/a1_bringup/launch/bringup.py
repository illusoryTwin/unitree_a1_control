import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():
      
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
      
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        # launch_arguments={'gz_args': PathJoinSubstitution([
        #     pkg_project_gazebo,
        #     'worlds',
        #     'diff_drive.sdf'
        # ])}.items(),
    )

    return LaunchDescription([
        gz_sim
    ])
