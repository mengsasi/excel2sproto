using UnityEngine;
using XLua;

namespace Game {

    public class LuaMgr : BaseMgr<LuaMgr> {

        public LuaEnv LuaState { get; private set; }

        private float timer = 0;
        public float Duration = 1f;

        public override void Init( GameObject owner ) {
            base.Init( owner );
            LuaState = new LuaEnv();
            LuaLoader.InitLoader( LuaState );
            LuaLibrary.InitLibrary( LuaState );
            timer = 0f;
        }

        public override void Update() {
            timer += Time.deltaTime;
            if( timer > Duration ) {
                timer = 0f;
                if( LuaState != null ) {
                    LuaState.Tick();
                }
            }
        }

        public override void LateUpdate() {

        }

        public override void FixedUpdate() {

        }

        public override void Exit() {
            base.Exit();
            LuaState.Dispose();
            LuaState = null;
            timer = 0f;
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

        public LuaTable NewTable() {
            return LuaState.NewTable();
        }

        public void CallLuaFunc( string funcName ) {
            if( LuaState != null ) {
                LuaFunction func = Get<LuaFunction>( funcName );
                if( func != null ) {
                    func.Call();
                }
            }
        }

    }

}
