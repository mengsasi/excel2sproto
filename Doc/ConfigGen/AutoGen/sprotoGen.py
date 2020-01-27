import os

'''.TestConfig {
    .item {
        id 0 : string
        count 1 : integer
    }
    id 0 : integer
}'''

'''sprotoStruct = {
    title,
    structs: {
        name: {
            name,
            type
        }
    }
    childs: {
        name: {
            name,
            type
        }
    }
}'''

class Sproto:
    def __init__(self):
        self.title = ''
        self.structs = {}
        self.childs = {}
        
    def parseTitle(self, title):
        return "." + title + " {"
        
    #integer string bool boolean number
    def parseItem(self, name, index, type):
        if "number" in type:
            type = "integer"
        elif type == "bool":
            type = "boolean"
        return name + " " + str(index) + " : " + type
        
    def parseItems(self, childs, dep):
        tmp = ""
        index = 0
        for k, v in childs.items():
            if k == "index":
                continue
            tmp += dep + self.parseItem(v['name'], index, v['type'])
            tmp += "\n"
            index += 1
        return tmp
        
    def parseSproto(self):
        spTmp = ""
        spTmp = self.parseTitle(self.title)
        spTmp += "\n"
        #子结构
        cs = self.structs
        for ck, cv in cs.items():
            spTmp += "\t" + self.parseTitle(ck)
            spTmp += "\n"
            spTmp += self.parseItems(cv, "\t\t")
            spTmp += "\t}\n"
        #子项
        spTmp += self.parseItems(self.childs, "\t")
        spTmp += "}\n"
        return spTmp
        
'''def parseTitle(title):
    return "." + title + " {"
    
def parseItem(name, index, type):
    if "number" in type:
        type = "integer"
    elif type == "bool":
        type = "boolean"
    return name + " " + str(index) + " : " + type
    
def parseItems(childs, dep):
    tmp = ""
    index = 0
    for k, v in childs.items():
        if k == "index":
            continue
        tmp += dep + parseItem(v['name'], index, v['type'])
        tmp += "\n"
        index += 1
    return tmp
    
def parseSproto(sproto):
    spTmp = ""
    spTmp = parseTitle(sproto.title)
    spTmp += "\n"
    #子结构
    cs = sproto.structs
    for ck, cv in cs.items():
        spTmp += "\t" + parseTitle(ck)
        spTmp += "\n"
        spTmp += parseItems(cv, "\t\t")
        spTmp += "\t}\n"
    #子项
    spTmp += parseItems(sproto.childs, "\t")
    spTmp += "}\n"
    return spTmp'''

if __name__ == '__main__':
    try:
        '''spT = {
            'title': "test",
            'structs': {
                'item': {
                    'id': {
                        'name': 'id',
                        'type': 'string'
                    },
                    'count': {
                        'name': 'count',
                        'type': 'integer'
                    }
                },
                'day': {
                    'dayStr': {
                        'name': 'dayStr',
                        'type': 'string'
                    },
                    'dayNum': {
                        'name': 'dayNum',
                        'type': 'integer'
                    }
                },
            },
            'childs': {
                'id': {
                    'name': 'id',
                    'type': 'string'
                },
                'count': {
                    'name': 'count',
                    'type': 'integer'
                }
            }
        }
        t = parseSproto(spT)
        print(t)'''
        print("try")
    except:
        print("except")
        os.system("pause")
