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
        

        public void ConvertPoint(ref int x,ref int y){
            int Height = this.pictureBox1.Height;
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
        private void toolStripButton3_Click(object sender, EventArgs e) {
            int Height = this.pictureBox1.Height;
            int Width = this.pictureBox1.Width;
            //创建位图
            Bitmap bitmap = new Bitmap(Width, Height);
            Graphics g = Graphics.FromImage(bitmap);
            g.Clear(Color.White);
            int x = 0;
            int y = 100;
            ConvertPoint(ref x, ref y );
            g.DrawRectangle(new Pen(Color.Black), x, y, 50, 100);
            this.pictureBox1.Image = bitmap;
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
    }
}
