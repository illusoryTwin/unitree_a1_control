# import os
# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
# from launch_ros.actions import Node
# from launch_ros.substitutions import FindPackageShare
# import xacro
# # import os

# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch_ros.actions import Node
# from launch.substitutions import Command
# from launch.actions import IncludeLaunchDescription, ExecuteProcess, TimerAction, LogInfo
# from launch.launch_description_sources import PythonLaunchDescriptionSource


# def generate_launch_description():

#     # Launch arguments
#     use_sim_time = LaunchConfiguration('use_sim_time', default='true')

#     a1_description_path = os.path.join(
#         get_package_share_directory('a1_description'))
#     xacro_file = os.path.join(a1_description_path, 'xacro', 'robot.xacro')
#     controller_yaml = os.path.join(a1_description_path, 'config', 'controller.yaml')
    
    
#     pkg_share = FindPackageShare(package='a1_description')
#     default_world_path = PathJoinSubstitution([pkg_share, 'world', 'normal.world'])
#     world_path = LaunchConfiguration('world', default=default_world_path)


#     pkg_gazebo_ros = FindPackageShare(package='gazebo_ros')


#     params = {'robot_description': Command(['xacro ', xacro_file]), 'use_sim_time': True}
#     # params = {'robot_description': Command(['xacro ', xacro_file, ' use_gazebo:=true DEBUG:=false']), 'use_sim_time': True}

#     # Robot State Publisher
#     node_robot_state_publisher = Node(
#         package='robot_state_publisher',
#         executable='robot_state_publisher',
#         output='both',
#         parameters=[params],
#         remappings=[
#             ('/joint_states', '/a1_gazebo/joint_states')
#         ]
#     )

#     # Joint State Publisher
#     node_joint_state_publisher = Node(
#         package='joint_state_publisher',
#         executable='joint_state_publisher',
#         output='screen',
#         parameters=[{
#             'use_sim_time': use_sim_time
#         }]
#     )

#     # Load controllers with ros2_control_node
#     ros2_control_node = Node(
#         package='controller_manager',
#         executable='ros2_control_node',
#         parameters=[params, controller_yaml],
#         output='screen',
#         namespace='a1_gazebo'
#     )

#     gazebo = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource([get_package_share_directory('gazebo_ros') + '/launch/gazebo.launch.py']),
#         launch_arguments={'world': get_package_share_directory('a1_description') + '/world/normal.world'}.items()
#     )


#     # Spawn Entity
#     spawn_entity = Node(
#         package='gazebo_ros',
#         executable='spawn_entity.py',
#         arguments=['-topic', 'robot_description',
#                    '-entity', 'a1',
#                    '-x', '0.0',
#                    '-y', '0.0',
#                    '-z', '0.1'],
#         output='screen'
#     )

#     # controller_spawner = Node(
#     #     package='controller_manager',
#     #     executable="ros2_control_node", #'spawner',
#     #     arguments=[
#     #         'FR_hip_joint', 'FR_thigh_joint', 'FR_calf_joint',
#     #         'FL_hip_joint', 'FL_thigh_joint', 'FL_calf_joint',
#     #         'RR_hip_joint', 'RR_thigh_joint', 'RR_calf_joint',
#     #         'RL_hip_joint', 'RL_thigh_joint', 'RL_calf_joint',
#     #         '--controller-manager-timeout', '60'
#     #     ],
#     #     namespace='a1_gazebo',
#     #     output='screen',
#     #     parameters=[controller_yaml]  # Loading controller YAML here
#     # )



#     # controller manager
#     controller_manager = Node(
#         package='controller_manager',
#         executable='ros2_control_node',
#         parameters=[params, os.path.join(
#             get_package_share_directory('a1_description'),
#             'config',
#             'controller.yaml'
#         )],
#         output='screen'
#     )


#     # controller manager
#     controller_manager = Node(
#         package='controller_manager',
#         executable='ros2_control_node',
#         parameters=[params, os.path.join(
#             get_package_share_directory('a1_description'),
#             'config',
#             'controller.yaml'
#         )],
#         output='screen'
#     )

#     # log info
#     log_info = LogInfo(msg="Launching controller manager and loading controllers...")

#     # load controllers with a delay to ensure controller_manager is ready
#     load_controllers = [
#         TimerAction(
#             period=5.0,  # delay in seconds
#             actions=[
#                 ExecuteProcess(
#                     cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', controller],
#                     output='screen'
#                 )
#             ]
#         )
#         for controller in [
#             'joint_state_controller',
#             'FL_hip_controller',
#             'FL_thigh_controller',
#             'FL_calf_controller',
#             'FR_hip_controller',
#             'FR_thigh_controller',
#             'FR_calf_controller',
#             'RL_hip_controller',
#             'RL_thigh_controller',
#             'RL_calf_controller',
#             'RR_hip_controller',
#             'RR_thigh_controller',
#             'RR_calf_controller'
#         ]
#     ]


#     # # Launch Description
#     # ld = LaunchDescription()

#     # # # Add Launch Arguments
#     # ld.add_action(DeclareLaunchArgument('use_sim_time', default_value='true'))

#     # # Add nodes
#     # ld.add_action(node_robot_state_publisher)
#     # ld.add_action(node_joint_state_publisher)
#     # ld.add_action(gazebo)
#     # # ld.add_action(ros2_control_node)
#     # ld.add_action(spawn_entity)
#     # # ld.add_action(controller_manager)
#     # return ld

#     return LaunchDescription([node_robot_state_publisher, node_joint_state_publisher, gazebo, spawn_entity, controller_manager, log_info] + load_controllers)





#     # return LaunchDescription([rsp, jsp, rviz_node])
#     return LaunchDescription([rsp, jsp, gazebo, spawn_entity] + load_controllers)

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch.actions import IncludeLaunchDescription, ExecuteProcess, TimerAction, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    a1_description_path = os.path.join(
        get_package_share_directory('a1_description'))
    xacro_file = os.path.join(a1_description_path, 'xacro', 'robot.xacro')
    params = {'robot_description': Command(['xacro ', xacro_file, ' use_gazebo:=true DEBUG:=false']), 'use_sim_time': True}

    # this is for publishing the robot state to ROS 2
    rsp = Node(package='robot_state_publisher',
               executable='robot_state_publisher',
               output='both',
               parameters=[params])

    # this is for sliders to control the joints
    jsp = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen',
    )

    # run gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('gazebo_ros') + '/launch/gazebo.launch.py']),
    )

    # spawn the robot in gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'a1_phuc', '-topic', 'robot_description'],
        output='screen',
    )

    # controller manager
    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[params, os.path.join(
            get_package_share_directory('a1_description'),
            'config',
            'controller.yaml'
        )],
        output='screen'
    )

    # log info
    log_info = LogInfo(msg="Launching controller manager and loading controllers...")

    # load controllers with a delay to ensure controller_manager is ready
    load_controllers = [
        TimerAction(
            period=5.0,  # delay in seconds
            actions=[
                ExecuteProcess(
                    cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', controller],
                    output='screen'
                )
            ]
        )
        for controller in [
            'joint_state_controller',
            'FL_hip_controller',
            'FL_thigh_controller',
            'FL_calf_controller',
            'FR_hip_controller',
            'FR_thigh_controller',
            'FR_calf_controller',
            'RL_hip_controller',
            'RL_thigh_controller',
            'RL_calf_controller',
            'RR_hip_controller',
            'RR_thigh_controller',
            'RR_calf_controller'
        ]
    ]

    return LaunchDescription([rsp, jsp, gazebo, spawn_entity, controller_manager, log_info] + load_controllers)