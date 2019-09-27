using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;


namespace snap {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
        }
        public static string strPath  = "D:\\"; //文件夹完整的路径名
        public static int x1 = 0 ;
        public static int y1 = 0;
        public static int x2 = Screen.PrimaryScreen.Bounds.Width;
        public static int y2 = Screen.PrimaryScreen.Bounds.Height;
        public static int s_width;
        public static int s_height;
        public static double interval;
        public static int interval_int;


        private void Auto_snap() {
            try {
                x1 = int.Parse(txt_x1.Text);
                y1 = int.Parse(txt_y1.Text);
                x2 = int.Parse(txt_x2.Text);
                y2 = int.Parse(txt_y2.Text);
            }
            catch (Exception ex) {
                MessageBox.Show(ex.Message);
            }
            s_width = x2 - x1;
            s_height = y2 - y1;
            Snap(x1, y1, s_width, s_height);
        }
        

        public static void Snap(int x, int y, int width, int height){
            try{
                GC.Collect();
                Image image = new Bitmap(width, height);
                Graphics g = Graphics.FromImage(image);
                g.CopyFromScreen(x, y, 0, 0, new System.Drawing.Size(width, height));
                string hour = DateTime.Now.Hour.ToString();
                string minute = DateTime.Now.Minute.ToString();
                string second = DateTime.Now.Second.ToString();
                image.Save(strPath + hour + "-" + minute+"-"+second + ".jpg");

                //Bitmap image = new Bitmap(width,height);
                //using (Graphics g = Graphics.FromImage(image))
                //{
                //    g.CopyFromScreen(0, 0, 0, 0, image.Size);
                //    g.Dispose();
                //    string hour = DateTime.Now.Hour.ToString();
                //    string minute = DateTime.Now.Minute.ToString();
                //    string second = DateTime.Now.Second.ToString();
                //    image.Save(strPath + hour + "-" + minute+"-"+second + ".jpg");
                //}
            }
            catch (Exception ex) {
                    MessageBox.Show(ex.Message);
            }
        }

        private void timer1_Tick(object sender, EventArgs e) {
             lbl_x.Text = Control.MousePosition.X.ToString();
             lbl_y.Text = Control.MousePosition.Y.ToString();
        }

        private void timer2_Tick(object sender, EventArgs e) {
            Auto_snap();
        }

        private void button2_Click(object sender, EventArgs e) {
            FolderBrowserDialog dialog = new FolderBrowserDialog();
            dialog.Description = "请选择文件存放路径";
            if (dialog.ShowDialog() == DialogResult.OK) {
                try {
                    strPath = dialog.SelectedPath+"\\";
                } catch (Exception ex) {
                    MessageBox.Show(ex.Message);
                }
            }
        }
        
        private void button1_Click(object sender, EventArgs e) {
            try {
                interval = Convert.ToDouble(txt_interval.Text);
                interval_int = Convert.ToInt32(interval*1000);
                this.timer2.Enabled = true;
                this.timer2.Interval = interval_int;
                toolStripStatusLabel1.Text = "胡博正在努力采集中...";
            }
            catch (Exception ex) {
                 MessageBox.Show(ex.Message);
            }
            
        }

        private void button3_Click(object sender, EventArgs e) {
            this.timer2.Enabled = false;
            toolStripStatusLabel1.Text = "让胡博休息一会，采集已停止.";
        }
    }

}
