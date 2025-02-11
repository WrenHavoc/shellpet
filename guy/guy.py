# ----------[Little guy!!!]----------


import os, random, time

# set poses
idle_pose = "./assets/guy_idle.txt"
wave_pose = "./assets/guy_wave.txt"

# RNG
while True:
    pose = random.randint(1, 2)
    time.sleep(5)

# idle pose
def idle():
    print(idle_pose)

# wave pose
def wave():
    print(wave_pose)
    time.sleep(0.5)
    print(idle)
    time.sleep(0.5)

# main
idle()
