import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='motor_command_node',
            executable='motor_command_node',
            name='motor_command_node',
            output='screen',
        ),
        Node(
            package='motor_command_node',
            executable='motor_control_node',
            name='motor_control_node',
            output='screen',
        ),
    ])
