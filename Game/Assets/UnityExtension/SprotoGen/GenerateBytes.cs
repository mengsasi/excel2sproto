using Game;
using System;
using UnityEditor;
using UnityEngine;

namespace UnityExtension {

    public class SprotoGen {

        private static void Do( Action callback ) {
            LuaMgr.Instance.Init( null );
            LuaMgr.Instance.LuaState.AddLoader( LuaLoader.LuaEditorLoader );
            callback();
            LuaMgr.Instance.Exit();
        }

        [MenuItem( "XLua/Generate Bytes" )]
        public static void GenerateBytes() {
            Do( () => {
                try {
                    LuaMgr.Instance.DoFile( "LuaGen/AllGen" );
                    Debug.Log( "generate bytes finish" );
                }
                catch( Exception e ) {
                    Debug.Log( e.ToString() );
                }
            } );
            AssetDatabase.Refresh();
        }

    }

}
