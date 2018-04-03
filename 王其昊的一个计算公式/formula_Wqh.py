from tkinter import *
from sympy import *
import math
from scipy.optimize import fsolve

def main():
 	 
	root = Tk()
	root.title("formula_wqh_v1.0.0")
	Label(root, text="alpha和fai是角度制").grid(row=0, column=0)
	
	Label(root, text="alpha").grid(row=1, column=0)
	e_alpha = Entry(root)
	e_alpha.grid(row=1, column=1)

	Label(root, text="S_wb").grid(row=2, column=0)
	e_Swb = Entry(root)
	e_Swb.grid(row=2, column=1)

	Label(root, text="S_d").grid(row=3, column=0)
	e_Sd = Entry(root)
	e_Sd.grid(row=3, column=1)

	Label(root, text="z").grid(row=4, column=0)
	e_z = Entry(root)
	e_z.grid(row=4, column=1)

	Label(root, text="k").grid(row=5, column=0)
	e_k = Entry(root)
	e_k.grid(row=5, column=1)

	Label(root, text="emax").grid(row=6, column=0)
	e_emax = Entry(root)
	e_emax.grid(row=6, column=1)

	Label(root, text="emin").grid(row=7, column=0)
	e_emin = Entry(root)
	e_emin.grid(row=7, column=1)

	Label(root, text="y'_in").grid(row=8, column=0)
	e_yin = Entry(root)
	e_yin.grid(row=8, column=1)

	Label(root, text="fai'(内摩擦角)").grid(row=9, column=0)
	e_fai = Entry(root)
	e_fai.grid(row=9, column=1)

	Label(root, text="D_r").grid(row=10, column=0)
	e_Dr = Entry(root)
	e_Dr.grid(row=10, column=1)

	Label(root, text="y_w").grid(row=11, column=0)
	e_yw = Entry(root)
	e_yw.grid(row=11, column=1)

	Label(root, text="G_s").grid(row=12, column=0)
	e_Gs = Entry(root)
	e_Gs.grid(row=12, column=1)
	
	def calc():		
		x = symbols('x')
		# ---A-----------------------------
		alpha = float(e_alpha.get())/180*math.pi
		Swb = float(e_Swb.get())
		Sd = float(e_Sd.get())
		z = float(e_z.get())
		tana = math.tan(alpha)
		Sst = (Swb+Sd/tana)
		A = (1 + tana*( (Sst/math.sqrt(Sst**2+z**2)) - (Swb/(math.sqrt(Swb**2+z**2))) ))
		# --------------------------------

		# ---系数a1-----------------------------
		k = float(e_k.get())
		emax = float(e_emax.get())
		emin = float(e_emin.get())
		delta_e = emax-emin
		a1 = k/delta_e
		# --------------------------------

		# ---ln部分1-----------------------------
		yin = float(e_yin.get())
		fai = float(e_fai.get())/180*math.pi
		sinfai = math.sin(fai)
		Dr = float(e_Dr.get())
		yzS = yin*(z+Sd)
		eDdd = (1+emax-(Dr-x)*delta_e)
		ln1 = yzS*(3-2*sinfai)*eDdd
		# --------------------------------

		# ---ln部分2-----------------------------
		yw = float(e_yw.get())
		Gs = float(e_Gs.get())
		AzyG = A*z*yw*(Gs-1)
		ln2 = AzyG*(1+2*(1-sinfai)*((yzS*eDdd/AzyG)**sinfai))
		# --------------------------------	
		print('A =',A)
		print('delta_Dr = '+str(a1)+'*(ln'+str(ln1)+')-(ln'+str(ln2)+')')
		ans = solve(a1*(log(ln1)-log(ln2))-x, x)
		print('delta_Dr = ',ans)
		print('================================================')


	Button(root, text="计算", width=10,command=calc).grid(row=13, column=0, sticky=W, padx=10, pady=5)

	Button(root, text="关闭", width=10, command=root.quit).grid(row=13, column=1, sticky=E, padx=10, pady=5)

	mainloop()

if __name__ == '__main__':
    main()