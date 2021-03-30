import os
import logging
import subprocess
import glob



def walk(path):
    fs = []
    ds = []
    for root, dirs, files in os.walk(path):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for directory in dirs:
            #paths.append(os.path.join(root, directory))
            ds.append(directory)
        for filename in files: 
            relDir = os.path.relpath(root,path)
            relFile = os.path.join(relDir,filename)
            #paths.append(os.path.join(root,filename))
            fs.append(relFile)
    return (ds,fs)

def callCmd(cmd):
    logging.info("Calling <%s>"%cmd)
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    (output,err)=p.communicate()
    if output is not None:
        logging.info("stdout: %s"%output)
    if err is not None:
        logging.error("stderr: %s"%err)

def catFile(fpath):
    # Contents of file to logger
    logging.info("Contents of <%s>"%fpath)
    if not os.path.isfile(fpath):
        logging.error("File does not exist!")
    else:
        cmd = "cat %s"%fpath
        callCmd(cmd)
    return

def catFiles(repo,fpaths):
    for fpath in fpaths:
        catFile(os.path.join(repo,fpath))

def checkFiles(repo,flist):
    logging.info("Checking existence of files/directories...") 
    yes = 0
    no = 0
    for p in flist:
        path = os.path.join(repo,p)
        test = os.path.exists(path)
        if test:
            logging.info("Does %s exist? %s"%(os.path.join(path),str(test)))
            yes+=1
        else:
            no+=1
            logging.warn("Does %s exist? %s"%(os.path.join(path),str(test)))
    if (no > 0 ):
        logging.warn("Checking File Existence: Failure: Only %d of %d files/directories exist"%(yes,yes+no))
    else:
        logging.info("Checking File Existence: Success: All %d of %d files/directories exist"%(yes,yes+no))
    return (no==0)

def checkAllFiles(repo,flist):
    allthere = True
    logging.info("Checking for %d files"%len(flist))
    for f,ii in zip(flist,range(len(flist))):
        test = checkFile(repo,f)
        if test:
            logging.info("%d: Success",ii)
        else:
            logging.error("%d: Missing",ii)
            allthere = False
    return allthere

def checkFile(repo,f):
    path = os.path.join(repo,f)
    test = os.path.isfile(path)
    logging.info("Is there a file <%s>? %s"%(path,str(test)))
    return test

def checkDir(repo,d):
    path = os.path.join(repo,d)
    test = os.path.isdir(path)
    logging.info("Is there a directory <%s>? %s"%(path,str(test)))
    return test
                 
    
    

