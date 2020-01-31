using UnityEngine;
using XLua;

namespace Game {

    public class LuaMgr {

        private static LuaMgr instance;
        public static LuaMgr Instance {
            get { return instance ?? ( instance = new LuaMgr() ); }
        }

        public LuaEnv LuaState { get; private set; }

        public void Init() {
            LuaState = new LuaEnv();
            LuaLoader.InitLoader( LuaState );
            LuaLibrary.InitLibrary( LuaState );
        }

        public void SetEnv( string path ) {
            LuaLoader.RootPath = path;
        }

        public void Exit() {
            LuaState.Dispose();
            LuaState = null;
        }

        public T Get<T>( string key ) {
            return LuaState.Global.Get<T>( key );
        }

        public T LoadString<T>( string chunk, string chunkName = "chunk", LuaTable env = null ) {
            return LuaState.LoadString<T>( chunk, chunkName, env );
        }

        public object[] DoString( string chunk, string chunkName = "chunk", LuaTable env = null ) {
            return LuaState.DoString( chunk, chunkName, env );
        }

        public object[] DoFile( string filename ) {
            string file = "require \"" + filename + "\"";
            return DoString( file );
        }

    }

}
