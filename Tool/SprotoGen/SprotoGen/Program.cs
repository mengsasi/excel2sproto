using Game;
using System;
using System.IO;
using XLua;

namespace SprotoGen {

    class Program {

        static void Main( string[] args ) {
            string curDir = Environment.CurrentDirectory;
            try {
                LuaMgr.Instance.Init();
                LuaMgr.Instance.SetEnv( Path.Combine( curDir, "lua_src" ) );
                if( args.Length > 1 ) {
                    if( args[0] == "-s" ) {
                        LuaMgr.Instance.DoString( args[1] );
                    }
                    else if( args[0] == "-f" ) {
                        LuaMgr.Instance.DoFile( args[1] );
                    }
                }
                else {
                    LuaMgr.Instance.DoFile( "main" );
                    var func = LuaMgr.Instance.Get<LuaFunction>( "Main" );
                    func.Call( args );
                }
            }
            catch( Exception e ) {
                Console.WriteLine( e.ToString() );
                Console.ReadKey();
            }
        }

    }
}
