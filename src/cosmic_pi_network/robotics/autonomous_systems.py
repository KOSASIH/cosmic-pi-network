import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class AutonomousSystem:
    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('scan', LaserScan, self.callback)

    def callback(self, msg):
        twist = Twist()
        twist.linear.x = 0.5
        twist.angular.z = 0.5
        self.pub.publish(twist)

    def navigate(self):
        rospy.init_node('autonomous_system')
        rospy.spin()

# Example usage
system = AutonomousSystem()
system.navigate()
