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
o_rho_oel=0 # Fehler für die Dichte des Öls

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
    t=sum(t_5)/5
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

def Ladenburg (eta0, r):
    return (eta0/((1+2.1*r/(0.5*D_Gefaes))*(1+3.3*r/h_Gefaes)))

# Radius der vier Kugelsorten in m
r1, o_r1=r_kugel(d_1)
r2, o_r2=r_kugel(d_2)
r3, o_r3=r_kugel(d_3)
r4, o_r4=r_kugel(d_4)

# Masse der vier Kugelsorten in kg
m1, o_m1=m_Kugel(m_5k_1, o_Waage)
m2, o_m2=m_Kugel(m_5k_2, o_Waage)
m3, o_m3=m_Kugel(m_5k_3, o_Waage)
m4, o_m4=m_Kugel(m_5k_4, o_Waage)

#Fallzeit der vier Kugelsorten in s
t1, o_t1=t_kugel(t_5k_1)
t2, o_t2=t_kugel(t_5k_2)
t3, o_t3=t_kugel(t_5k_3)
t4, o_t4=t_kugel(t_5k_4)

#Zähigkeiten der 5 Kugelsorten kg/(s*m)
eta1, o_eta1=Zähigkeit_Stokes(m1,r1,rho_oel,t1,l_mess, o_m1, o_r1, o_rho_oel, o_t1)
eta2, o_eta2=Zähigkeit_Stokes(m2,r2,rho_oel,t2,l_mess, o_m2, o_r2, o_rho_oel, o_t2)
eta3, o_eta3=Zähigkeit_Stokes(m3,r3,rho_oel,t3,l_mess, o_m3, o_r3, o_rho_oel, o_t3)
eta4, o_eta4=Zähigkeit_Stokes(m4,r4,rho_oel,t4,l_mess, o_m4, o_r4, o_rho_oel, o_t4)

#best-fit gerade mit Zähigkeit auf y-Achse und radius auf x-Achse inklusive fehler
a, o_a, b, o_b= lr.linear_regression((r1,r2,r3,r4),(eta1,eta2,eta3,eta4),(o_eta1,o_eta2,o_eta3,o_eta4))

#Ladenburg Korrekturen
eta_Korregiert1=Ladenburg(b,r1)
eta_Korregiert2=Ladenburg(b,r2)
eta_Korregiert3=Ladenburg(b,r3)
eta_Korregiert4=Ladenburg(b,r4)

#Ausgabe
print("Kugelsorte 1: Radius: ("+str(r1)+"+/-"+str(o_r1)+")m,  Masse: ("+str(m1)+"+/-"+str(o_m1)+")kg,  Fallzeit: ("+str(t1)+'+/-'+str(o_t1)+")s,  Zähigkeit: ("+str(eta1)+"+/-"+str(o_eta1)+")kg/(m*s),   Ladenburg: "+str(eta_Korregiert1)+"kg/(m*s)")
print("Kugelsorte 2: Radius: ("+str(r2)+"+/-"+str(o_r2)+")m,  Masse: ("+str(m2)+"+/-"+str(o_m2)+")kg,  Fallzeit: ("+str(t2)+'+/-'+str(o_t2)+")s,  Zähigkeit: ("+str(eta2)+"+/-"+str(o_eta2)+")kg/(m*s),   Ladenburg: "+str(eta_Korregiert2)+"kg/(m*s)")
print("Kugelsorte 3: Radius: ("+str(r3)+"+/-"+str(o_r3)+")m,  Masse: ("+str(m3)+"+/-"+str(o_m3)+")kg,  Fallzeit: ("+str(t3)+'+/-'+str(o_t3)+")s,  Zähigkeit: ("+str(eta3)+"+/-"+str(o_eta3)+")kg/(m*s),   Ladenburg: "+str(eta_Korregiert3)+"kg/(m*s)")
print("Kugelsorte 4: Radius: ("+str(r4)+"+/-"+str(o_r4)+")m,  Masse: ("+str(m4)+"+/-"+str(o_m4)+")kg,  Fallzeit: ("+str(t4)+'+/-'+str(o_t4)+")s,  Zähigkeit: ("+str(eta4)+"+/-"+str(o_eta4)+")kg/(m*s),   Ladenburg: "+str(eta_Korregiert4)+"kg/(m*s)")
print()
print('Lineare-Regression: ('+str(a)+'+/-'+str(o_a)+")*x+("+str(b)+'+/-'+str(o_b)+")")