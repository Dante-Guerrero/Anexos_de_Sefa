from tkinter import *
import tkinter as tk
from herramientas import mod1_acceso as acceso

########################################################################
class Aplicacion(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""

        self.root = parent
        self.root.withdraw()
        subFrame = acceso.Logueo(self)

#----------------------------------------------------------------------
def main():
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()

