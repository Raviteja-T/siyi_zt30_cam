import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="siyi_zt30_cam",
            executable="siyi_zt30_camera",
            name="zt30_camera_node",
            output="screen",
            parameters=[{
                "camera_rtsp_url": "rtsp://192.168.144.25:8554/main.264",
                "image_save_dir": "/home/ros2_ws/images"
            }]
        )
    ])
