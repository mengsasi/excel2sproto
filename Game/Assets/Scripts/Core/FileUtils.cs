using System.IO;
using UnityEngine;

namespace Core {

    public class FileUtils {

        public static void MakeDir( string path ) {
            string dir = path;
            if( path.Contains( "." ) ) {
                dir = Path.GetDirectoryName( path );
            }
            if( !Directory.Exists( dir ) ) {
                Directory.CreateDirectory( dir );
            }
        }

        public static bool Exists( string path ) {
            return File.Exists( path );
        }

        public static void WriteAllBytes( string path, byte[] content ) {
            File.WriteAllBytes( path, content );
        }

        public static byte[] ReadAllBytes( string path ) {
            bool hasFile = Exists( path );
            if( !hasFile ) {
                Debug.LogWarning( "FileNotExist!!!!!" + path );
                return null;
            }
            return File.ReadAllBytes( path );
        }

        public static void Save( string path, string content, FileMode mode = FileMode.OpenOrCreate ) {
            var filemode = mode;
            bool hasFile = Exists( path );

            if( mode == FileMode.OpenOrCreate ) {
                if( hasFile ) {
                    filemode = FileMode.Truncate;
                }
            }
            else {
                if( hasFile == false )
                    filemode = FileMode.OpenOrCreate;
            }
            using( var fs = new FileStream( path, filemode, FileAccess.Write ) ) {
                using( var sw = new StreamWriter( fs ) ) {
                    sw.Write( content );
                }
            }
        }

        public static string Load( string path ) {
            bool hasFile = Exists( path );
            if( !hasFile ) {
                Debug.LogWarning( "FileNotExist!!!!!" + path );
                return "";
            }
            string content;
            using( var fs = new FileStream( path, FileMode.Open, FileAccess.Read ) ) {
                using( var sr = new StreamReader( fs ) ) {
                    content = sr.ReadToEnd();
                }
            }
            return content;
        }

        public static void SaveBytes( string path, byte[] content ) {
            FileMode mode = FileMode.OpenOrCreate;
            bool hasFile = Exists( path );
            if( hasFile ) {
                mode = FileMode.Truncate;
            }
            using( var fs = new FileStream( path, mode, FileAccess.ReadWrite ) ) {
                fs.Write( content, 0, content.Length );
            }
        }

        public static byte[] LoadBytes( string path ) {
            bool hasFile = Exists( path );
            if( !hasFile ) {
                //Debug.LogWarning( "FileNotExist!!!!!" + path );
                return null;
            }
            byte[] content = null;
            using( var fs = new FileStream( path, FileMode.Open, FileAccess.Read ) ) {
                content = new byte[fs.Length];
                fs.Read( content, 0, content.Length );
            }
            return content;
        }

    }

}
