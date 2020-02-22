# excel2sproto
excel配置数据，使用sproto读取

## sproto类型

> * integer
> * string
> * boolean

## 配置
可配置integer，string，boolean(bool)，JSON(json)，numberXX
数组，结构体，结构体数组，参考测试配置

### 配置浮点数类型
numberXX</br>
10.2</br>
类型写成number10</br>
数据直接填10.2</br>

存到bytes中的数据是10.2x10</br>
取数据时，需要自己手动/10</br>
如果可以，尝试把这个操作写到取数据的底层，done</br>
已经写到底层</br>

### 使用方法
#### 路径设置
setting.py
#### 当excel表结构修改时，执行export-sp.bat</br>
生成新的.sproto文件以及用于生成bytes的luaGen脚本和读取bytes的lua脚本</br>
</br>

#### 当只是数值变动时，执行export-data.bat</br>
或者打开Unity项目，点击菜单栏中的XLua/GenerateBytes</br>
生成新的bytes</br>
</br>

#### 如果只想生成某一个excel的sproto和数据bytes</br>
参考0-4测试配置表xxx.bat</br>
</br>

### 公共结构体 gloablStruct.py
不弄公共的结构体了，每个sproto单独处理</br>
如果想把sproto拼接成一个文件，然后一个sproto.parse("")</br>
这时候可以弄公共结构体</br>

### excel2Lua.py</br>
此文件是生成.. 用于读取bytes的脚本</br>
只是示例，需根据项目自定义</br>
</br>


## SprotoGen.exe
原本使用Unity中的lua环境，Unity中点击菜单按钮生成bytes</br>
我把它拿出来了，写了SprotoGen工程，原本Unity中生成方法也保留了</br>
使用SprotoGen的lua环境，执行lua脚本，生成bytes</br>
</br>
分x86，x64</br>
TODO x86报错??</br>

### LuaEnv注释
AddSearcher(StaticLuaCallbacks.LoadFromResource, 4);</br>
AddSearcher(StaticLuaCallbacks.LoadFromStreamingAssetsPath, -1);</br>
translator.Alias(typeof(Type), "System.MonoType");</br>
StaticLuaCallbacks Print UnityEngine.Debug.Log("LUA: " + s);</br>
</br>

### SprotoGen使用
start SprotoGen.exe -3rd <!path> -p <!path> -s <!string></br>

> * -3rd lua中使用的第三方库路径（lua_src父目录）
> * -p lua文件路径
> * -s 执行DoString
> * -f 执行DoFile
> * 默认执行 exe目录下的main.lua的Main(...)方法
