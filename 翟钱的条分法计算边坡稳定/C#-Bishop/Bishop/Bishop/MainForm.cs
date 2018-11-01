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

        private void button1_Click(object sender, EventArgs e) {
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

        private void MainForm_Load(object sender, EventArgs e) {
            this.dataGridView1.Width = this.splitContainer1.Panel1.Width;
        }

        private void timer1_Tick(object sender, EventArgs e) {
            toolStripStatusLabel1.Text = DateTime.Now.ToShortDateString();
            toolStripStatusLabel2.Text = DateTime.Now.ToLongTimeString();
        }

        private void 边坡形状ToolStripMenuItem_Click(object sender, EventArgs e) {
            SlopeShapeForm slopeShapeForm = new SlopeShapeForm();
            slopeShapeForm.ShowDialog();
        }

        private void button2_Click(object sender, EventArgs e) {
            int index = this.dataGridView1.Rows.Add();
            this.dataGridView1.Rows[index].Cells[0].Value = Setting.ShareClass.Ax;
            this.dataGridView1.Rows[index].Cells[1].Value = Setting.ShareClass.Ay;
            this.dataGridView1.Rows[index].Cells[2].Value = "123RR ";
            this.dataGridView1.Rows[index].Cells[3].Value = "123RR ";

        }

        private void button3_Click(object sender, EventArgs e) {
            int Height = this.pictureBox1.Height;
            int Width = this.pictureBox1.Width;
            MessageBox.Show(Height.ToString());
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), 0, Height-100, 50, 100);
            Pen mypen2 = new Pen(Color.Red, 12);
            Pen mypen3 = new Pen(Color.Yellow,111);
        }
    }
}
