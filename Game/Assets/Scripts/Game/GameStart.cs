using UnityEngine;

namespace Game {

    public class GameStart : Core.Singleton<GameStart> {

        private GameObject go;

        private void Start() {
            go = gameObject;
            try {
                StartGame();
            }
            catch( System.Exception e ) {
                Debug.Log( e.ToString() );
            }
        }

        public void StartGame() {
            try {
                LuaMgr.Instance.Init( go );
                LuaMgr.Instance.DoFile( "GameStart" );
                LuaMgr.Instance.CallLuaFunc( "StartGame" );
            }
            catch( System.Exception e ) {
                Debug.Log( e.ToString() );
            }
        }

        private void OnApplicationQuit() {
            try {
                LuaMgr.Instance.CallLuaFunc( "StopGame" );
                LuaMgr.Instance.Exit();
            }
            catch( System.Exception e ) {
                Debug.Log( e.ToString() );
            }
        }

    }

}
