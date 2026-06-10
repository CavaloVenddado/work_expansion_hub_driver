#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from math import pi

class ExpansionHubConfigTest(Node):
    #this node is made to make the robot make some moves, so you can roughly test the configurations from config.hpp

    def __init__(self):
        super().__init__('expansion_hub_config_test')

        self.cmdVelPublisher = self.create_publisher(Twist, "cmd_vel", 10)

        self.publishCmdVelTimer = self.create_timer(0.1, self.publishCmdVel)
        self.switchCmdVelTimer = self.create_timer(5, self.switchCmdVel)

        self.forwardTwist = Twist()
        self.forwardTwist.linear.x = 0.2

        self.backwardTwist = Twist()
        self.backwardTwist.linear.x = -0.2

        self.turnLeftTwist = Twist()
        self.turnLeftTwist.angular.z = pi/5

        self.turnRightTwist = Twist()
        self.turnRightTwist.angular.z = -pi/5

        self.leftStrafeTwist = Twist()
        self.leftStrafeTwist.linear.y = 0.2

        self.rightStrafeTwist = Twist()
        self.rightStrafeTwist.linear.y = -0.2

        self.stoppedTwist = Twist()

        self.twistes = [
            self.forwardTwist,
            self.stoppedTwist,
            self.leftStrafeTwist,
            self.stoppedTwist,
            self.backwardTwist,
            self.stoppedTwist,
            self.rightStrafeTwist,
            self.stoppedTwist,
            self.turnLeftTwist,
            self.stoppedTwist,
            self.turnRightTwist
        ]

    def publishCmdVel(self):
        if len(self.twistes) > 0:
            self.cmdVelPublisher.publish(self.twistes[0])
            self.get_logger().info(f"Publishing twist {self.twistes[0]}")

    def switchCmdVel(self):
        if len(self.twistes) > 0: 
            self.twistes.pop(0)

            if len(self.twistes) == 0:
                raise SystemExit

def main(args=None):
    rclpy.init(args=args)
    node = ExpansionHubConfigTest()
    try:
        rclpy.spin(node)
    except SystemExit:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        