# Sim Benchmark

A simple benchmark for pygazebo and pybullet simulator.


The scene is a turtlebot with 2 randomly moving wheels and a camera sensor. 

Pybullet incompatible sensors and plugins were removed from the turtlebot urdf file. The model file contains 2 continuous joints and 30 fixed joints.

# Test Result on Core i7-6700HQ@2.6Ghz, GTX970M
Note there are 100 substeps per one step)

Turtlebot pyBullet without camera sensor:
54.62 steps/second (5462 substeps/second), ~200% CPU Usage

Turtlebot pyBullet with camera sensor (image rendered by OpenGL) :
19.82 steps/second (1982 substeps/second), ~200% CPU Usage

Turtlebot pyBullet with camera sensor (image rendered by CPU) :
11.20 steps/second (1120 substeps/second), ~200% CPU Usage


Turtlebot pyGazebo without camera sensor:
71.06 steps/second (7106 substeps/second), ~155% CPU Usage

Turtlebot pyGazebo with camera sensor:
25.13 steps/second (2513 substeps/second), ~140% CPU Usage


# Install of PyBullet

pip install pybullet

See also the [PyBullet Quickstart Guide](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit#heading=h.2ye70wns7io3)

# Note
Change the mesh file path to absoulte path in model.urdf file at robot_df/turtlebot/
Pybullet working with relative path , but gazebo not.

