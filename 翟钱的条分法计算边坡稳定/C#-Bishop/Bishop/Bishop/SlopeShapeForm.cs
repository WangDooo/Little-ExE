using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Bishop {
    public partial class SlopeShapeForm : Form {
        public SlopeShapeForm() {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e) {
            this.Close();
        }

        private void button1_Click(object sender, EventArgs e) {
            try {
                Setting.ShareClass.Ax = System.Convert.ToDouble(txtAx.Text);
                Setting.ShareClass.Ay = System.Convert.ToDouble(txtAy.Text);
                Setting.ShareClass.Bx = System.Convert.ToDouble(txtBx.Text);
                Setting.ShareClass.By = System.Convert.ToDouble(txtBy.Text);
                Setting.ShareClass.Cx = System.Convert.ToDouble(txtCx.Text);
                Setting.ShareClass.Cy = System.Convert.ToDouble(txtCy.Text);
                Setting.ShareClass.Dx = System.Convert.ToDouble(txtDx.Text);
                Setting.ShareClass.Dy = System.Convert.ToDouble(txtDy.Text);
                Setting.ShareClass.Ex = System.Convert.ToDouble(txtEx.Text);
                Setting.ShareClass.Ey = System.Convert.ToDouble(txtEy.Text);
                Setting.ShareClass.Fx = System.Convert.ToDouble(txtFx.Text);
                Setting.ShareClass.Fy = System.Convert.ToDouble(txtFy.Text);
                this.Close();
            }
            catch(Exception ex) {
                MessageBox.Show(ex.Message);
            }
            
        }

        private void SlopeShapeForm_Load(object sender, EventArgs e) {
            txtAx.Text = Setting.ShareClass.Ax.ToString();
            txtAy.Text = Setting.ShareClass.Ay.ToString();
            txtBx.Text = Setting.ShareClass.Bx.ToString();
            txtBy.Text = Setting.ShareClass.By.ToString();
            txtCx.Text = Setting.ShareClass.Cx.ToString();
            txtCy.Text = Setting.ShareClass.Cy.ToString();
            txtDx.Text = Setting.ShareClass.Dx.ToString();
            txtDy.Text = Setting.ShareClass.Dy.ToString();
            txtEx.Text = Setting.ShareClass.Ex.ToString();
            txtEy.Text = Setting.ShareClass.Ey.ToString();
            txtFx.Text = Setting.ShareClass.Fx.ToString();
            txtFy.Text = Setting.ShareClass.Fy.ToString();
        }
    }
}
