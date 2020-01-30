import os
import sys
import traceback
import shutil

def make_dir(path):
    dir = os.path.dirname(path)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
        
def copy_file(source, target):
    if not os.path.isfile(source):
        return
    make_dir(target)
    shutil.copyfile(source, target)
    
def copy_files(sourceDir, targetDir):
    make_dir(target)
    for file in os.listdir(sourceDir):
        srcFile = sourceDir + "/" + file
        dstFile = targetDir + "/" + file
        if not os.path.isdir(srcFile):
            shutil.copy(srcFile, dstFile)
        else:
            copy_files(srcFile, dstFile)
            
def move_file(source, target):
    if not os.path.isfile(source):
        return
    make_dir(target)
    shutil.move(source, target)
    
def execute(cmd, source, target):
    if cmd == 'copy':
        copy_file(source, target)
    elif cmd == 'copys':
        copy_files(source, target)
    elif cmd == 'move':
        move_file(source, target)
    else:
        print('cmd not an operation')
        
if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            print('fileutils argv error')
            os.system("pause")
            
        cmd = sys.argv[1]
        source = sys.argv[2]
        target = sys.argv[3]
        execute(cmd, source, target)
    except:
        traceback.print_exc()
        os.system("pause")
