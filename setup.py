from setuptools import setup

package_name = 'motor_command_node'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    package_data={
        package_name: ['launch/*.py'],  # Include all Python files in the launch directory
    },
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='A ROS 2 package for motor command and control',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_command_node = motor_command_node.motor_command_node:main',
            'motor_control_node = motor_command_node.motor_control_node:main',
        ],
    },
)
