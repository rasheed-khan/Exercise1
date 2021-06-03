#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
from sensor_msgs.msg import LaserScan
from gazebo_msgs.msg import ModelStates
import time
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose
from goal_publisher.msg import PointArray
from actionlib.action_client import ActionClient
class task1:
    def __init__(self):
        #Initiated at start of program
        self.rate = rospy.Rate(10)
        rospy.Subscriber('/goals',PointArray,self.fetch_goal) #Fetch the goals from Goal Publisher
        self.pub = rospy.Publisher('/cmd_vel', Twist,queue_size=10) #Publish the velocity commands to Bot
        Client = actionlib.SimpleActionClient('/move_base', MoveBaseAction) # Action-Client to send goal requests to the 'move_base' server through a SimpleActionClient
        self.Temp = 0
    def fetch_goal(self,msg):
        global goals
        self.goals = msg.goals
        return self.goals

    def send_goal_2_movebase(self,goal):
        Client = actionlib.SimpleActionClient('/move_base',
                                              MoveBaseAction)  # Client for to send goal requests to the 'move_base' server through a SimpleActionClient
        Client.wait_for_server()

        movebase = MoveBaseGoal()  # Assigns movebase function to 'goal' variable

        movebase.target_pose.header.frame_id = "map"
        movebase.target_pose.header.stamp = rospy.Time.now()  # Set up the frame parameters
        movebase.target_pose.pose.position.x = goal[0]
        movebase.target_pose.pose.position.y = goal[1]
        movebase.target_pose.pose.position.z = 0  # Define Goal Position
        movebase.target_pose.pose.orientation.x = 0.0
        movebase.target_pose.pose.orientation.y = 0.0
        movebase.target_pose.pose.orientation.z = 0.0
        movebase.target_pose.pose.orientation.w = 1.0

        Client.send_goal(movebase)
        Client.wait_for_result(rospy.Duration(60))

        if (Client.get_state() == GoalStatus.SUCCEEDED):
            print("Goal Reached")
        else:
            rospy.loginfo("Failed to reach the Goal")
            print("The Robot failed to reach the destination")
            self.go_home()

    def go_home(self):
        Client = actionlib.SimpleActionClient('/move_base',
                                              MoveBaseAction)
        Client.action_client.cancel_all_goals()
        rospy.loginfo("Goal Cancelled! Returning to Home")
        Home = [self.goals[0].x,self.goals[0].y]
        self.send_goal_2_movebase(Home)
        self.Temp +=1 

    def go2goal(self,goal):
        self.send_goal_2_movebase(goal)

    def start_drive(self):
        rospy.sleep(1)
        start_time = rospy.Time.from_sec(time.time())
        for i in range (len(self.goals)):
            goal = [self.goals[i].x,self.goals[i].y]
            if (self.Temp == 0):
                self.go2goal(goal)
            else:
                pass

        End_time = rospy.Time.from_sec(time.time())
        Time_Taken = (End_time - start_time)*pow(10,-9)
        print("Time Taken to Complete the Task: " + str(Time_Taken) + " Seconds")

if __name__ == "__main__":
		# instantiates your class and calls the __init__ function
        rospy.init_node('robot')
        proj = task1()
        proj.start_drive()