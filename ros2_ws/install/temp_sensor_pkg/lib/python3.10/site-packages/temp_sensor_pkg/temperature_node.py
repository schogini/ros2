import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TemperatureNode(Node):

    def __init__(self):
        super().__init__('temperature_node')

        self.publisher_ = self.create_publisher(
            Float32,
            'temperature',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_temperature)

        self.get_logger().info("Temperature sensor node started.")

    def publish_temperature(self):
        temp_msg = Float32()
        temp_msg.data = random.uniform(20.0, 35.0)

        self.publisher_.publish(temp_msg)

        self.get_logger().info(
            f"Publishing temperature: {temp_msg.data:.2f} °C"
        )

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()