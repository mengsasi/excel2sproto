using System.IO;
using XLua;

namespace Game {

    public class LuaLoader {

        public static void InitLoader( LuaEnv luaState ) {
            luaState.AddLoader( XLuaLoader );
            luaState.AddLoader( LuaFileLoader );
        }

        private static byte[] XLuaLoader( ref string fileName ) {
            string fullName = LuaConst.XLuaDir + GetFullName( fileName );
            return LoadBytes( fullName );
        }

        private static byte[] LuaFileLoader( ref string fileName ) {
            string fullName = LuaConst.LuaDir + GetFullName( fileName );
            return LoadBytes( fullName );
        }

#if UNITY_EDITOR
        public static byte[] LuaEditorLoader( ref string fileName ) {
            string fullName = LuaConst.LuaEditorDir + GetFullName( fileName );
            return LoadBytes( fullName );
        }

        public static byte[] LuaEditorSPDLoader( ref string fileName ) {
            string fullName = LuaConst.LuaEditorDir + "sprotodump/" + GetFullName( fileName );
            return LoadBytes( fullName );
        }
#endif

        private static string GetFullName( string fileName ) {
            fileName = fileName.Replace( '.', '/' );
            return string.Format( "{0}{1}", fileName, fileName.EndsWith( ".lua" ) ? "" : ".lua" );
        }

        private static byte[] LoadBytes( string filePath ) {
            byte[] bytes = Core.FileUtils.LoadBytes( filePath );
            return bytes;
        }

    }

}
