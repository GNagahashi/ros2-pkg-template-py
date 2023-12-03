from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Parameters
    parameters = [
        # Parameters for demo_nodes_py package
        DeclareLaunchArgument(
            'exec_name',
            default_value = 'listener',
            choices = ['talker', 'listener'],
            description = (
                'ros2 run demo_nodes_py talker\n'
                'or\n'
                'ros2 run demo_nodes_py listener'
            )
        )
    ]

    # Nodes
    nodes = [
        # ros2 run ros2_pkg_template talker
        Node(
            package = 'ros2_pkg_template',
            executable = 'talker'
        ),
        # ros2 run demo_nodes_py ...
        Node(
            package = 'demo_nodes_py',
            executable = LaunchConfiguration('exec_name')
        )
        # Node(
        #     package = 'package_name',
        #     executable = 'executable_name',
        #     parameters=[
        #         {'param_1': LaunchConfiguration('param_1')},
        #         {'param_2': 'param_2'},
        #     ]
        # )
    ]

    actions = parameters + nodes

    return LaunchDescription(actions)