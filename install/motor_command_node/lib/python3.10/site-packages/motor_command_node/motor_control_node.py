import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import smbus
import time

class MotorControlNode(Node):
    def __init__(self):
        super().__init__('motor_control_node')
        self.subscription = self.create_subscription(
            String,
            'motor_commands',
            self.listener_callback,
            10)
        self.get_logger().info('Motor Control Node has been started.')

        # Initialize I2C bus and address
        self.bus = smbus.SMBus(1)
        self.address = 0x08

    def listener_callback(self, msg):
        command = msg.data
        self.get_logger().info(f'Received command: {command}')
        
        if command in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            self.bus.write_byte(self.address, ord(command))
            self.get_logger().info(f'Sent command to motor: {command}')
        else:
            self.get_logger().warn("Invalid command received. Please enter a number between 0 and 8.")

def main(args=None):
    rclpy.init(args=args)
    motor_control_node = MotorControlNode()
    rclpy.spin(motor_control_node)
    motor_control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
