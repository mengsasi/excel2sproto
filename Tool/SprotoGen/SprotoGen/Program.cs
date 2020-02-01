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
                if( args.Length == 4 ) {
                    if( args[0] == "-d" ) {
                        LuaMgr.Instance.SetEnv( Path.Combine( args[1], "lua_src" ) );
                    }
                    if( args[2] == "-s" ) {
                        LuaMgr.Instance.DoString( args[3] );
                    }
                    else if( args[2] == "-f" ) {
                        LuaMgr.Instance.DoFile( args[3] );
                    }
                }
                else {
                    LuaMgr.Instance.SetEnv( Path.Combine( curDir, "lua_src" ) );
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
