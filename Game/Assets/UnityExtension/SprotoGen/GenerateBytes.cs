using Game;
using System;
using UnityEditor;

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
                LuaMgr.Instance.DoFile( "LuaGen/AllGen" );
            } );
        }

    }

}
