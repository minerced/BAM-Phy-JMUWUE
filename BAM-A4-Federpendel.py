import numpy as np
import sympy as sp
import math
#Eingabe der Werte in SI einheiten (0 sind placeholder werte)
    #Eingabe der Geräte Fehler
o_Waage=0 #Messfehler der Wage in kg
o_Stoppuhr=0 #Messfehler der Stoppuhr in s
o_Messleiste=0 #Messfehker der Messleiste in m

    #Eingabe Messwerte bzw. aus Zeichnung abgelesenen statische Methode
g=9.80665 #Ortsfaktor g in m*s^-2 Fehlerfrei nach Walcher A1.2 (bitte nicht ändern)
x_max_stat=0 #Maximale Auslenkungen in m
m_Halter=0 #Masse des Trägers in kg
m_Zusatz_stat=(0,0,0,0,0) #Liste mit den Zusatzmassen für die maximale Auslenkung in kg (m_ges wird bei Auswertung berechnet)
s_best_stat=0 #Steigung der Best fit Geraden in m/kg
s_min_stat=0 #Steigung der Minimal Geraden in m/kg
s_max_stat=0 #Steigung der Maximal Geraden in m/kg

    #Eingabe Messwerte bzw. aus Zeichnung abgelesenen Dynamische Methode
n_mess=0 #Anzahl gemessener Schwingungen
T_n=(0,0,0,0,0) #Dauer von n schwingungen in Sekunden
m_Zusatz_dym=(0,0,0,0,0)
s_best_dym=0  #Steigung der Best fit Geraden in m/kg
s_min_dym=0 #Steigung der Minimal Geraden in m/kg
s_max_dym=0 #Steigung der Maximal Geraden in m/kg
m_Feder=0 #Gewogene Feder Masse

#Auswertung Statische Methode
o_s_best_stat=max(abs(s_best_stat-s_min_stat),(abs(s_best_stat-s_max_stat))) #Fehler der Steigung statische Methode
D_stat_zeich=g/s_best_stat      #Federkonstante Zeichnerisch bestimmt statische Methode
o_D_stat_zeich=o_s_best_stat*g/(s_best_stat)**2 #Fehler Federkonstante Zeichnerisch bestimmt statische Methode
m_ges=m_Halter+sum(m_Zusatz_stat) #Bestwert Gesamtmasse des Halter und Zusatzmassen
o_m_ges=
D_stat_rech=m_ges*g/x_max_stat #Bestwert der Federhärte D Rechnersich bestimmt
