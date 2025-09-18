cmake_minimum_required(VERSION 3.8)
project(sdrc_navigation)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_compiler_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find necessary ROS 2 packages
find_package(ament_cmake REQUIRED)

# Install the Python executable script
install(PROGRAMS
  scripts/mock_gnss_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install the launch and config directories
install(
  DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()