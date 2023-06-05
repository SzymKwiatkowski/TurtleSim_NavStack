import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from tf2_msgs.msg import TFMessage


import numpy as np

class Distance(Node):
    def __init__(self):
        super().__init__('planner_distance')
        self.subscription_local_plan = self.create_subscription(Path,'/received_global_plan',self.sub_callback,10)
        self.subscription_tf = self.create_subscription(TFMessage,'/tf',self.tf_callback,10)
        self.publisher_goal = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.path_length = 0.0
        self.first_run = True
        # Long path
        # self.goal_x = -1.0
        # self.goal_y = -1.0

        # Short path
        self.goal_x = 0.5
        self.goal_y = 1.5

        self.stamp_sec = 0
        self.stamp_nanosec = 0
        
    def tf_callback(self, data):
        self.stamp_sec = data.transforms[0].header.stamp.sec
        self.stamp_nanosec = data.transforms[0].header.stamp.nanosec
        self.pub_callback()
        

    def pub_callback(self):
        goal_pose = PoseStamped()
        goal_pose.pose.position.x = self.goal_x
        goal_pose.pose.position.y = self.goal_y
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp.sec = self.stamp_sec
        goal_pose.header.stamp.nanosec = self.stamp_nanosec
        self.publisher_goal.publish(goal_pose)
    
    def sub_callback(self, data):
        if self.first_run == True:
            self.first_run = False
            for i in range(len(data.poses) - 1):
                position_a_x = data.poses[i].pose.position.x
                position_b_x = data.poses[i+1].pose.position.x
                position_a_y = data.poses[i].pose.position.y
                position_b_y = data.poses[i+1].pose.position.y
                self.path_length += np.sqrt(np.power((position_b_x - position_a_x), 2) + np.power((position_b_y- position_a_y), 2))

            print('Goal position: ', (self.goal_x, self.goal_y))
            print('Length of path: ',self.path_length)
        

def main(args=None):

    rclpy.init(args=args)
    distance = Distance()

    rclpy.spin(distance)

    distance.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
