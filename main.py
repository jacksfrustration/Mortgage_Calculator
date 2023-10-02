import tkinter
from tkinter import messagebox
def calc_mort():
    '''gets years to pay back, interest and deposit percentage
    and total loan amount and outputs monthly payments
    this process is automated so if there are non-digits or empty
    entries the program will not crash and will output appropriate error message'''
    try:
        loan=round(float(loan_ent.get()),2)
    except ValueError:
        messagebox.showerror(title="Oops",message="Loan Amount not applicable")
    else:
        try:
            term=int(term_ent.get())
        except ValueError:
            messagebox.showerror(title="Oops",message="Time to pay back by not applicable")
        else:
            num_payments=term*12
            try:
                interest=(float(interest_ent.get())/100)/12
            except ValueError:
                messagebox.showerror(title="Oops",message="Interest rate not applicable")
            else:
                try:
                    deposit_percentage=float(dep_ent.get())/100
                    deposit_amount=deposit_percentage*loan
                except ValueError:
                    messagebox.showerror(title="Oops",message="Deposit percentage not applicable")
                else:
                    loan_remainder=loan-deposit_amount
                    monthly_payments=abs(round((loan_remainder*interest)/(1-((1+interest)**(-num_payments))),2))
                    res=('{:,}'.format(monthly_payments))
                    loan_res=('{:,}'.format(loan))

                    messagebox.showinfo(title="Mortgage Payment",message=f"You have borrowed £{loan_res}0 and you have {term} years to pay it back\n"
                                                                     f"Initial deposit percentage of {deposit_percentage*100}0%\n"
                    f"You have to pay £{res} a month.\n")

window=tkinter.Tk()
window.title("Mortgage Calculator")
window.config(padx=50,pady=50)
canvas=tkinter.Canvas(window,width=600,height=315)
img=tkinter.PhotoImage(file="Mortgage_1488379562.png")
bg=canvas.create_image(300,157, image=img)
canvas.grid(row=0,column=1)
loan_lbl=tkinter.Label(text="Loan Amount:")
loan_lbl.grid(column=0,row=1)
loan_ent=tkinter.Entry()
loan_ent.grid(column=1,row=1)
term_lbl=tkinter.Label(text="Years to pay back:")
term_lbl.grid(column=0,row=2)
term_ent=tkinter.Entry()
term_ent.grid(column=1,row=2)
pay_win_lbl=tkinter.Label(text="Payment Window:")
pay_win_lbl.grid(column=0,row=4)
interest_lbl=tkinter.Label(text="Interest percentage:")
interest_lbl.grid(column=0,row=4)
interest_ent=tkinter.Entry()
interest_ent.grid(column=1,row=4)
dep_lbl=tkinter.Label(text="Deposit Percentage")
dep_lbl.grid(row=5,column=0)
dep_ent=tkinter.Entry()
dep_ent.grid(row=5,column=1)
calc_img=tkinter.PhotoImage(file="calculate.png")
calc_but=tkinter.Button(image=calc_img,text="Calculate",command=calc_mort,borderwidth=0,compound="bottom")
calc_but.grid(row=6,column=1)
window.mainloop()