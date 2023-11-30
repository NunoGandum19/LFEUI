import math 

c = 299792458 # m/s
m_prot = 0.938272 # GeV/c^2
m_B = 0.9314941 * 11.009305 # GeV/c^2
m_Be = 0.9314941 * 8.005305 # GeV/c^2
m_alpha = 0.931491 * 4.002603 # GeV/c^2
theta = (5*math.pi)/6 # rad

### I
Q_1 = (m_prot + m_B - m_Be - m_alpha)
print("Q_1 = ", Q_1 * 1000, "MeV")

T_prot = 0.7*0.001  # GeV
T_alpha0 = ((math.sqrt(m_prot * m_alpha * T_prot) * math.cos(theta))+ 
            math.sqrt(m_prot * m_alpha * T_prot * math.cos(theta) * math.cos(theta) + (m_Be+m_alpha)*(m_Be*Q_1 + (m_Be-m_prot)*T_prot)))/(m_Be + m_alpha)

print("T_alpha0 = ", T_alpha0 * 1000, "MeV")

#### II
E_asterisco = 3.04*0.001 # GeV
T_prot2 = 2.5*0.001 # GeV
T_alpha1 = ((math.sqrt(m_prot * m_alpha * T_prot2) * math.cos(theta))+ 
            math.sqrt(m_prot * m_alpha * T_prot2 * math.cos(theta) * math.cos(theta) + (m_Be + E_asterisco + m_alpha)*((m_Be + E_asterisco) *Q_1 + (m_Be + E_asterisco - m_prot)*T_prot2)))/(m_Be + E_asterisco + m_alpha)

print("T_alpha1 = ", T_alpha1 * 1000, "MeV")

#### III
Q_3 = (m_prot + m_B - 3 * m_alpha)
print("Q_3 = ", Q_3 * 1000, "MeV")