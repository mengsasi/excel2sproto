using UnityEngine;

namespace Game {

    public class BaseMgr<T> where T : class, new() {

        private static T instance = null;
        public static T Instance {
            get { return instance ?? ( instance = new T() ); }
        }

        protected GameObject Owner;

        public virtual void Init( GameObject owner ) {
            Owner = owner;
        }

        public virtual void Update() {

        }

        public virtual void LateUpdate() {

        }

        public virtual void FixedUpdate() {

        }

        public virtual void Exit() {
            Owner = null;
        }

    }

}
