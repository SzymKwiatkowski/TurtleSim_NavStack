import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from tf2_msgs.msg import TFMessage


import numpy as np

class Distance(Node):
    def __init__(self):
        super().__init__('planner_distance')
        self.subscription_local_plan = self.create_subscription(Path, '/received_global_plan',self.sub_callback,10)
        self.publisher_goal = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.path_length = 0.0
        self.first_run = True
        # Long path
        self.goal_x_long = -1.0
        self.goal_y_long = -1.0

        # Short path
        self.goal_x_short = 0.5
        self.goal_y_short = 1.5
        
        self.start_time = self.get_clock().now()
        self.publish_goal(self.goal_x_long, self.goal_y_long)
        

    def publish_goal(self, goal_x, goal_y):
        goal_pose = PoseStamped()
        goal_pose.pose.position.x = goal_x
        goal_pose.pose.position.y = goal_y
        header = Header()
        header.frame_id = 'map'
        self.start_time = self.get_clock().now()
        header.stamp = self.start_time.to_msg()
        goal_pose.header = header
        
        self.publisher_goal.publish(goal_pose)
        self.get_logger().info('Goal sent')
    
    def sub_callback(self, data: Path):
        if self.first_run == True:
            self.first_run = False
            for i in range(len(data.poses) - 1):
                position_a_x = data.poses[i].pose.position.x
                position_b_x = data.poses[i+1].pose.position.x
                position_a_y = data.poses[i].pose.position.y
                position_b_y = data.poses[i+1].pose.position.y
                self.path_length += np.sqrt(np.power((position_b_x - position_a_x), 2) + np.power((position_b_y- position_a_y), 2))

            print('Goal position: ', (self.goal_x_long, self.goal_y_long))
            print('Length of path: ',self.path_length)
            time_now = data.header.stamp.sec + data.header.stamp.nanosec * 0.000000001
            time_pose = self.start_time.seconds_nanoseconds()[0] * 1.0 + self.start_time.seconds_nanoseconds()[1] * 0.000000001
            print('Print planning time: ', time_now - time_pose)
        

def main(args=None):

    rclpy.init(args=args)
    distance = Distance()

    rclpy.spin(distance)

    distance.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
