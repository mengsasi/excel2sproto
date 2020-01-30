import os
import sys
import codecs
import traceback

'''local AllConfigs = {}
function AllConfigs.Init()
    require("Logic/Config/UIConfigs")
    ...
end
return AllConfigs'''

def Gen(genDir, reqPath):
    allGenPath = genDir + "/AllConfigs.lua"
    dir = os.path.dirname(allGenPath)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    file = codecs.open(allGenPath, "w", "utf-8")

    file.write("local AllConfigs = {}\n\n")
    file.write("function AllConfigs.Init()\n")

    files = os.listdir(genDir)
    for f in files:
        if os.path.splitext(f)[1] == ".lua":
            if f != "AllConfigs.lua" and f != "ConfigMgr.lua":
                f = f.replace('.lua', '')
                file.write("\trequire(\"" + reqPath + f + "\").InitModule()\n")

    file.write("end\n\nreturn AllConfigs")
    file.close()

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('genAllLua argv error')
            os.system("pause")
            
        genDir = sys.argv[1]
        reqPath = sys.argv[2]
        Gen(genDir, reqPath)
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
