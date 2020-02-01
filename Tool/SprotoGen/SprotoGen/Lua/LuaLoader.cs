using System.IO;
using XLua;

namespace Game {

    public class LuaLoader {

        public static string LuaSrcPath = "";
        public static string LuaFilePath = "";

        public static void InitLoader( LuaEnv luaState ) {
            luaState.AddLoader( LuaSrcLoader );
            luaState.AddLoader( LuaFileLoader );
        }

        /// <summary>
        /// 加载lua_src,第三方库
        /// </summary>
        /// <param name="fileName"></param>
        /// <returns></returns>
        private static byte[] LuaSrcLoader( ref string fileName ) {
            string src = Path.Combine( LuaSrcPath, "lua_src" );
            string fullName = Path.Combine( src, GetFullName( fileName ) );
            return Core.FileUtils.LoadBytes( fullName );
        }

        /// <summary>
        /// 加载lua
        /// </summary>
        /// <param name="fileName"></param>
        /// <returns></returns>
        private static byte[] LuaFileLoader( ref string fileName ) {
            string fullName = Path.Combine( LuaFilePath, GetFullName( fileName ) );
            return Core.FileUtils.LoadBytes( fullName );
        }

        private static string GetFullName( string fileName ) {
            fileName = fileName.Replace( '.', '/' );
            return string.Format( "{0}{1}", fileName, fileName.EndsWith( ".lua" ) ? "" : ".lua" );
        }

    }

}
