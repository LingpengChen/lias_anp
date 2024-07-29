# from package uuv_teleop
python3 traj_generator.py 

roslaunch lias_anp teleop_joy.launch
rosrun lias_anp simulator.py

rviz -d ./rviz/sim.rviz 


roslaunch lias_anp teleop_keyboard.launch
# /uuv/cmd_vel
# linear: 
#   x: 0.0
#   y: 0.0
#   z: 0.0
# angular: 
#   x: 0.0
#   y: 0.0
#   z: 0.0
roslaunch package_name start_joystick.launch joy_id:=0