import math
#Eingabe der Werte in SI einheiten (0 sind placeholder werte)
    #Literatur Werte
g=9.80665 #Ortsfaktor g in m*s^-2 Fehlerfrei nach Walcher A1.2

    #Eingabe der Geräte Fehler
o_Waage=0 #Messfehler der Wage in kg
o_Stoppuhr=0 #Messfehler der Stoppuhr in s
o_Messleiste=0 #Messfehker der Messleiste in m

    #Eingabe Messwerte bzw. aus Zeichnung abgelesenen statische Methode
x_max_stat=0 #Maximale Auslenkungen in m
m_Halter=0 #Masse des Trägers in kg
m_Zusatz_stat=(0,0,0,0,0) #Liste mit den Zusatzmassen für die maximale Auslenkung in kg (m_ges wird bei Auswertung berechnet)
s_best_stat=0 #Steigung der Best fit Geraden in m/kg
s_min_stat=0 #Steigung der Minimal Geraden in m/kg
s_max_stat=0 #Steigung der Maximal Geraden in m/kg

    #Eingabe Messwerte bzw. aus Zeichnung abgelesenen Dynamische Methode
n_mess=0 #Anzahl gemessener Schwingungen
T_n_max=0 #Maximal gemessene Dauer von n schwingungen in Sekunden
m_Zusatz_dym=(0,0,0,0,0) #Zusatzmassen die bei der Dynamiscen methode aufgelegt wurde
s_best_dym=0  #Steigung der Best fit Geraden in m/kg
s_min_dym=0 #Steigung der Minimal Geraden in m/kg
s_max_dym=0 #Steigung der Maximal Geraden in m/kg
m_Feder=0 #Gewogene Feder Masse
m_eff_best_zeich=0 #Zeichnerisch bestimmte effektive Masse
m_eff_min_zeich=0 #Zeichnerisch bestimmter minimal Wert der effektive Masse
m_eff_max_zeich=0 #Zeichnerisch bestimmter maximal Wert der effektive Masse

#Auswertung Statische Methode
o_s_best_stat=max(abs(s_best_stat-s_min_stat),(abs(s_best_stat-s_max_stat))) #Fehler der Steigung statische Methode
D_stat_zeich=g/s_best_stat      #Federkonstante Zeichnerisch bestimmt statische Methode
o_D_stat_zeich=o_s_best_stat*g/s_best_stat**2 #Fehler Federkonstante Zeichnerisch bestimmt statische Methode
m_ges_stat=m_Halter+sum(m_Zusatz_stat) #Bestwert Gesamtmasse des Halter und Zusatzmassen statische Methode
o_m_ges_stat=math.sqrt((1+len(m_Zusatz_stat))*o_Waage**2) #fehler der Gesamtmasse der statischen Methode
D_stat_rech=m_ges_stat*g/x_max_stat #Bestwert der Federhärte D Rechnersich bestimmt
o_D_stat_rech=math.sqrt((o_m_ges_stat/m_ges_stat)**2 + (o_Messleiste/x_max_stat)**2)*D_stat_rech #Fehler der Federhärte D rechnerisch bestimmt

#Auswertung Dynamische Methode
T_f=T_n_max/n_mess #ZEit für eine Schwingung
o_T_f=o_Stoppuhr/n_mess #Fehler der Zeit für eine Schwingung
o_s_best_dym=max(abs(s_best_dym-s_min_dym),(abs(s_best_dym-s_max_dym))) #Fehler der Steigung Dynamische Methode
D_dym_zeich=4*(math.pi**2)/s_best_dym #Zeichnerich bestimmte Federhärte nach Dynamischer Methode
o_D_dym_zeich=4*(math.pi**2)*o_s_best_dym/(s_best_dym**2)  #Fehler der Zeichnerisch bestimmten Fehlerhärt nach Dynamischer Methode
m_ges_dym=m_Halter+sum(m_Zusatz_dym) #bestwert Gesamtmasse des Halter und der Zusatzmassen bei dynamischer Methode
o_m_ges_dym=math.sqrt((1+len(m_Zusatz_dym))*o_Waage**2) #fehler der Gesamtmasse der Dynamischen Methode
D_dym_rech=4*(math.pi**2)*m_ges_dym/(T_f**2) #Bestwert der Federhärte Rechnerisch bestimmt für dynamische Methode
o_d_dym_rech=math.sqrt((o_m_ges_dym/m_ges_dym)**2+4*(o_T_f/T_f)**2)*D_dym_rech #Fehler der Federhärte Rechnerisch bestimmt für dynamische Methode

#Bestimmung effektive Masse:
m_eff_rech=m_Feder/3 #Rechnerisch Bestimmte Effektive Masse
o_m_eff_rech=o_Waage/3 #Rechnerische Bestimmter Fehler der Effektiven Masse
o_m_eff_zeich=max(abs(m_eff_best_zeich-m_eff_min_zeich),abs(m_eff_max_zeich-m_eff_max_zeich)) #Fehler für Zeichnerisch bestimmte Effektive Masse

#Vergleich der Federkonstante:
n_gleich=(2*x_max_stat/T_f)*(o_Stoppuhr/o_T_f) #Benötigte Anzahl für gleiche Genauigkeit