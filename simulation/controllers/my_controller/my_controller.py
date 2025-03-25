"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))  # Not sure why, but Kajal said so
right_motor.setPosition(float('inf'))

left_motor.setVelocity(5.0)
right_motor.setVelocity(3.8)

left_lidar = robot.getDevice('LDS-01')
right_lidar = robot.getDevice('LDS-02')
left_lidar.enable(timestep)
right_lidar.enable(timestep)

left_lidar.enablePointCloud()
right_lidar.enablePointCloud()

ewout = []
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    range_image = left_lidar.getRangeImage()
    ewout.append(range_image)
    range_image = right_lidar.getRangeImage()
    ewout.append(range_image)
    pass

