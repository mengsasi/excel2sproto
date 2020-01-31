using System.IO;
using XLua;

namespace Game {

    public class LuaLoader {

        public static string RootPath = "";

        public static void InitLoader( LuaEnv luaState ) {
            luaState.AddLoader( LuaFileLoader );
        }

        private static byte[] LuaFileLoader( ref string fileName ) {
            string fullName = Path.Combine( RootPath, GetFullName( fileName ) );
            return Core.FileUtils.LoadBytes( fullName );
        }

        private static string GetFullName( string fileName ) {
            fileName = fileName.Replace( '.', '/' );
            return string.Format( "{0}{1}", fileName, fileName.EndsWith( ".lua" ) ? "" : ".lua" );
        }

    }

}
