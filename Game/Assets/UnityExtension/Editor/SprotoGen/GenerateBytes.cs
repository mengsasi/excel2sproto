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

        [MenuItem( "XLua/Generate CS" )]
        public static void GenerateCS() {
            Do( () => {
                string c2s = Application.dataPath + "/Res/Configs/Sproto/c2s.sproto";
                string s2c = Application.dataPath + "/Res/Configs/Sproto/s2c.sproto";
                string c2s_cs = Application.dataPath + "/Scripts/Core/Sproto/c2s.cs";
                string s2c_cs = Application.dataPath + "/Scripts/Core/Sproto/s2c.cs";
                LuaMgr.Instance.DoFile( "sprotodump" );
                LuaFunction dump = LuaMgr.Instance.Get<LuaFunction>( "Dump" );
                dump.Call( "-cs", c2s, "-o", c2s_cs, "-p", "C2S", "-namespace" );
                dump.Call( "-cs", s2c, "-o", s2c_cs, "-p", "S2C", "-namespace" );
                Debug.Log( "generate cs finish" );
            } );
            AssetDatabase.Refresh();
        }

    }

}
