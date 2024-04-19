import tkinter as tk

def checkCompScience():
    window = tk.Tk()
    window.title("Computer Science Admission Checker")
    window.geometry("640x480")
    
    mth_label = tk.Label(window, text="What grade did you get in your Mathematics WASSCE?")
    mth_label.pack()
    
    global mth_entry
    
    mth_entry = tk.Entry(window)
    mth_entry.pack()
    
    eng_label = tk.Label(window, text="What grade did you get in your English WASSCE?")
    eng_label.pack()
    
    global eng_entry
    
    eng_entry = tk.Entry(window)
    eng_entry.pack()
    
    phy_label = tk.Label(window, text="What grade did you get in your Physics WASSCE?")
    phy_label.pack()
    
    global phy_entry
    
    phy_entry = tk.Entry(window)
    phy_entry.pack()
    
    chem_label = tk.Label(window, text="What grade did you get in your Chemistry WASSCE?")
    chem_label.pack()
    
    global chem_entry
    
    chem_entry = tk.Entry(window)
    chem_entry.pack()
    
    comp_label = tk.Label(window, text="What grade did you get in your Computer Science WASSCE?")
    comp_label.pack()
    
    global comp_entry
    
    comp_entry = tk.Entry(window)
    comp_entry.pack()
    
    submit_button = tk.Button(window,text="Submit",command=submitCompSci)
    submit_button.pack()
    
    root.mainloop()
    
def submitCompSci():
    mth = mth_entry.get()
    eng = eng_entry.get()
    phy = phy_entry.get()
    chem = chem_entry.get()
    comp = comp_entry.get()
    
    detailSummary(mth,eng,phy,chem,comp,admitted,not_admitted,"Computer Science")

def detailSummary(g1,g2,g3,g4,g5,adm,n_adm,course):
    name = name_entry.get()
    score = int(jamb_entry.get())
    iview = iview_entry.get()
    
    pass_grades = ["A", "B", "C"]
    grades = [g1,g2,g3,g4,g5]
    
    if iview == 'y':
        interview = "Pass"
    else:
        interview = "Fail"
        
    details = {
                'name': name.title(), 'grade 1': g1.upper(),
                'grade 2': g2.upper(), 'grade 3': g3.upper(),
                'grade 4': g4.upper(), 'grade 5': g5.upper(),
                'jamb': score, 'interview': interview,
                'course':course
            }
    
    if score >= 250 and interview == "Pass":
        for grade in grades:
            if grade.upper() not in pass_grades:
                n_adm.append(details)
                return
            else:
                continue
        adm.append(details)
    else:
        n_adm.append(details)
    
def checkMassComm():
    window = tk.Tk()
    window.title("Computer Science Admission Checker")
    window.geometry("640x480")
    
    mth_label = tk.Label(window, text="What grade did you get in your Mathematics WASSCE?")
    mth_label.pack()
    
    global mmth_entry
    
    mmth_entry = tk.Entry(window)
    mmth_entry.pack()
    
    eng_label = tk.Label(window, text="What grade did you get in your English WASSCE?")
    eng_label.pack()
    
    global meng_entry
    
    meng_entry = tk.Entry(window)
    meng_entry.pack()
    
    lit_label = tk.Label(window, text="What grade did you get in your Literature WASSCE?")
    lit_label.pack()
    
    global lit_entry
    
    lit_entry = tk.Entry(window)
    lit_entry.pack()
    
    govt_label = tk.Label(window, text="What grade did you get in your Government WASSCE?")
    govt_label.pack()
    
    global govt_entry
    
    govt_entry = tk.Entry(window)
    govt_entry.pack()
    
    econs_label = tk.Label(window, text="What grade did you get in your Economics WASSCE?")
    econs_label.pack()
    
    global econs_entry
    
    econs_entry = tk.Entry(window)
    econs_entry.pack()
    
    submit_button = tk.Button(window, text="Submit", command=submitMassComm)
    submit_button.pack()
    
    root.mainloop()
    
def submitMassComm():
    mth = mmth_entry.get()
    eng = meng_entry.get()
    lit = lit_entry.get()
    govt = govt_entry.get()
    econs = econs_entry.get()
    
    detailSummary(mth,eng,lit,govt,econs,admitted,not_admitted, "Mass Communication")

def viewResults():
    window = tk.Tk()
    window.title("Results")
    window.geometry("800x600")
    
    if admitted:
        tk.Label(window, text="Admitted Students:").pack()
        for detail in admitted:
            tk.Label(window,text=detail).pack()
    else:
        tk.Label(window, text="No admitted students!").pack()
            
    if not_admitted:
        tk.Label(window, text="Non-Admitted Students:").pack()
        for detail in not_admitted:
            tk.Label(window, text=detail).pack()
    else:
        tk.Label(window, text="No non-admitted students!").pack()
        
    root.mainloop()

admitted = []
not_admitted = []

root = tk.Tk()
root.title("Admission Checker")
root.geometry("500x200")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

jamb_label = tk.Label(root, text="JAMB Score:")
jamb_label.pack()
jamb_entry = tk.Entry(root)
jamb_entry.pack()

iview_label = tk.Label(root, text="Did you pass the interview? (Enter y/n):")
iview_label.pack()
iview_entry = tk.Entry(root)
iview_entry.pack()

mass_comm_button = tk.Button(root, text="Mass Communication", command=checkMassComm)
mass_comm_button.pack()

comp_sci_button = tk.Button(root, text="Computer Science", command=checkCompScience)
comp_sci_button.pack()

view_results_button = tk.Button(root, text="View Results", command=viewResults)
view_results_button.pack()
       
root.mainloop()