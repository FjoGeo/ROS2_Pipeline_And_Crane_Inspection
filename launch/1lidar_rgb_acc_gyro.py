from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import datetime

def generate_launch_description():
    current_time = datetime.datetime.now()

    return LaunchDescription([
        Node(
            package='rp_test',
            executable='talker_single',
            name='rplidar_talker'
        ),

        Node(
            package='my_realsense',
            executable='talker_rgb',
            name='my_realsense_talker'
        ),


        Node(
            package='my_realsense',
            executable='talker_acc_gyro',
            name='my_realsense_talker'
        ),


        ExecuteProcess(
            cmd=['ros2', 'bag', 'record', '-o', f'bagfile_{current_time}', 
                 'lidar_quality','lidar_angle', 'lidar_distance',               
                 '/realsense1/rgb', '/realsense1/accel', '/realsense1/gyro',
                 '/realsense2/rgb',  '/realsense2/accel', '/realsense2/gyro'
                 
                ],
            output='screen'
        )
 
    ])
