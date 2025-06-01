import numpy as np
import sympy as sp
#Eingabe der Werte in SI einheiten (0 sind placeholder werte)
    #Eingabe der Geräte Fehler
o_Waage=0 #Messfehler der Wage in kg
o_Stoppuhr=0 #Messfehler der Stoppuhr in s
o_Messleiste=0 #Messfehker der Messleiste in m

    #Eingabe Mess-/Abgelesenewerte statische Methode
g=9.80665 #Ortsfaktor g in m*s^-2 Fehlerfrei nach Walcher A1.2 (bitte nicht ändern)
x_stat=(0,0,0,0,0)  #Liste mit Auslenkungen in m
m_Halter=0 #Masse des Trägers in kg
m_Zusatz1=(0,0,0,0,0) #Liste mit den Zusatz massen in kg (m_ges wird bei Auswertung berechnet)
s_best_stat=0 #Steigung der Best fit geraden in m/kg
s_min_stat=0 #Steigung der Minimal geraden in m/kg
s_max_stat=0 #Steigung der Maximal geraden in m/kg
