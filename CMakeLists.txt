cmake_minimum_required(VERSION 3.8)
project(siyi_zt30_camera)

# Find required packages
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Install Python nodes
install(
  PROGRAMS
  siyi_zt30_cam.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Package the project
ament_package()
