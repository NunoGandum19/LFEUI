""" Objetivos:
    - Determinar se existe B nos materiais
    - Determinar a quantindade de B nos materiais
    - Verificar se existe Li na amostra que supostamente tinha Li
    - Determinar o endpoint do espectro de B (comparar com o Teórico)
    - Verificar se o motor influencia a calibração (calibração 4 - calibração 5)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import xml.etree.ElementTree as ET
from reader import reader, plotter, plotter_3
from sklearn.preprocessing import StandardScaler
#######################################################################
############################ READ DATA ################################
#######################################################################
### Read TT4 ###
TT4_Chn0 = reader("../2_exp/TT_4/UNFILTERED/CH0@N6781_21198_Espectrum_TT_4_20231205_163512.n42", 0)
TT4_Chn1 = reader("../2_exp/TT_4/UNFILTERED/CH1@N6781_21198_Espectrum_TT_4_20231205_163512.n42", 1)
TT4_Chn2 = reader("../2_exp/TT_4/UNFILTERED/CH2@N6781_21198_Espectrum_TT_4_20231205_163512.n42", 2)

### Read TT5 ###
TT5_Chn0 = reader("../2_exp/TT_5/UNFILTERED/CH0@N6781_21198_Espectrum_TT_5_20231205_165327.n42", 0)
TT5_Chn1 = reader("../2_exp/TT_5/UNFILTERED/CH1@N6781_21198_Espectrum_TT_5_20231205_165327.n42", 1)
TT5_Chn2 = reader("../2_exp/TT_5/UNFILTERED/CH2@N6781_21198_Espectrum_TT_5_20231205_165327.n42", 2)

### Read TT7 ###
TT7_Chn0 = reader("../2_exp/TT_7/UNFILTERED/CH0@N6781_21198_Espectrum_TT_7_20231205_171105.n42", 0)
TT7_Chn1 = reader("../2_exp/TT_7/UNFILTERED/CH1@N6781_21198_Espectrum_TT_7_20231205_171105.n42", 1)
TT7_Chn2 = reader("../2_exp/TT_7/UNFILTERED/CH2@N6781_21198_Espectrum_TT_7_20231205_171105.n42", 2)

### Read TT8 ###
TT8_Chn0 = reader("../2_exp/TT_8/UNFILTERED/CH0@N6781_21198_Espectrum_TT_8_20231205_171630.n42", 0)
TT8_Chn1 = reader("../2_exp/TT_8/UNFILTERED/CH1@N6781_21198_Espectrum_TT_8_20231205_171630.n42", 1)
TT8_Chn2 = reader("../2_exp/TT_8/UNFILTERED/CH2@N6781_21198_Espectrum_TT_8_20231205_171630.n42", 2)

### Read TT9 ###
TT9_Chn0 = reader("../2_exp/TT_9/UNFILTERED/CH0@N6781_21198_Espectrum_TT_9_20231205_171904.n42", 0)
TT9_Chn1 = reader("../2_exp/TT_9/UNFILTERED/CH1@N6781_21198_Espectrum_TT_9_20231205_171904.n42", 1)
TT9_Chn2 = reader("../2_exp/TT_9/UNFILTERED/CH2@N6781_21198_Espectrum_TT_9_20231205_171904.n42", 2)

### Read TT10 ###
TT10_Chn0 = reader("../2_exp/TT_10/UNFILTERED/CH0@N6781_21198_Espectrum_TT_10_20231205_172452.n42", 0)
TT10_Chn1 = reader("../2_exp/TT_10/UNFILTERED/CH1@N6781_21198_Espectrum_TT_10_20231205_172452.n42", 1)
TT10_Chn2 = reader("../2_exp/TT_10/UNFILTERED/CH2@N6781_21198_Espectrum_TT_10_20231205_172452.n42", 2)

### Read TT11 ###
TT11_Chn0 = reader("../2_exp/TT_11/UNFILTERED/CH0@N6781_21198_Espectrum_TT_11_20231205_173244.n42", 0)
TT11_Chn1 = reader("../2_exp/TT_11/UNFILTERED/CH1@N6781_21198_Espectrum_TT_11_20231205_173244.n42", 1)
TT11_Chn2 = reader("../2_exp/TT_11/UNFILTERED/CH2@N6781_21198_Espectrum_TT_11_20231205_173244.n42", 2)

### Read TT12 ###
TT12_Chn0 = reader("../2_exp/TT_12/UNFILTERED/CH0@N6781_21198_Espectrum_TT_12_20231205_175347.n42", 0)
TT12_Chn1 = reader("../2_exp/TT_12/UNFILTERED/CH1@N6781_21198_Espectrum_TT_12_20231205_175347.n42", 1)
TT12_Chn2 = reader("../2_exp/TT_12/UNFILTERED/CH2@N6781_21198_Espectrum_TT_12_20231205_175347.n42", 2)

### Read TT13 ###
TT13_Chn0 = reader("../2_exp/TT_13/UNFILTERED/CH0@N6781_21198_Espectrum_TT_13_20231205_181753.n42", 0)
TT13_Chn1 = reader("../2_exp/TT_13/UNFILTERED/CH1@N6781_21198_Espectrum_TT_13_20231205_181753.n42", 1)
TT13_Chn2 = reader("../2_exp/TT_13/UNFILTERED/CH2@N6781_21198_Espectrum_TT_13_20231205_181753.n42", 2)

### Read TT14 ###
TT14_Chn0 = reader("../2_exp/TT_14/UNFILTERED/CH0@N6781_21198_Espectrum_TT_14_20231205_182429.n42", 0)
TT14_Chn1 = reader("../2_exp/TT_14/UNFILTERED/CH1@N6781_21198_Espectrum_TT_14_20231205_182429.n42", 1)
TT14_Chn2 = reader("../2_exp/TT_14/UNFILTERED/CH2@N6781_21198_Espectrum_TT_14_20231205_182429.n42", 2)

### Read TT15 ###
TT15_Chn0 = reader("../2_exp/TT_15/UNFILTERED/CH0@N6781_21198_Espectrum_TT_15_20231205_183207.n42", 0)
TT15_Chn1 = reader("../2_exp/TT_15/UNFILTERED/CH1@N6781_21198_Espectrum_TT_15_20231205_183207.n42", 1)
TT15_Chn2 = reader("../2_exp/TT_15/UNFILTERED/CH2@N6781_21198_Espectrum_TT_15_20231205_183207.n42", 2)

### Read TT16 ###
TT16_Chn0 = reader("../2_exp/TT_16/UNFILTERED/CH0@N6781_21198_Espectrum_TT_16_20231205_183732.n42", 0)
TT16_Chn1 = reader("../2_exp/TT_16/UNFILTERED/CH1@N6781_21198_Espectrum_TT_16_20231205_183732.n42", 1)
TT16_Chn2 = reader("../2_exp/TT_16/UNFILTERED/CH2@N6781_21198_Espectrum_TT_16_20231205_183732.n42", 2)

### Read TT18 ###
TT18_Chn0 = reader("../2_exp/TT_18/UNFILTERED/CH0@N6781_21198_Espectrum_TT_18_20231205_184721.n42", 0)
TT18_Chn1 = reader("../2_exp/TT_18/UNFILTERED/CH1@N6781_21198_Espectrum_TT_18_20231205_184721.n42", 1)
TT18_Chn2 = reader("../2_exp/TT_18/UNFILTERED/CH2@N6781_21198_Espectrum_TT_18_20231205_184721.n42", 2)

########################################################################
######################### PLOT DATA ####################################
########################################################################

TTs_Chn0 = [TT4_Chn0, TT5_Chn0, TT7_Chn0, TT8_Chn0, TT9_Chn0, TT10_Chn0, TT11_Chn0, TT12_Chn0, TT13_Chn0, TT14_Chn0, TT15_Chn0, TT16_Chn0, TT18_Chn0]
TTs_Chn1 = [TT4_Chn1, TT5_Chn1, TT7_Chn1, TT8_Chn1, TT9_Chn1, TT10_Chn1, TT11_Chn1, TT12_Chn1, TT13_Chn1, TT14_Chn1, TT15_Chn1, TT16_Chn1, TT18_Chn1]
TTs_Chn2 = [TT4_Chn2, TT5_Chn2, TT7_Chn2, TT8_Chn2, TT9_Chn2, TT10_Chn2, TT11_Chn2, TT12_Chn2, TT13_Chn2, TT14_Chn2, TT15_Chn2, TT16_Chn2, TT18_Chn2]
TTs_names = ["TT4", "TT5", "TT7", "TT8", "TT9", "TT10", "TT11", "TT12", "TT13", "TT14", "TT15", "TT16", "TT18"]

"""for i in range(len(TTs_Chn0)):
    plotter_3(TTs_Chn0[i], TTs_Chn1[i], TTs_Chn2[i], TTs_names[i])  
"""

##########################################################################
######################### DEFINITIONS ####################################
##########################################################################
###### Define functions
def gaussian3_sum(x, a1, mu1, sigma1, a2, mu2, sigma2, a3, mu3, sigma3, c):
    return (a1 * np.exp(-(x - mu1)**2 / (2 * sigma1**2)) + 
            a2 * np.exp(-(x - mu2)**2 / (2 * sigma2**2)) +
            a3 * np.exp(-(x - mu3)**2 / (2 * sigma3**2)) + c)

def linear (x, a, b):
    return a*x + b

###### Define random things 
Channels = np.array(range(len(TT5_Chn0)))
x_grid = np.linspace(0, len(TT5_Chn0), 100000)

###### Theoretical Energies (Assumimos o Valor de Energia de Pico Como a média ponderada dos vários ficos) [E_Pu, E_Am, E_Cm]
Energias = [5.148, 5.478, 5.795] # MeV

###### Define the aquisition times
time_TTs = [95, 49, 37, 15, 337, 1146, 58, 245, 272, 251] #in seconds

###### Define the thresholds
thresholds = [170, 170, 170, 170, 170, 170, 95, 95, 95, 95]

###### Define the data
Data_Chn0 = TTs_Chn0[2:len(TTs_Chn0)-1]
Data_Chn1 = TTs_Chn1[2:len(TTs_Chn1)-1]

##########################################################################
######################### CALIBRATION ####################################
##########################################################################
###### Calibration 1 
### Calibration with TT5 ###
Detectors_TT5 = [TT5_Chn0, TT5_Chn1]

# Define initial guess and bounds 
p0_TT5 = [[100, 650, 10, 100, 700, 10, 100, 730, 10, 0], [90, 650, 5, 90, 692, 5, 90, 733, 5, 0]]
bounds_TT5 = ([[75, 600, 0, 75, 650, 0, 75, 700, 0, 0], [125, 700, 15, 125, 750, 15, 125, 760, 15, 0.001]], 
              [[80, 625, 4.5, 80, 675, 4.5, 80, 715, 4.5, 0], [100, 670, 10, 100, 700, 10, 100, 750, 10, 0.001]])

m_TT5, b_TT5, delta_m_TT5, delta_b_TT5 = [], [], [], []
for i in range(len(Detectors_TT5)):
    # Fit data
    params1, covariance = curve_fit(gaussian3_sum, Channels, Detectors_TT5[i], p0=p0_TT5[i], bounds=bounds_TT5[i], method='trf')

    A_Pu, mu_Pu, sigma_Pu, A_Am, mu_Am, sigma_Am, A_Cm, mu_Cm, sigma_Cm, C = params1
    errors = np.sqrt(np.diag(covariance))

    """print (f"Pu: A = {A_Pu} +- {errors[0]}, mu = {mu_Pu} +- {errors[1]}, sigma = {sigma_Pu} +- {errors[2]}")
    print (f"Am: A = {A_Am} +- {errors[3]}, mu = {mu_Am} +- {errors[4]}, sigma = {sigma_Am} +- {errors[5]}")
    print (f"Cr: A = {A_Cm} +- {errors[6]}, mu = {mu_Cm} +- {errors[7]}, sigma = {sigma_Cm} +- {errors[8]}")
    """
    """# Plot data
    plt.figure(figsize=(10, 6))
    plt.plot(Channels, TT5_Chn0, 'b-', label='data')
    plt.plot(x_grid, gaussian3_sum(x_grid, *params1), 'r-', label='fit')
    plt.yscale("log")  
    plt.xlabel("Channel")
    plt.ylabel("Counts (log scale)")
    plt.show()"""

    Canais_médias = [mu_Pu, mu_Am, mu_Cm]

    #### Calibration 
    params2, covariance = curve_fit(linear, Canais_médias, Energias)
    a, b = params2
    errors = np.sqrt(np.diag(covariance))
    #print (f"a = {a} +- {errors[0]}, b = {b} +- {errors[1]}")

    """xfit = np.linspace(mu_Pu - 20, mu_Cm + 20, 100000)
    plt.plot(xfit , linear(xfit, *params2), 'r-', label='fit')
    plt.plot(Canais_médias, Energias, label='data', marker = 'o', color = 'black', linestyle='None')
    plt.text(0.1, 0.90, f'a: {a:.4f} +- {"{:.7f}".format(errors[0])}', transform = plt.gca().transAxes, color='black')
    plt.text(0.1, 0.85, f'b: {b:.4f} +- {"{:.5f}".format(errors[1])}', transform = plt.gca().transAxes, color='black')
    plt.xlabel("Channel")
    plt.ylabel("Energy (MeV)")
    plt.grid()
    plt.show()"""
    
    m_TT5.append(a)
    b_TT5.append(b)
    delta_m_TT5.append(errors[0])
    delta_b_TT5.append(errors[1])

print("Calibration")
print (f"Chn0: m = {m_TT5[0]} +- {delta_m_TT5[0]}, b = {b_TT5[0]} +- {delta_b_TT5[0]}")
print (f"Chn1: m = {m_TT5[1]} +- {delta_m_TT5[1]}, b = {b_TT5[1]} +- {delta_b_TT5[1]}")

###### Calibration 2 
### Calibration with TT18
Detectors_TT18 = [TT18_Chn0, TT18_Chn1]

# Define initial guess and bounds 
p0_TT18 = [[50, 555, 5, 50, 600, 5, 50, 630, 5, 0], [50, 557, 4, 50, 591, 4, 50, 625, 4, 0]]
bounds_TT18 = ([[25, 545, 0, 25, 585, 0, 25, 615, 0, 0], [75, 570, 10, 75, 600, 10, 75, 635, 10, 0.001]], 
               [[25, 552, 2, 25, 587, 2, 25, 620, 2, 0], [75, 566, 6, 75, 597, 6, 75, 630, 6, 0.001]])

m_TT18, b_TT18, delta_m_TT18, delta_b_TT18 = [], [], [], []
for i in range(len(Detectors_TT18)):
    # Fit data
    params1, covariance = curve_fit(gaussian3_sum, Channels, Detectors_TT18[i], p0=p0_TT18[i], bounds=bounds_TT18[i], method='trf')

    A_Pu, mu_Pu, sigma_Pu, A_Am, mu_Am, sigma_Am, A_Cm, mu_Cm, sigma_Cm, C = params1
    errors = np.sqrt(np.diag(covariance))

    """print (f"Pu: A = {A_Pu} +- {errors[0]}, mu = {mu_Pu} +- {errors[1]}, sigma = {sigma_Pu} +- {errors[2]}")
    print (f"Am: A = {A_Am} +- {errors[3]}, mu = {mu_Am} +- {errors[4]}, sigma = {sigma_Am} +- {errors[5]}")
    print (f"Cr: A = {A_Cm} +- {errors[6]}, mu = {mu_Cm} +- {errors[7]}, sigma = {sigma_Cm} +- {errors[8]}")
    """
    """# Plot data
    plt.figure(figsize=(10, 6))
    plt.plot(Channels, TT18_Chn0, 'b-', label='data')
    plt.plot(x_grid, gaussian3_sum(x_grid, *params1), 'r-', label='fit')
    plt.yscale("log")  
    plt.xlabel("Channel")
    plt.ylabel("Counts (log scale)")
    plt.show()"""

    Canais_médias = [mu_Pu, mu_Am, mu_Cm]

    #### Calibration 
    params2, covariance = curve_fit(linear, Canais_médias, Energias)
    a, b = params2
    errors = np.sqrt(np.diag(covariance))
    #print (f"a = {a} +- {errors[0]}, b = {b} +- {errors[1]}")

    """xfit = np.linspace(mu_Pu - 20, mu_Cm + 20, 100000)
    plt.plot(xfit , linear(xfit, *params2), 'r-', label='fit')
    plt.plot(Canais_médias, Energias, label='data', marker = 'o', color = 'black', linestyle='None')
    plt.text(0.1, 0.90, f'a: {a:.4f} +- {"{:.7f}".format(errors[0])}', transform = plt.gca().transAxes, color='black')
    plt.text(0.1, 0.85, f'b: {b:.4f} +- {"{:.5f}".format(errors[1])}', transform = plt.gca().transAxes, color='black')
    plt.xlabel("Channel")
    plt.ylabel("Energy (MeV)")
    plt.grid()
    plt.show()"""
    
    m_TT18.append(a)
    b_TT18.append(b)
    delta_m_TT18.append(errors[0])
    delta_b_TT18.append(errors[1])

print("Calibration")
print (f"Chn0: m = {m_TT18[0]} +- {delta_m_TT18[0]}, b = {b_TT18[0]} +- {delta_b_TT18[0]}")
print (f"Chn1: m = {m_TT18[1]} +- {delta_m_TT18[1]}, b = {b_TT18[1]} +- {delta_b_TT18[1]}")
print("\n")

################################################################################
######################### QUALIFICATION ########################################
################################################################################

### Endpoint dos espetros de B
def over_log(x, a, b):
    return a/(np.log(x)) + b

def endpoint(data, xmin, xmax):
    x = np.linspace(xmin, xmax, len(data) * 100)
        
    p1, cov1 = curve_fit(linear, Channels[xmin:xmax], data[xmin:xmax])
    a, b = p1
    err = np.sqrt(np.diag(cov1))
    
    plt.figure(figsize=(10, 6))
    plt.plot(Channels[xmin: xmax], data[xmin: xmax], 'b-', label='data', linestyle='None', marker='o')
    plt.plot(x, linear(x, *p1), 'r-', label='a*x + b')
    plt.text(0.6, 0.90, f'a: {a:.4f} +- {"{:.4f}".format(err[0])}', transform = plt.gca().transAxes, color='black')
    plt.text(0.6, 0.85, f'b: {b:.4f} +- {"{:.4f}".format(err[1])}', transform = plt.gca().transAxes, color='black')
    plt.grid()
    plt.xlabel("Channel")
    plt.ylabel("Counts ")
    plt.legend()
    plt.show()
    return -b/a

def endpoint2(data, xmin, xmax):
    x = np.linspace(xmin, xmax, len(data) * 100)

    p1, cov1 = curve_fit(over_log, Channels[xmin:xmax], data[xmin:xmax])
    a, b = p1
    err = np.sqrt(np.diag(cov1))

    plt.figure(figsize=(10, 6))
    plt.plot(Channels[xmin: xmax], data[xmin: xmax], 'b-', label='data', linestyle='None', marker='o')
    plt.plot(x, over_log(x, *p1), 'r-', label='a/(log(x)) + b')
    plt.text(0.6, 0.90, f'a: {a:.4f} +- {"{:.4f}".format(err[0])}', transform = plt.gca().transAxes, color='black')
    plt.text(0.6, 0.85, f'b: {b:.4f} +- {"{:.4f}".format(err[1])}', transform = plt.gca().transAxes, color='black')
    plt.grid()
    plt.xlabel("Channel")
    plt.ylabel("Counts")
    plt.legend()
    plt.show()
    return np.exp(-a/b)


    x = np.linspace(xmin, xmax, len(data) * 100)

    p1, cov1 = curve_fit(exp_neg, Channels[xmin:xmax], data[xmin:xmax], p0=[10, -1, 500])
    a, b, x0 = p1

    plt.figure(figsize=(10, 6))
    plt.plot(Channels[xmin: xmax], data[xmin: xmax], 'b-', label='data', linestyle='None', marker='o')
    plt.plot(x, exp_neg(x, *p1), 'r-', label='exp(-a*(x-x0)) + b')
    plt.text(0.6, 0.90, f'a: {a:.4f} +- {"{:.4f}".format(errors[0])}', transform = plt.gca().transAxes, color='black')
    plt.text(0.6, 0.85, f'b: {b:.4f} +- {"{:.4f}".format(errors[1])}', transform = plt.gca().transAxes, color='black')
    plt.text(0.6, 0.80, f'x0: {x0:.4f} +- {"{:.4f}".format(errors[2])}', transform = plt.gca().transAxes, color='black')
    plt.grid()
    plt.xlabel("Channel")
    plt.ylabel("Counts")
    plt.legend()
    plt.show()
    return - np.log(-b) / a

# TT7
endpoint_TT7 = endpoint(TT7_Chn0, 500, 600)
endpoint_TT7_2 = endpoint2(TT7_Chn0, 500, 600)
endpoint_TT7_3 = endpoint3(TT7_Chn0, 500, 600)
print ("Endpoint TT7 com linear: ", endpoint_TT7)
print ("Endpoint TT7 com 1/log: ", endpoint_TT7_2)

print("\n")
################################################################################
######################### QUANTIFICATION #######################################
################################################################################
def Integral(data, time, threshold):
    res = 0
    for i in range(threshold, len(data)):
        res += data[i]
    return res / time

Integral_Chn0, Integral_Chn1 = [], []
for i in range(len(Data_Chn0)):
    integral0 = Integral(Data_Chn0[i], time_TTs[i], thresholds[i])
    integral1 = Integral(Data_Chn1[i], time_TTs[i], thresholds[i])
    Integral_Chn0.append(integral0)
    Integral_Chn1.append(integral1)

print ("Integrais Chn0:", Integral_Chn0)
print ("Integrais Chn1:", Integral_Chn1)


