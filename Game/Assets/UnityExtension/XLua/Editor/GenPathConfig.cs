using UnityEngine;
using CSObjectWrapEditor;

//配置的详细介绍请看Doc下《XLua的配置.doc》
public static class GenPathConfig {
    [GenPath]//代码生成路径
    public static string GenPath = Application.dataPath + "/UnityExtension/XLua/Gen/";
}
