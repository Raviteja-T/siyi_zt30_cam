import cv2
import rclpy
import os
from datetime import datetime

from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import Trigger

class SiyiZT30Camera(Node):
    def __init__(self):
        super().__init__("zt30_camera_node")

        # Declare and get parameters
        self.declare_parameter("camera_rtsp_url", "rtsp://192.168.144.25:8554/main.264")
        self.declare_parameter("image_save_dir", "/home/ros2_ws/images")

        self.camera_rtsp_url = self.get_parameter("camera_rtsp_url").value
        self.image_save_dir = self.get_parameter("image_save_dir").value

        # Ensure the directory exists
        os.makedirs(self.image_save_dir, exist_ok=True)

        # Open camera stream
        self.capture = cv2.VideoCapture(self.camera_rtsp_url)
        self.bridge = CvBridge()

        # ROS Publisher
        self.image_publisher = self.create_publisher(Image, "zt30/captured_image", 10)

        # ROS Service
        self.srv = self.create_service(Trigger, "capture_photo", self.capture_photo_callback)

        self.get_logger().info(f"SIYI ZT30 Camera node started with RTSP URL: {self.camera_rtsp_url}")

    def capture_photo_callback(self, request, response):
        ret, frame = self.capture.read()
        if not ret:
            self.get_logger().error("Failed to capture image!")
            response.success = False
            response.message = "Capture failed"
            return response

        # Save image
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = os.path.join(self.image_save_dir, f"zt30_{timestamp}.jpg")
        cv2.imwrite(image_filename, frame)

        # Convert and publish
        ros_image = self.bridge.cv2_to_imgmsg(frame, "bgr8")
        ros_image.header.stamp = self.get_clock().now().to_msg()
        self.image_publisher.publish(ros_image)

        self.get_logger().info(f"Image saved: {image_filename}")
        response.success = True
        response.message = f"Saved at {image_filename}"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SiyiZT30Camera()
    rclpy.spin(node)
    node.capture.release()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
