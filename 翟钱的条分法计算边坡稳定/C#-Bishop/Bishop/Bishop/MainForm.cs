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
            //OpenFileDialog ofd = new OpenFileDialog();//首先根据打开文件对话框，选择excel表格
            //ofd.Filter = "表格|*.csv";//打开文件对话框筛选器
            string strPath;//文件完整的路径名
            if (true) //ofd.ShowDialog() == DialogResult.OK
            {
                try
                {
             //       strPath = ofd.FileName;
             //       //string strCon = "provider=microsoft.jet.oledb.4.0;data source=" + strPath + ";extended properties=excel 12.0;HDR=YE";//关键是红色区域
             //       string strCon = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source="+ strPath + ";Extended Properties=\"text;HDR=Yes;FMT=Delimited\"";
             //       OleDbConnection Con = new OleDbConnection(strCon);//建立连接
             //       //string strSql = "select * from [Sheet1$]";//表名的写法也应注意不同，对应的excel表为sheet1，在这里要在其后加美元符号$，并用中括号
             //       string csvFileName = "1.csv";
             //       string strSql = "SELECT * FROM [" + csvFileName + "]";
             //       OleDbCommand Cmd = new OleDbCommand(strSql, Con);//建立要执行的命令
             //       OleDbDataAdapter da = new OleDbDataAdapter(Cmd);//建立数据适配器
             //       DataSet ds = new DataSet();//新建数据集
             //       da.Fill(ds, "shyman");//把数据适配器中的数据读到数据集中的一个表中（此处表名为shyman，可以任取表名）
             //       //指定datagridview1的数据源为数据集ds的第一张表（也就是shyman表），也可以写ds.Table["shyman"]

　　　　　　　      //dataGridView1.DataSource = ds.Tables[0];
                    
                    //strPath = ofd.FileName;
                    strPath = "D:\\Coding\\Github\\Little-ExE\\翟钱的条分法计算边坡稳定\\C#-Bishop\\";
                    string cnstring = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + strPath + ";Extended Properties=\"text;HDR=Yes;FMT=Delimited\";";
                    string file =  "1234.csv";
                    OleDbConnection cn = new OleDbConnection(cnstring);
                    string aSQL = "select * from [" + file + "]";
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
    }
}
