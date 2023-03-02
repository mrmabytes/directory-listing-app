#!/usr/bin/env python3

import os
import tkinter as tk
from time import sleep


class DirectoryListing:
    def __init__(self, initdir=None):
        self.top = tk.Tk()
        self.top.iconbitmap('icon.ico')
        self.top.title('Directory Listing App')

        # The Search Box. The user can enter the desired directory
        # here, hit Enter to see the results, delele faulty input,
        # although the app can take care of it too.
        self.cwd = tk.StringVar(self.top)
        self.dirn = tk.Entry(self.top, textvariable=self.cwd)
        self.dirn.bind('<Return>', self.search_dir)
        self.dirn.pack(fill='x', padx=3, pady=3)

        # This the full current directory, which is always displayed
        # at the bottom of the app.
        self.dirl = tk.Label(self.top, fg='black', font=('Arial', 9))
        self.dirl.pack(anchor='w', padx=3, pady=3, side='bottom')

        # The directories window. The user can go back by
        # double-clicking two dots in the upper left corner.
        self.dirsb = tk.Scrollbar(self.top)
        self.dirsb.pack(fill='y', side='right')
        self.dirs = tk.Listbox(
            self.top,
            width=50,
            height=50,
            yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.set_dir)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(expand=True, fill='both', padx=3, pady=3, side='left')

        if initdir:
            self.cwd.set(os.curdir)
            self.search_dir()

    def set_dir(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.search_dir()

    # Main search function with error checking. If the file does
    # not exist, the error message will appear in the Search Box.
    # It automatically dissappears after 2 seconds.
    def search_dir(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'
        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set('')
            self.dirs.config(
                selectbackground='LightSkyBlue')
            self.top.update()
            return

        dirlist = sorted(os.listdir(tdir))
        os.chdir(tdir)
        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, tk.END)
        self.dirs.insert(tk.END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(tk.END, eachFile)
        self.cwd.set('')
        self.dirs.config(
            selectbackground='LightSkyBlue')


if __name__ == '__main__':
    d = DirectoryListing(os.curdir)
    tk.mainloop()
