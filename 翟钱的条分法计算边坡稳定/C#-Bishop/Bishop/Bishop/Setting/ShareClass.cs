using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bishop.Setting {
    class ShareClass {
        // 记录各点坐标
        private static float _Ax = 0;
        public static float Ax {
            get { return ShareClass._Ax; }
            set { ShareClass._Ax = value; }
        }
        private static float _Ay = 0;
        public static float Ay {
            get { return ShareClass._Ay; }
            set { ShareClass._Ay = value; }
        }
        private static float _Bx = 0;
        public static float Bx {
            get { return ShareClass._Bx; }
            set { ShareClass._Bx = value; }
        }
        private static float _By = 15;
        public static float By {
            get { return ShareClass._By; }
            set { ShareClass._By = value; }
        }
        private static float _Cx = 15;
        public static float Cx {
            get { return ShareClass._Cx; }
            set { ShareClass._Cx = value; }
        }
        private static float _Cy = 15;
        public static float Cy {
            get { return ShareClass._Cy; }
            set { ShareClass._Cy = value; }
        }
        private static float _Dx = 20;
        public static float Dx {
            get { return ShareClass._Dx; }
            set { ShareClass._Dx = value; }
        }
        private static float _Dy = 10;
        public static float Dy {
            get { return ShareClass._Dy; }
            set { ShareClass._Dy = value; }
        }
        private static float _Ex = 35;
        public static float Ex {
            get { return ShareClass._Ex; }
            set { ShareClass._Ex = value; }
        }
        private static float _Ey = 10;
        public static float Ey {
            get { return ShareClass._Ey; }
            set { ShareClass._Ey = value; }
        }
        private static float _Fx = 35;
        public static float Fx {
            get { return ShareClass._Fx; }
            set { ShareClass._Fx = value; }
        }
        private static float _Fy = 0;
        public static float Fy {
            get { return ShareClass._Fy; }
            set { ShareClass._Fy = value; }
        }
        // 记录土体参数
        private static float _EffectiveC = 5;
        public static float EffectiveC {
            get { return ShareClass._EffectiveC; }
            set { ShareClass._EffectiveC = value; }
        }
        private static float _EffectivePhi = 30;
        public static float EffectivePhi {
            get { return ShareClass._EffectivePhi; }
            set { ShareClass._EffectivePhi = value; }
        }
        private static float _Gamma = 20;
        public static float Gamma {
            get { return ShareClass._Gamma; }
            set { ShareClass._Gamma = value; }
        }
        // 记录网格布种信息

    }
}
