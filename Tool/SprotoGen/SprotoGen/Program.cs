using Game;
using System;
using XLua;

namespace SprotoGen {

    class Program {

        static void Main( string[] args ) {
            string curDir = Environment.CurrentDirectory;
            try {
                LuaMgr.Instance.Init();
                //默认当前环境
                LuaLoader.LuaSrcPath = curDir;
                LuaLoader.LuaFilePath = curDir;
                Params param = new Params( args );
                var _3rd = param.GetOpt( OptData._3rd );
                if( _3rd != null ) {
                    LuaLoader.LuaSrcPath = _3rd.Data;
                }
                var _p = param.GetOpt( OptData._p );
                if( _p != null ) {
                    LuaLoader.LuaFilePath = _p.Data;
                }
                bool def = true;//默认执行main
                var _s = param.GetOpt( OptData._s );
                if( _s != null ) {
                    def = false;
                    LuaMgr.Instance.DoString( _s.Data );
                }
                var _f = param.GetOpt( OptData._f );
                if( _f != null ) {
                    def = false;
                    LuaMgr.Instance.DoFile( _f.Data );
                }
                if( def ) {
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
