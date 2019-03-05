# Copyright (c) 2019 Horizon Robotics. All Rights Reserved.
import random
import social_bot.pygazebo as bot
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

import time
import psutil
import os

bot.initialize()
world = bot.new_world_from_file("./turtlebot.world")
world.info()

agent = world.get_agent()
print(agent.get_joint_names())

sleep(1)

steps = 0
t0 = time.time()
for i in range(10000000):
    steps += 1
    agent.take_action({
        "turtlebot::turtlebot::wheel_left_joint":
        random.random() * 0.001,
        "turtlebot::turtlebot::wheel_right_joint":
        random.random() * 0.002
    })
    len = 100
    for i in range(len):
        world.step()
    pose = agent.get_pose()
    # agent.set_pose(((5, random.random() * 5, 0), (0, 0, 0)))
    # print(pose)        
    print("steps=%s" % steps +
                     " frame_rate=%s" % (steps / (time.time() - t0)))