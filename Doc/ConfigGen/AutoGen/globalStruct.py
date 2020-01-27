import os
import sys
import codecs

# 不弄公共结构体了，这里把每个sproto单独处理
# 如果想把sproto拼接成一个文件，然后一个sproto.parse("")
# 这时候可以弄公共结构体

gssp = "Sproto/structure.sproto"

# .item {
# 	id 0 : string
# 	count 1 : integer
# }

globalSp = {}
# globalSp['item'] = {
#     'id': {
#         'name': 'id',
#         'type': 'string'
#     },
#     'count': {
#         'name': 'count',
#         'type': 'integer'
#     }
# }

def check(key):
    return key in globalSp

def get(key):
    return globalSp[key]

def init():
    file = codecs.open(gssp, "r", 'utf-8')
    content = file.read()
    print(content)

if __name__ == '__main__':
    try:
        init()
    except:
        traceback.print_exc()
        os.system("pause")
    