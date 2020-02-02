using System;
using System.Collections.Generic;
using UnityEngine;

namespace UnityExtension {

    [Serializable]
    public class SPGenSetting {
        public bool Generate = false;
        public string SprotoPath;
        public string CSPath;
        public string Namespace;
    }

    [Serializable, CreateAssetMenu( fileName = "SprotoGen", menuName = "SprotoGen/NewSprotoGen" )]
    public class SprotoGenSettings : ScriptableObject {

        public List<SPGenSetting> Settings = new List<SPGenSetting>();

    }

}
