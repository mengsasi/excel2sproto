# excel2sproto
excel配置数据，使用sproto读取

## sproto类型

> * integer
> * string
> * boolean

### 配置浮点数类型
10.2</br>
类型写成number10</br>
数据直接填10.2</br>

存到bytes中的数据是10.2x10</br>
取数据时，需要自己手动/10</br>
如果可以，尝试把这个操作写到取数据的底层</br>

### 公共结构体 gloablStruct.py
不弄公共的结构体了，每个sproto单独处理</br>
如果想把sproto拼接成一个文件，然后一个sproto.parse("")</br>
这时候可以弄公共结构体</br>

### excel2Lua.py</br>
此文件是生成.. 用于读取bytes的脚本</br>
只是示例，需根据项目自定义</br>
</br>

------
### TODO</br>
C#的生成部分</br>
