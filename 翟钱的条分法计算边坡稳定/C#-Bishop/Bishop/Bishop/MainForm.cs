using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.OleDb;

namespace Bishop {
    public partial class MainForm : Form {
        public MainForm() {
            InitializeComponent();
        }

        private void splitContainer1_SplitterMoved(object sender, SplitterEventArgs e) {
            this.dataGridView1.Width = this.splitContainer1.Panel1.Width;
        }

        private void MainForm_Load(object sender, EventArgs e) {
            this.dataGridView1.Width = this.splitContainer1.Panel1.Width;
            this.MouseWheel += PictureBox1_MouseWheel; 
        }

        void PictureBox1_MouseWheel(object sender, MouseEventArgs e){ //判断上滑还是下滑
            if (e.Delta < 0){ //计算缩放大小
                this.pictureBox1.Width = this.pictureBox1.Width * 9 / 10;
                this.pictureBox1.Height = this.pictureBox1.Height * 9 / 10;
            }else{
                this.pictureBox1.Width = this.pictureBox1.Width * 11 / 10;
                this.pictureBox1.Height = this.pictureBox1.Height * 11 / 10;
            }//设置图片在窗体居中
            
        }

        int xPos;
        int yPos;
        bool MoveFlag;
        


        private void timer1_Tick(object sender, EventArgs e) {
            toolStripStatusLabel1.Text = DateTime.Now.ToShortDateString();
            toolStripStatusLabel2.Text = DateTime.Now.ToLongTimeString();
        }

        private void 边坡形状ToolStripMenuItem_Click(object sender, EventArgs e) {
            SlopeShapeForm slopeShapeForm = new SlopeShapeForm();
            slopeShapeForm.ShowDialog();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e) {
            //鼠标已经抬起
            MoveFlag = false;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e) {
            //只在鼠标按下时绘制移动
            if (MoveFlag){
                pictureBox1.Left += Convert.ToInt16(e.X - xPos);//设置x坐标.
                pictureBox1.Top += Convert.ToInt16(e.Y - yPos);//设置y坐标.
            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e) {
            this.pictureBox1.Focus();
            MoveFlag = true;//已经按下.
            xPos = e.X;//当前x坐标.
            yPos = e.Y;//当前y坐标.
        }
        

        public void ConvertPoint(ref float x,ref float y){
            float Height = this.pictureBox1.Height;
            x = x + 10; // 10与边界的距离
            y = Height - y - 10;
        }
        
        // 读取csv
        private void toolStripButton1_Click(object sender, EventArgs e) {
            OpenFileDialog ofd = new OpenFileDialog();//首先根据打开文件对话框，选择excel表格
            ofd.Filter = "表格|*.csv";//打开文件对话框筛选器
            string strPath;//文件完整的路径名
            if (ofd.ShowDialog() == DialogResult.OK) 
            {
                try
                {
                    strPath = ofd.FileName.Replace("\\", "\\\\"); 
                    MessageBox.Show(strPath);
                    string filePath = strPath.Substring(0,strPath.LastIndexOf("\\")+1);
                    MessageBox.Show(filePath);
                    //filePath = "D:\\Coding\\Github\\Little-ExE\\翟钱的条分法计算边坡稳定\\C#-Bishop\\";
                    string cnstring = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + filePath + ";Extended Properties=\"text;HDR=Yes;FMT=Delimited\";";
                    string fileName =  strPath.Remove(0,strPath.LastIndexOf("\\") + 1) ;
                    OleDbConnection cn = new OleDbConnection(cnstring);
                    string aSQL = "select * from [" + fileName + "]";
                    cn.Open();
                    OleDbDataAdapter da = new OleDbDataAdapter(aSQL, cn);
                    DataTable dt = new DataTable();
                    da.Fill(dt);
                    cn.Close();
                    dataGridView1.DataSource = dt;
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);//捕捉异常
                }
            }
        }
        // dataGridView显示
        private void toolStripButton2_Click(object sender, EventArgs e) {
            int index = this.dataGridView1.Rows.Add();
            this.dataGridView1.Rows[index].Cells[0].Value = Setting.ShareClass.Ax;
            this.dataGridView1.Rows[index].Cells[1].Value = Setting.ShareClass.Ay;
            this.dataGridView1.Rows[index].Cells[2].Value = "123RR ";
            this.dataGridView1.Rows[index].Cells[3].Value = "123RR ";
        }
        
        // 绘制
        public void DrawSlope() {
            int Height = this.pictureBox1.Height;
            int Width = this.pictureBox1.Width;
            //创建位图
            Bitmap bitmap = new Bitmap(Width, Height);
            Graphics g = Graphics.FromImage(bitmap);
            g.Clear(Color.White);
            Pen mypen = new Pen(Color.Black, 2);
            // 读取各点值
            float LargeRatio = 10;
            float Ax = Setting.ShareClass.Ax * LargeRatio;
            float Ay = Setting.ShareClass.Ay * LargeRatio;
            float Bx = Setting.ShareClass.Bx * LargeRatio;
            float By = Setting.ShareClass.By * LargeRatio;
            float Cx = Setting.ShareClass.Cx * LargeRatio;
            float Cy = Setting.ShareClass.Cy * LargeRatio;
            float Dx = Setting.ShareClass.Dx * LargeRatio;
            float Dy = Setting.ShareClass.Dy * LargeRatio;
            float Ex = Setting.ShareClass.Ex * LargeRatio;
            float Ey = Setting.ShareClass.Ey * LargeRatio;
            float Fx = Setting.ShareClass.Fx * LargeRatio;
            float Fy = Setting.ShareClass.Fy * LargeRatio;
            ConvertPoint(ref Ax, ref Ay );
            ConvertPoint(ref Bx, ref By );
            ConvertPoint(ref Cx, ref Cy );
            ConvertPoint(ref Dx, ref Dy );
            ConvertPoint(ref Ex, ref Ey );
            ConvertPoint(ref Fx, ref Fy );
            g.DrawLine(mypen, Ax, Ay, Bx, By);
            g.DrawLine(mypen, Bx, By, Cx, Cy);
            g.DrawLine(mypen, Cx, Cy, Dx, Dy);
            g.DrawLine(mypen, Dx, Dy, Ex, Ey);
            g.DrawLine(mypen, Ex, Ey, Fx, Fy);
            g.DrawLine(mypen, Fx, Fy, Ax, Ay);
            this.pictureBox1.Image = bitmap;
        }

        private void toolStripButton3_Click(object sender, EventArgs e) {
            DrawSlope();
        }
        // 图片复位
        private void toolStripButton4_Click(object sender, EventArgs e) {
            int y = splitContainer1.Panel2.Top;
            pictureBox1.Width = splitContainer1.Panel2.Width;
            pictureBox1.Height = splitContainer1.Panel2.Height;
            pictureBox1.Location = new Point(0, y);
        }

        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e) {
            this.Close();
        }

        private void 关于ToolStripMenuItem_Click(object sender, EventArgs e) {
            AboutForm aboutForm = new AboutForm();
            aboutForm.ShowDialog();
        }

        private void 土体参数ToolStripMenuItem_Click(object sender, EventArgs e) {
            SoilParameterForm soilParameterForm = new SoilParameterForm();
            soilParameterForm.ShowDialog();
        }

        private void toolStripButton5_Click(object sender, EventArgs e) {
            ComputeBishop();
        }

        public void ComputeBishop() {
            // 分条的宽度
            float slice_width(float point_left,float point_right, int N) {
                float width = Math.Abs(point_right-point_left);
                return width / N;
            }
            // 分条的x坐标 维度是N+1
            float[] slice_x_axis(float point_left, float point_right, int N) {
                float single_width = slice_width(point_left,point_right,N);
                return
            }
        }
    }
}
