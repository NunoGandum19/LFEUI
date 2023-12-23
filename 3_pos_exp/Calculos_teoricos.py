"""
from math import pi
from math import math.cos
from math import math.sqrt
"""
import math

m_alpha = 3727.983 #MeV   """6.645*pow(10,-27)"""
m_p = 938.272 #MeV  """1.673*pow(10,-27)"""
dalton = 931.294 #MeV """1.66*pow(10,-27)"""
m_b = 11.009 * dalton #MeV
m_be = 8.005 * dalton #MeV
theta = 5 * math.pi / 6 #rad
T_p1 = 0.675 #MeV
T_p2 = 0.805 #MeV
c = 299792458

def energia_alpha675(E_be):
    T_alpha1 = ((2*m_p*T_p1*m_alpha*math.cos(theta)*math.cos(theta) + (m_be+E_be+m_alpha)*(T_p1*(m_be+E_be-m_p)+(m_be+E_be)*(m_b+m_p-m_alpha-m_be-E_be)) + 2*math.sqrt((m_p*T_p1*m_alpha*math.cos(theta)*math.cos(theta))*(m_p*T_p1*m_alpha*math.cos(theta)*math.cos(theta)+(m_be+E_be+m_alpha)*(T_p1*(m_be+E_be-m_p)+(m_be+E_be)*(m_b+m_p-m_alpha-m_be-E_be))))) / pow((m_be+E_be+m_alpha),2))
    T_alpha2 = ((2*m_p*T_p1*m_alpha*math.cos(theta)*math.cos(theta) + (m_be+E_be+m_alpha)*(T_p1*(m_be+E_be-m_p)+(m_be+E_be)*(m_b+m_p-m_alpha-m_be-E_be)) - 2*math.sqrt((m_p*T_p1*m_alpha*math.cos(theta)*math.cos(theta))*(m_p*T_p1*m_alpha*math.cos(theta)*math.cos(theta)+(m_be+E_be+m_alpha)*(T_p1*(m_be+E_be-m_p)+(m_be+E_be)*(m_b+m_p-m_alpha-m_be-E_be))))) / pow((m_be+E_be+m_alpha),2))
    return (T_alpha1, T_alpha2)

def energia_alpha805(E_be):
    T_alpha1 = ((2*m_p*T_p2*m_alpha*math.cos(theta)*math.cos(theta) + (m_be+E_be+m_alpha)*(T_p2*(m_be+E_be-m_p)+(m_be+E_be)*(m_b+m_p-m_alpha-m_be-E_be)) + 2*math.sqrt((m_p*T_p2*m_alpha*math.cos(theta)*math.cos(theta))*(m_p*T_p2*m_alpha*math.cos(theta)*math.cos(theta)+(m_be+E_be+m_alpha)*(T_p2*(m_be+E_be-m_p)+(m_be+E_be)*(m_b+m_p-m_alpha-m_be-E_be))))) / pow((m_be+E_be+m_alpha),2))
    T_alpha2 = ((2*m_p*T_p2*m_alpha*math.cos(theta)*math.cos(theta) + (m_be+E_be+m_alpha)*(T_p2*(m_be+E_be-m_p)+(m_be+E_be)*(m_b+m_p-m_alpha-m_be-E_be)) - 2*math.sqrt((m_p*T_p2*m_alpha*math.cos(theta)*math.cos(theta))*(m_p*T_p2*m_alpha*math.cos(theta)*math.cos(theta)+(m_be+E_be+m_alpha)*(T_p2*(m_be+E_be-m_p)+(m_be+E_be)*(m_b+m_p-m_alpha-m_be-E_be))))) / pow((m_be+E_be+m_alpha),2))
    return (T_alpha1, T_alpha2)

print("Energia do protão = 0.675 MeV")
print("Energia máxima:")
print(energia_alpha675(0))
print("Outros valores possíveis")
print(energia_alpha675(3.03))

print()
print("Energia do protão = 0.805 MeV")
print("Energia máxima:")
print(energia_alpha805(0))
print("Outros valores possíveis")
print(energia_alpha805(3.03))