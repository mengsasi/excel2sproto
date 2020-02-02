using Game;
using System;
using UnityEditor;
using UnityEngine;
using XLua;

namespace UnityExtension {

    public class SprotoGen {

        private static void Do( Action callback ) {
            LuaMgr.Instance.Init( null );
            LuaMgr.Instance.LuaState.AddLoader( LuaLoader.LuaEditorLoader );
            LuaMgr.Instance.LuaState.AddLoader( LuaLoader.LuaEditorSPDLoader );
            try {
                callback();
            }
            catch( Exception e ) {
                Debug.Log( e.ToString() );
            }
            LuaMgr.Instance.Exit();
            AssetDatabase.Refresh();
        }

        [MenuItem( "XLua/Generate Bytes" )]
        public static void GenerateBytes() {
            Do( () => {
                LuaMgr.Instance.DoFile( "LuaGen/AllGen" );
                Debug.Log( "generate bytes finish" );
            } );
        }

        public static string SettingPath = "Assets/UnityExtension/Editor/SprotoGen/SprotoGen.asset";

        [MenuItem( "XLua/Generate CS" )]
        public static void GenerateCS() {
            Do( () => {
                LuaMgr.Instance.DoFile( "sprotodump" );
                LuaFunction dump = LuaMgr.Instance.Get<LuaFunction>( "Dump" );
                SprotoGenSettings settings = AssetDatabase.LoadAssetAtPath<SprotoGenSettings>( SettingPath );
                var list = settings.Settings;
                for( int i = 0; i < list.Count; i++ ) {
                    var item = list[i];
                    if( item.Generate ) {
                        string sp_path = Application.dataPath + item.SprotoPath;
                        string cs_path = Application.dataPath + item.CSPath;
                        if( !string.IsNullOrEmpty( item.Namespace ) ) {
                            dump.Call( "-cs", sp_path,
                                "-o", cs_path,
                                "-p", item.Namespace,
                                "-namespace" );
                        }
                        else {
                            dump.Call( "-cs", sp_path,
                                "-o", cs_path,
                                "-namespace" );
                        }
                    }
                }
                //string structure = Application.dataPath + "/Res/Configs/Sproto/structure.sproto";
                //string structure_cs = Application.dataPath + "/Scripts/Core/Sproto/structure.cs";
                //dump.Call( "-cs", structure, "-o", structure_cs, "-namespace" );
                Debug.Log( "generate cs finish" );
            } );
            AssetDatabase.Refresh();
        }

        //[MenuItem( "XLua/Generate Net CS" )]
        //public static void GenerateNetCS() {
        //    Do( () => {
        //        string c2s = Application.dataPath + "/Res/Configs/Sproto/c2s.sproto";
        //        string s2c = Application.dataPath + "/Res/Configs/Sproto/s2c.sproto";
        //        string c2s_cs = Application.dataPath + "/Scripts/Core/Sproto/c2s.cs";
        //        string s2c_cs = Application.dataPath + "/Scripts/Core/Sproto/s2c.cs";
        //        LuaMgr.Instance.DoFile( "sprotodump" );
        //        LuaFunction dump = LuaMgr.Instance.Get<LuaFunction>( "Dump" );
        //        dump.Call( "-cs", c2s, "-o", c2s_cs, "-p", "C2S", "-namespace" );
        //        dump.Call( "-cs", s2c, "-o", s2c_cs, "-p", "S2C", "-namespace" );
        //        Debug.Log( "generate cs finish" );
        //    } );
        //    AssetDatabase.Refresh();
        //}

    }

}
