import math
#Eingabe der Werte in Stanadrd!!!! SI einheiten (0 sind placeholder werte)
    #Literatur Werte
g=9.80665 #Ortsfaktor g in m*s^-2 Fehlerfrei nach Walcher A1.2

    #Eingabe der Geräte Fehler
o_Waage=10**-4 #Messfehler der Wage in kg
o_Stoppuhr=0.2 #Messfehler der Stoppuhr in s
o_Messleiste=10**-3 #Messfehker der Messleiste in m

    #Eingabe Messwerte bzw. aus Zeichnung abgelesenen statische Methode
x_max_stat=0 #Maximale Auslenkungen in m
m_Halter=0 #Masse des Trägers in kg
m_Zusatz=(0,0,0,0,0) #Liste mit allen Zusatzmassen für (statisch und dynamisch) in kg (m_ges wird bei Auswertung berechnet)
s_best_stat=0 #Steigung der Best fit Geraden in m/kg
s_min_stat=0 #Steigung der Minimal Geraden in m/kg
s_max_stat=0 #Steigung der Maximal Geraden in m/kg

    #Eingabe Messwerte bzw. aus Zeichnung abgelesenen Dynamische Methode
n_mess=0 #Anzahl gemessener Schwingungen
T_n_max=0 #Maximal gemessene Dauer von n schwingungen in Sekunden
s_best_dym=0  #Steigung der Best fit Geraden in s**2/kg
s_min_dym=0 #Steigung der Minimal Geraden in s**2/kg
s_max_dym=0 #Steigung der Maximal Geraden in s**2/kg
m_Feder=0 #Gewogene Feder Masse
m_eff_best_zeich=0 #Zeichnerisch bestimmte effektive Masse
m_eff_min_zeich=0 #Zeichnerisch bestimmter minimal Wert der effektive Masse
m_eff_max_zeich=0 #Zeichnerisch bestimmter maximal Wert der effektive Masse

#Auswertung Statische Methode
o_s_best_stat=max(abs(s_best_stat-s_min_stat),(abs(s_best_stat-s_max_stat))) #Fehler der Steigung statische Methode
D_best_stat_zeich=g/s_best_stat      # BestwertFederkonstante Zeichnerisch bestimmt statische Methode
o_D_stat_zeich=o_s_best_stat*g/s_best_stat**2 #Fehler Federkonstante Zeichnerisch bestimmt statische Methode
m_ges=m_Halter+sum(m_Zusatz) #Bestwert Gesamtmasse des Halter und Zusatzmassen statische Methode
o_m_ges=math.sqrt((1+len(m_Zusatz))*o_Waage**2) #fehler der Gesamtmasse der statischen Methode
D_stat_rech=m_ges*g/x_max_stat #Bestwert der Federhärte D Rechnersich bestimmt
o_D_stat_rech=math.sqrt((o_m_ges/m_ges)**2 + (o_Messleiste/x_max_stat)**2)*D_stat_rech #Fehler der Federhärte D rechnerisch bestimmt

#Auswertung Dynamische Methode
T_f=T_n_max/n_mess #ZEit für eine Schwingung
o_T_f=o_Stoppuhr/n_mess #Fehler der Zeit für eine Schwingung
o_s_best_dym=max(abs(s_best_dym-s_min_dym),(abs(s_best_dym-s_max_dym))) #Fehler der Steigung Dynamische Methode
D_best_dym_zeich=4*(math.pi**2)/s_best_dym #Zeichnerich bestimmte Federhärte nach Dynamischer Methode
D_min_dym_zeich=4*(math.pi**2)/s_min_dym
D_max_dym_zeich=4*(math.pi**2)/s_max_dym
o_D_dym_zeich=max(abs(D_best_dym_zeich-D_min_dym_zeich),(abs(D_best_dym_zeich-D_max_dym_zeich)))  #Fehler der Zeichnerisch bestimmten Fehlerhärt nach Dynamischer Methode #bestwert Gesamtmasse des Halter und der Zusatzmassen bei dynamischer Methode
D_dym_rech=4*(math.pi**2)*m_ges/(T_f**2) #Bestwert der Federhärte Rechnerisch bestimmt für dynamische Methode
o_D_dym_rech=math.sqrt((o_m_ges/m_ges)**2+4*(o_T_f/T_f)**2)*D_dym_rech #Fehler der Federhärte Rechnerisch bestimmt für dynamische Methode

#Bestimmung effektive Masse:
m_eff_rech=m_Feder/3 #Rechnerisch Bestimmte Effektive Masse
o_m_eff_rech=o_Waage/3 #Rechnerische Bestimmter Fehler der Effektiven Masse
o_m_eff_zeich=max(abs(m_eff_best_zeich-m_eff_min_zeich),abs(m_eff_max_zeich-m_eff_max_zeich)) #Fehler für Zeichnerisch bestimmte Effektive Masse

#Vergleich der Federkonstante:
n_gleich=(2*x_max_stat/T_f)*(o_Stoppuhr/o_Messleiste) #Benötigte Anzahl für gleiche Genauigkeit


#Ausgabe
print('Statische Methode:')
print('Fehler der Steigung: '+ str(o_s_best_stat))
print('Federhärte:'+ 'Zeichnerich: ('+str(D_best_stat_zeich)+'+/-'+str(o_D_stat_zeich)+')N/m   Rechnerisch: ('+str(D_stat_rech)+'+/-'+str(o_D_stat_rech)+')N/m')
print()
print('Dynamische Methode:')
print('Fehler der Steigung: '+ str(o_s_best_dym))
print('Federhärte:'+ 'Zeichnerich: ('+str(D_best_dym_zeich)+'+/-'+str(o_D_dym_zeich)+')N/m   Rechnerisch: ('+str(D_dym_rech)+'+/-'+str(o_D_dym_rech)+')N/m')
print()
print('Effektive Masse:')
print('Fehler der Zeichnerischen effektiven Masse:'+str(o_m_eff_zeich))
print('Rechnerisch bestimmte Effektiven Masse: ('+str(m_eff_rech)+'+/-'+str(o_m_eff_rech)+')kg')
print()
print('Vergleich Konstante:')
print('Anzahl der gemessenen Schwingungen für gleichen Fehler:'+str(n_gleich))