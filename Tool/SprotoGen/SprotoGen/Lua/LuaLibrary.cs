using System;
using System.Runtime.InteropServices;
using UnityEngine;
using XLua;

#if USE_UNI_LUA
using LuaAPI = UniLua.Lua;
using RealStatePtr = UniLua.ILuaState;
using LuaCSFunction = UniLua.CSharpFunctionDelegate;
#else
using LuaAPI = XLua.LuaDLL.Lua;
using RealStatePtr = System.IntPtr;
using LuaCSFunction = XLua.LuaDLL.lua_CSFunction;
#endif

namespace XLua {

    public partial class StaticLuaCallbacks {

        [MonoPInvokeCallback( typeof( LuaCSFunction ) )]
        public static int LoadLpeg( RealStatePtr L ) {
            return LuaAPI.luaopen_lpeg( L );
        }

        [MonoPInvokeCallback( typeof( LuaCSFunction ) )]
        public static int LoadSprotoCore( RealStatePtr L ) {
            return LuaAPI.luaopen_sproto_core( L );
        }

        [MonoPInvokeCallback( typeof( LuaCSFunction ) )]
        public static int LoadCJson( RealStatePtr L ) {
            return LuaAPI.luaopen_cjson( L );
        }

    }

}

namespace XLua.LuaDLL {

    public partial class Lua {

        //lpeg
        [DllImport( LUADLL, CallingConvention = CallingConvention.Cdecl )]
        public static extern int luaopen_lpeg( IntPtr luaState );

        //sproto
        [DllImport( LUADLL, CallingConvention = CallingConvention.Cdecl )]
        public static extern int luaopen_sproto_core( IntPtr luaState );

        //lua-cjson
        [DllImport( LUADLL, CallingConvention = CallingConvention.Cdecl )]
        public static extern int luaopen_cjson( IntPtr luaState );

    }

}

namespace Game {

    public static class LuaLibrary {

        public static void InitLibrary( LuaEnv luaState ) {
            luaState.AddBuildin( "lpeg", StaticLuaCallbacks.LoadLpeg );
            luaState.AddBuildin( "sproto.core", StaticLuaCallbacks.LoadSprotoCore );
            luaState.AddBuildin( "cjson", StaticLuaCallbacks.LoadCJson );
        }

    }

}
