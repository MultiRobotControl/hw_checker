#!/usr/bin/env python 
import os
import sys
import logging

# Local
import hwutils
reload(hwutils)

# For local testing
# For github testing
repo='../hw'

# Number of tests
testN = 5
# Test success coutner
testCnt = 0

# Get root logger
logger = logging.getLogger()
#Have to set the root logger level, it defaults to logging.WARNING
logger.setLevel(logging.NOTSET)
fstr="%(levelname)s: %(message)s"
formatter = logging.Formatter(fstr)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# tell the handler to use this format
console.setFormatter(formatter)
logger.addHandler(console)


logging.info("Contents of repository:")
ds,fs = hwutils.walk(repo)
hwutils.callCmd('tree %s'%repo)

# Test 1
logging.info("## Exercise 1: Make a ROS Package in Your Git Repository ##")
flist = ['CMakeLists.txt','package.xml','ex1.txt'],
if hwutils.checkFiles(repo,flist):
    testCnt += 1
else:
    pass
hwutils.catFiles(repo,['ex1.txt']);


# Test 2
logging.info("## Exercise 2: Using `rospack` ##")
flist = ['ex2.txt']
if hwutils.checkFiles(repo,flist):
    testCnt += 1
else:
    pass
hwutils.catFiles(repo,flist);

# Test 3
logging.info("## Exercise 3: Driving a Turtle, One Letter ##")
flist = ['scripts/turtleletter.sh',
         'images/turtleletter.png']
if hwutils.checkFiles(repo,flist):
    testCnt += 1
else:
    pass

hwutils.catFiles(repo,['scripts/turtleletter.sh'])


# Test 4
logging.info("## Exercise 4:  Turtle Services, Two Letters ##")
flist = ['scripts/turtleletterstwo.sh',
         'images/turtleletterstwo.png']
if hwutils.checkFiles(repo,flist):
    testCnt += 1
else:
    pass

# Test 5
logging.info("## Exercise 5: Gazebo Demo ##")
flist = ['launch/YOUROBOT.launch',
         'worlds/YOUROBOT.world']
if hwutils.checkFiles(repo,flist):
    testCnt += 1
else:
    pass

# Summary
logging.info("Automated Test Summary:")
if testCnt==testN:
    logging.info("PASSED!  All %d of %d tests passed"%(testCnt, testN))
    sys.exit(0)
else:
    logging.warn("FAILED: Only %d of %d tests passed"%(testCnt, testN))
    sys.exit(1)




