namespace snap {
    partial class Form1 {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent() {
            this.components = new System.ComponentModel.Container();
            this.button1 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.txt_interval = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.button2 = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.button3 = new System.Windows.Forms.Button();
            this.txt_x1 = new System.Windows.Forms.TextBox();
            this.txt_x2 = new System.Windows.Forms.TextBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.lbl_x = new System.Windows.Forms.Label();
            this.lbl_y = new System.Windows.Forms.Label();
            this.txt_y1 = new System.Windows.Forms.TextBox();
            this.txt_y2 = new System.Windows.Forms.TextBox();
            this.timer2 = new System.Windows.Forms.Timer(this.components);
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.statusStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(33, 290);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(68, 41);
            this.button1.TabIndex = 0;
            this.button1.Text = "开始采集";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(31, 38);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(71, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "间隔时间(s)";
            // 
            // txt_interval
            // 
            this.txt_interval.Location = new System.Drawing.Point(122, 35);
            this.txt_interval.Name = "txt_interval";
            this.txt_interval.Size = new System.Drawing.Size(83, 21);
            this.txt_interval.TabIndex = 2;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(31, 88);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(89, 12);
            this.label2.TabIndex = 3;
            this.label2.Text = "图片保存的位置";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(126, 80);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(132, 29);
            this.button2.TabIndex = 4;
            this.button2.Text = "设置-默认在D:\\";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(32, 212);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(101, 12);
            this.label3.TabIndex = 5;
            this.label3.Text = "区域左上角的坐标";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(32, 252);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(101, 12);
            this.label4.TabIndex = 6;
            this.label4.Text = "区域右下角的坐标";
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(151, 290);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(74, 41);
            this.button3.TabIndex = 7;
            this.button3.Text = "停止采集";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // txt_x1
            // 
            this.txt_x1.Location = new System.Drawing.Point(139, 209);
            this.txt_x1.Name = "txt_x1";
            this.txt_x1.Size = new System.Drawing.Size(35, 21);
            this.txt_x1.TabIndex = 8;
            // 
            // txt_x2
            // 
            this.txt_x2.Location = new System.Drawing.Point(139, 243);
            this.txt_x2.Name = "txt_x2";
            this.txt_x2.Size = new System.Drawing.Size(35, 21);
            this.txt_x2.TabIndex = 9;
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(32, 141);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(77, 12);
            this.label5.TabIndex = 10;
            this.label5.Text = "当前鼠标坐标";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(149, 141);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(11, 12);
            this.label6.TabIndex = 11;
            this.label6.Text = "X";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(212, 141);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(11, 12);
            this.label7.TabIndex = 12;
            this.label7.Text = "Y";
            // 
            // lbl_x
            // 
            this.lbl_x.AutoSize = true;
            this.lbl_x.Location = new System.Drawing.Point(149, 176);
            this.lbl_x.Name = "lbl_x";
            this.lbl_x.Size = new System.Drawing.Size(11, 12);
            this.lbl_x.TabIndex = 13;
            this.lbl_x.Text = "0";
            // 
            // lbl_y
            // 
            this.lbl_y.AutoSize = true;
            this.lbl_y.Location = new System.Drawing.Point(212, 176);
            this.lbl_y.Name = "lbl_y";
            this.lbl_y.Size = new System.Drawing.Size(11, 12);
            this.lbl_y.TabIndex = 14;
            this.lbl_y.Text = "0";
            // 
            // txt_y1
            // 
            this.txt_y1.Location = new System.Drawing.Point(198, 209);
            this.txt_y1.Name = "txt_y1";
            this.txt_y1.Size = new System.Drawing.Size(35, 21);
            this.txt_y1.TabIndex = 15;
            // 
            // txt_y2
            // 
            this.txt_y2.Location = new System.Drawing.Point(198, 243);
            this.txt_y2.Name = "txt_y2";
            this.txt_y2.Size = new System.Drawing.Size(35, 21);
            this.txt_y2.TabIndex = 16;
            // 
            // timer2
            // 
            this.timer2.Tick += new System.EventHandler(this.timer2_Tick);
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1});
            this.statusStrip1.Location = new System.Drawing.Point(0, 347);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(286, 22);
            this.statusStrip1.TabIndex = 17;
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            this.toolStripStatusLabel1.Size = new System.Drawing.Size(56, 17);
            this.toolStripStatusLabel1.Text = "采集状态";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(286, 369);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.txt_y2);
            this.Controls.Add(this.txt_y1);
            this.Controls.Add(this.lbl_y);
            this.Controls.Add(this.lbl_x);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.txt_x2);
            this.Controls.Add(this.txt_x1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txt_interval);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "胡博专用";
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txt_interval;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.TextBox txt_x1;
        private System.Windows.Forms.TextBox txt_x2;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label lbl_x;
        private System.Windows.Forms.Label lbl_y;
        private System.Windows.Forms.TextBox txt_y1;
        private System.Windows.Forms.TextBox txt_y2;
        private System.Windows.Forms.Timer timer2;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
    }
}

