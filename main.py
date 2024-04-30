import numpy as np
import matplotlib.pyplot as plt
import customtkinter
from tkinter import messagebox



#US1 Newton

def button():
    dp = input_dp.get().replace(",", ".")#deltaP(Impuls)
    dm = input_dm.get().replace(",", ".")#deltaMasse
    ve = input_ve.get().replace(",", ".")#Geschwindigkeit der ausgestoßenen Gase relativ zur Rakete