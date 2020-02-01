using System;
using System.Collections.Generic;

namespace SprotoGen {

    public class OptData {

        public string Opt;

        public string Data;

        public static List<string> OptList;
        public static void InitList() {
            OptList = new List<string> {
                _3rd,
                _p,
                _s,
                _f
            };
        }

        public static readonly string _3rd = "-3rd";    // xx/lua_src 第三方库
        public static readonly string _p = "-p";        // 自定义运行lua脚本路径
        public static readonly string _s = "-s";        // LuaMgr DoString
        public static readonly string _f = "-f";        // LuaMgr DoFile

    }

    class Params {

        private List<OptData> listOpt;

        public OptData GetOpt( string opt ) {
            return listOpt.Find( item => item.Opt == opt );
        }

        public List<OptData> GetOpts() {
            return listOpt;
        }

        public Params( string[] args ) {
            OptData.InitList();
            if( args.Length % 2 == 0 ) {
                ParseArgs( args );
            }
            else {
                Console.WriteLine( "参数错误" );
            }
        }

        private void ParseArgs( string[] args ) {
            listOpt = new List<OptData>();
            for( int i = 0; i < args.Length; i += 2 ) {
                string opt = args[i];
                string data = args[i + 1];
                if( OptData.OptList.Contains( opt ) ) {
                    listOpt.Add( new OptData() {
                        Opt = opt,
                        Data = data
                    } );
                }
                else {
                    listOpt.Clear();
                    Console.WriteLine( "命令错误" );
                    break;
                }
            }
        }

    }

}
