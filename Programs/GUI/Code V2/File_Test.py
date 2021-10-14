####1####
##import tkinter
##from tkinter.filedialog import askopenfilename
##tk_root = tkinter.Tk()
##tk_root.withdraw()
##
##result = askopenfilename(
##    filetypes=[("PDF Documents", "*.pdf")],
##)


####2####
##import tkinter
##import tkinter.filedialog
##import os
##
##tk_root = tkinter.Tk()
##tk_root.withdraw()
##
##result = tkinter.filedialog.askopenfilename(
##    filetypes=[("PDF Documents", "*.pdf")],
##)
##
##currdir = os.getcwd()
##tempdir = tkinter.filedialog.askdirectory(parent=tk_root, initialdir=currdir, title='Select File')
##if len(tempdir)>0:
##    print ("You chose %s" % tempdir)


####3####
import tkinter
import tkinter.filedialog

tk_root = tkinter.Tk()
tk_root.withdraw()

result = tkinter.filedialog.askopenfilename(
    initialdir=tk_root,
    title="Select File",
    filetypes=[("PDF Documents", "*.pdf")],
)

if len(result)>0:
    print ("You chose %s" % result)

