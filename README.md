# Exercise1
Task assigned by Neobotix
Step 1: Downloaded the SDF files from the sources.
Step 2: Launched the Gazebo Empty world with TurtleBot3 and spawned the model.
Step3: Created the map using Rviz Gmapping.

$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

(To launch the Slam Package)

$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

(To navigate the bot using keyboard)

$ rosrun map_server map_saver -f ~/map

(Saving the created map as yaml file)


Step 4: Created Goal Publisher Package to publish the goals.

Step 5: Developed the code to send subscribed goal to move base.

Operational Commands:

Launch the Empty World: $ roslaunch turtlebot3_gazebo turtlebot3_emptyworld.launch

Spawn the SDF Model: $ rosrun gazebo_ros spawn_model -file ~<=PATH TO THE MODEL.SDF=>/model.sdf -sdf -x 3 -y -4 -model task_area

Start the RVIZ: $ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/<=PATH TO THE MAP IN MAPS FOLDER=>/map.yaml

Publish the Goals: $ roslaunch goal_publisher goal_publisher.launch

Launch the Task: $ roslaunch exercise1 exercise1.launch
