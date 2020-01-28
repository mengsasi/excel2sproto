import os
import sys
import codecs
import traceback

def Gen(genDir, reqPath):
    allGenPath = genDir + "/AllGen.lua"
    dir = os.path.dirname(allGenPath)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    file = codecs.open(allGenPath, "w", "utf-8")

    file.write("local allGen = {\n")

    files = os.listdir(genDir)
    for f in files:
        if os.path.splitext(f)[1] == ".lua":
            if f != "AllGen.lua":
                f = f.replace('.lua', '')
                file.write("\trequire(\"" + reqPath + f + "\")\n")

    file.write("}\n\nreturn allGen")
    file.close()

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('genAllGen argv error')
            os.system("pause")
            
        genDir = sys.argv[1]
        reqPath = sys.argv[2]
        Gen(genDir, reqPath)
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
