import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MotorCommandNode(Node):
    def __init__(self):
        super().__init__('motor_command_node')
        self.publisher_ = self.create_publisher(String, 'motor_commands', 10)
        self.get_logger().info('Motor Command Node has been started.')
        self.get_input_commands()

    def get_input_commands(self):
        while rclpy.ok():
            command = input("Enter motor command: ")
            msg = String()
            msg.data = command
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published command: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    motor_command_node = MotorCommandNode()
    rclpy.spin(motor_command_node)
    motor_command_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
