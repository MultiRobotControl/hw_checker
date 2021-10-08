#!/usr/bin/env python 
import os
import sys
import logging

# Local
import hwutils
reload(hwutils)

# For local testing
# For github testing
repo='../ay22_hw2'

# Number o tests
testN = 4
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
logging.info("## Exercise 1: Creating Directories and Files on the Command Line ##")
flist = ['sandbox','sandbox/dir1','sandbox/dir1/file1.txt',
         'sandbox/dir2','sandbox/dir2/file2.txt','sandbox/commands.txt']
if hwutils.checkFiles(repo,flist):
    testCnt += 1
else:
    pass
hwutils.catFiles(repo,['sandbox/commands.txt']);


# Test 2
logging.info("## Exercise 2: Copying, Moving and Editing ##")
flist = ['playpen','playpen/folder1','playpen/folder1/file1.txt',
         'playpen/folder2','playpen/folder2/file2.txt','playpen/play.txt']
if hwutils.checkFiles(repo,flist):
    testCnt += 1
else:
    pass
hwutils.catFiles(repo,['playpen/play.txt']);

# Test 3
logging.info("## Exercise 3: Using Tree and Redirection ##")
flist = ['tree.out']
if hwutils.checkFiles(repo,flist):
    testCnt += 1
else:
    pass

hwutils.catFiles(repo,['tree.out']);


# Test 4
logging.info("## Exercise 5: ROS Graph ##")
flist = ['images/rosgraph_turtlesim.png']
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




