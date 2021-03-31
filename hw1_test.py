#!/usr/bin/env python 
import os
import sys
import logging

# Local
import hwutils
reload(hwutils)

good_cnt = 0
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

repo='../ay21_hw1'
testN = 1
testcnt = 0

logging.info("Contents of repository:")
ds,fs = hwutils.walk(repo)

flist = ['README.md']
if hwutils.checkFiles(repo,flist):
    # Test to see if the last line of the file is
    helloworld = "Hello Git World!"
    readme=os.path.join(repo,'README.md')
    with open(readme) as f:
        for line in f:
            pass
        last_line = line
    # Strip whitespace
    ll = last_line.strip()

    # Strict comparison
    if ll == helloworld:
        testcnt += 1
        logging.info("Success: last line of the README.md file is <%s>"%helloworld)
    else:
        logging.warn("Failure: last line of the README.md file is <%s>.  It should be <%s>."%(ll,helloworld))
else:
    pass

logging.info("Automated Test Summary:")
if testcnt==testN:
    logging.info("PASSED!  All %d of %d tests passed"%(testcnt, testN))
    sys.exit(0)
else:
    logging.warn("FAILED: Only %d of %d tests passed"%(testcnt, testN))
    sys.exit(1)




