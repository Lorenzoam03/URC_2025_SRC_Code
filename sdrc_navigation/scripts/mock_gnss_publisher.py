#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class MockGNSSPublisher(Node):
    def __init__(self):
        super().__init__("mock_gnss_publisher")
        self.publisher_ = self.create_publisher(NavSatFix, "/gps/fix", 10)
        self.timer = self.create_timer(1.0, self.publish_gnss)
        self.get_logger().info("Mock GNSS publisher started.")

    def publish_gnss(self):
        msg = NavSatFix()
        msg.latitude = 34.0522  # Example lat
        msg.longitude = -118.2437  # Example lon
        msg.altitude = 100.0  # Example altitude
        msg.status.status = 1  # Status: GNSS fix
        msg.position_covariance_type = 1  # Diagonal covariance
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published GNSS: {msg.latitude}, {msg.longitude}")

def main(args=None):
    rclpy.init(args=args)
    node = MockGNSSPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()