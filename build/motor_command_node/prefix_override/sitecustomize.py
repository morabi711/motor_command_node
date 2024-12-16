import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mariam/dev_ws/src/motor_command_node/install/motor_command_node'
