import rclpy
import sys

from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class Publisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1


def main(args = None):
    rclpy.init(args = args)
    node = Publisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt as e:
        pass
    except ExternalShutdownException as e:
        sys.exit(e)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()