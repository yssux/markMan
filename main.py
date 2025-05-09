from tkinter import *
from tkinter import ttk
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

root = Tk()
icon = PhotoImage(file="wm_icon.png")
root.wm_attributes("-topmost", 1)
root.resizable(0,0)
root.title("markMan")
root.iconphoto(True, icon)
fr = ttk.Frame(root, padding=10)
fr.pack(fill="both", expand=True)
##################Var definitions#######################
version = StringVar()
version.set("alpha-GUI_dev")###Current Version var (for the version label)
####################Widget Creation############################
ttk.Style().configure("main.TLabel",
                      foreground="#000000",
                      font=("Helvetica", 50, "bold"),
                      padding=10)
ttk.Style().configure("version.TLabel",
                      foreground="#000000",
                      font=("Helvetica", 9),
                      padding=10)
lblMain = ttk.Label(fr,text="markMan", style="main.TLabel")
lblVer = ttk.Label(fr, textvariable=version, style="version.TLabel")
add_btn = ttk.Button(fr, text="➕ Add mark")
remove_btn = ttk.Button(fr, text="➖ Remove mark")
search_btn = ttk.Button(fr, text="🔍 Search")
show_btn = ttk.Button(fr, text="👓 Show Marks")
export_btn = ttk.Button(fr, text="⬇️ Export")
quit_btn = ttk.Button(fr, text="❌ Quit")
########################Widget Placement##################
lblMain.grid(column=0,row=0, columnspan=6)
lblVer.place(x=400, y=50)
lblMain.lift()
btn_list = [add_btn, remove_btn, search_btn, show_btn, export_btn, quit_btn]
i = 0
for btn in btn_list:
    btn.grid(column=i, row=3)
    i += 1
##########################################################
root.mainloop()
#Icon by Icon8 (https://icons8.com/icons/set/bookmark)
##x: 413, y:73