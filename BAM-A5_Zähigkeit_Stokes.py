import linear_regression as lr
import numpy as np
#Eingabe der Werte in Stanadard!!!! SI einheiten (0 sind placeholder werte)
    #Literatur Werte
g=9.80665 #Ortsfaktor g in m*s^-2 Fehlerfrei nach Walcher A1.2

    #Eingabe der Geräte Fehler
o_Waage=2*10**-7 #Messfehler der Wage in kg
o_Stoppuhr=(2**0.5)*0.2 #Messfehler der Stoppuhr in s
o_Messleiste=10**-3 #Messfehker der Messleiste in m
o_Messschraube=10**-5 #Messfehler der Messschraube in m

    #Eingabe der Messwerte:
D_Gefaes=0 #Druchmesser des Gefäßes in m
h_Gefaes=0 #Höhe des Gefäßes in m
l_mess=0 #Länge der gemessenen Strecke für Zeitmessung in m
rho_oel=0 #Dichte des Öls in kg/m^3

        #erste Kugelsorte
m_5k_1=0 #Masse für fünf Kugeln der ersten Kugelsorte in kg
d_1=(0,0,0,0,0) #Durchmesser der ersten Kugelsorte in m
t_5k_1=(0,0,0,0,0) #Fallzeiten für die erste Kugelsorte in s

        #zweite Kugelsorte
m_5k_2=0 #Masse für fünf Kugeln der zweiten Kugelsorte in kg
d_2=(0,0,0,0,0) #Durchmesser der zweiten Kugelsorte in m
t_5k_2=(0,0,0,0,0) #Fallzeiten für die zweite Kugelsorte in s

        #dritte Kugelsorte
m_5k_3=0 #Masse für fünf Kugeln der dritten Kugelsorte in kg
d_3=(0,0,0,0,0) #Durchmesser der dritten Kugelsorte in m
t_5k_3=(0,0,0,0,0) #Fallzeiten für die dritte Kugelsorte in s

        #vierte Kugelsorte
m_5k_4=0 #Masse für fünf Kugeln der vierten Kugelsorte in kg
d_4=(0,0,0,0,0) #Durchmesser der vierten Kugelsorte in m
t_5k_4=(0,0,0,0,0) #Fallzeiten für die vierte Kugelsorte in s

#Auswertung
def r_kugel(d):
    r=1/10 * sum(d)
    h1=0
    for i in range(len(d)):
        h1=(0.5*d[i]-r)**2+h1
    o=((h1 / 4) ** 0.5)/(5 ** 0.5)
    return (d,o)

def m_Kugel(m_5,o):
    m=m_5/5
    o_m=o/5
    return (m,o_m)

def t_kugel(t_5):
    t=t_5/5
    h1 = 0
    for i in range(len(t_5)):
        h1 = (0.5 * t_5[i] - t) ** 2 + h1
    o =((h1 / 4) ** 0.5)/(5 ** 0.5)
    return (t,o)

def Zähigkeit_Stokes(m,r,rho,t,l, o_m, o_r, o_rho, o_t):
    eta=(m-0.75*np.pi*(r**3)*rho)*g*t/(6*np.pi*r*l)
    h1=m/r - 4*np.pi*rho*(r**2)/3
    o_h1=((o_m/r)**2+(-m/(r**2)-((8/3)*np.pi*r*rho)**2)*(o_r**2)+((-3*np.pi*(r**2)/4)**2)*(o_rho**2))**0.5
    o_eta=(((o_h1/h1)**2+(o_t/t)**2+(o_Messleiste/l)**2)**0.5)*eta
    return (eta,o_eta)

