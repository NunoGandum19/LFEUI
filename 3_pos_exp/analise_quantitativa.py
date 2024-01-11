import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import xml.etree.ElementTree as ET
from reader import reader, plotter, plotter_3

############################ READ DATA ################################

"""info:
TT4 - primeira calibração com motor
TT5 - primeira calibração sem motor
TT7 - vidro 4
TT8 - vidro 3
TT9 - vidro 3.2
TT10 - não importa
TT11 - vidro 1 com carga demasiado pequena
TT12 - vidro 1
MUDANCA DE ENERGIA
TT13 - vidro 3.2
TT14 - vidro 3.2 com diferente ganho
TT15 - vidro 3 com diferente ganho
TT16 - vidro 4 com diferente ganho
TT18 - segunda calibração
-----------------------------
TT7-TT11 : carga 0.5microC
TT11 : carga 5 microC
TT12 : carga 20 microC
TT13: carga 0.5 microC
TT14, TT15, TT16: carga 20 micro C
"""

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


######################### DEF AQUISITION TIMES ####################################
time_TTS = [1.58,0.81667,0.61667,0.25,5.61667,19.1,0.9667,4.0833,4.5333,4.18333]
time_TTS = [x*60 for x in time_TTS] #in seconds

######################### DEF AQUISITION CHARGE ####################################
charge = [0.5,0.5,0.5,0.5,5,20,0.5,20,20,20] #in microCoulombs

######################### DEF THRESHOLDS ####################################

threshold_chn0 = [148,148,146,141,176,178,167]
threshold_chn1 = [169,155,171,173,169,176,171]

# threshold_chn0 = [156,156,156,156,156,156,156]
# threshold_chn1 = [156,156,156,156,156,156,156]

######################### PLOT DATA ####################################
TTs_Chn0 = [TT7_Chn0, TT8_Chn0, TT9_Chn0, TT12_Chn0, TT14_Chn0, TT15_Chn0, TT16_Chn0]
TTs_Chn1 = [TT7_Chn1, TT8_Chn1, TT9_Chn1, TT12_Chn1, TT14_Chn1, TT15_Chn1, TT16_Chn1]
TTs_Chn2 = [TT7_Chn2, TT8_Chn2, TT9_Chn2, TT12_Chn2, TT14_Chn2, TT15_Chn2, TT16_Chn2]
TTs_names = ["TT7", "TT8", "TT9", "TT12", "TT14", "TT15", "TT16"]
TTs_names = ['vidro 4', 'vidro 3', 'vidro 3.2', 'vidro 1', 'vidro 3.2 Energia 2', 'vidro 3 Energia 2', 'vidro 4 Energia 2']
# isto é : [vidro 4, vidro 3, vidro 3.2, vidro 1, |MUDANCA ENERGIA| vidro 3.2, vidro 3, vidro 4]

# for i in range(len(TTs_Chn0)): plotter(TTs_Chn0[i], TTs_names[i]+' Chn0')
# for i in range(len(TTs_Chn1)): plotter(TTs_Chn1[i], TTs_names[i]+' Chn1')

######################### CUT INITIAL NOISE ####################################
TTs_Chn0_cut = [x[threshold_chn0[i]:] for i, x in enumerate(TTs_Chn0)]
TTs_Chn1_cut = [x[threshold_chn1[i]:] for i, x in enumerate(TTs_Chn1)]
    
######################### PLOT CUT DATA ####################################
# for i in range(len(TTs_Chn0)):
#     plotter_3(TTs_Chn0[i], TTs_Chn1[i], TTs_Chn2[i], TTs_names[i])

######################### TRANSFORM IN NP ARRAYS ####################################
TTs_Chn0 = [np.array(x) for x in TTs_Chn0_cut]
TTs_Chn1 = [np.array(x) for x in TTs_Chn1_cut]

######################### CALCULATE INTEGRAL ####################################
integral_chn0 = [np.sum(x) / charge[i] for i, x in enumerate(TTs_Chn0)]
integral_chn1 = [np.sum(x) / charge[i] for i, x in enumerate(TTs_Chn1)]

######################### PRINT INTEGRAL ####################################
print("Integral chn0: ", integral_chn0)
print('')
print("Integral chn1: ", integral_chn1)

######################### CALCULATE PERCENTAGE   ####################################
p_SiO2_mass, p_B2O3_mass, p_Al2O3_mass, p_K2O_mass, p_SnO_mass, p_Br_mass = 0.4690, 0.3126, 0.0618, 0.0971, 0.014, 0.0455

percentagens_massicas = [0.4690, 0.3126, 0.0618, 0.0971, 0.014, 0.0455]

M_Si, M_O, M_B, M_Al, M_K, M_Sn, M_Br = 28.09, 16, 10.81, 26.98, 39.1, 118.71, 79.9

M_SiO2 = M_Si + 2*M_O
M_B2O3 = 2*M_B + 3*M_O
M_Al2O3 = M_Al + 3*M_O
M_K2O = 2*M_K + M_O
M_SnO = M_Sn + M_O
M_Br = M_Br

m_SiO2 = p_SiO2_mass / M_SiO2
m_B2O3 = p_B2O3_mass / M_B2O3
m_Al2O3 = p_Al2O3_mass / M_Al2O3
m_K2O = p_K2O_mass / M_K2O
m_SnO = p_SnO_mass / M_SnO
m_Br = p_Br_mass / M_Br

massas = np.array([m_SiO2, m_B2O3, m_Al2O3, m_K2O, m_SnO, m_Br])
numero_atomos = np.array([3, 5, 5, 3, 2, 1])
m_total = np.sum(massas)

percentagens_abs = [x/m_total for x in massas]

print('------------------------------------------')
print('Percentagem óxido boro: ', percentagens_abs[1])

percentagem_abs_vidro4 = percentagens_abs[1]/np.sum(numero_atomos*percentagens_abs)


######################### RELATIVE PERCENTAGES 1ST ENERGY ####################################
# print('------------------------------------------')
# print('')
# print('PRIMEIRA ENERGIA')
percentagens_relativas0_e1 = [round(x/integral_chn0[0],4) for x in integral_chn0[:4]]
percentagens_relativas1_e1 = [round(x/integral_chn1[0],4) for x in integral_chn1[:4]]
# print('As energias um sao: ', TTs_names[:4])
# print('')
# print("Percentagens relativas channel 0 (energia 1): ", percentagens_relativas0_e1)
# print("Percentagens relativas channel 1 (energia 1): ", percentagens_relativas1_e1)

######################### ABSOLUT PERCENTAGES 1ST ENERGY ####################################
percentagens_absolutas0_e1 = [round(x*percentagem_abs_vidro4,4) for x in percentagens_relativas0_e1]
percentagens_absolutas1_e1 = [round(x*percentagem_abs_vidro4,4) for x in percentagens_relativas1_e1]
# print('')
# print("Percentagens absolutas channel 0 (energia 1): ", percentagens_absolutas0_e1)
# print("Percentagens absolutas channel 1 (energia 1): ", percentagens_absolutas1_e1)

######################### RELATIVE PERCENTAGES 2ND ENERGY ####################################
# print('------------------------------------------')
# print('')
# print('SEGUNDA ENERGIA')
percentagens_relativas0_e2 = [round(x/integral_chn0[-1],4) for x in integral_chn0[4:]]
percentagens_relativas1_e2 = [round(x/integral_chn1[-1],4) for x in integral_chn1[4:]]
# print('As energias dois sao: ', TTs_names[4:])
# print('')
# print("Percentagens relativas channel 0 (energia 2): ", percentagens_relativas0_e2)
# print("Percentagens relativas channel 1 (energia 2): ", percentagens_relativas1_e2)

######################### ABSOLUT PERCENTAGES 2ND ENERGY ####################################
percentagens_absolutas0_e2 = [round(x*percentagem_abs_vidro4,4) for x in percentagens_relativas0_e2]
percentagens_absolutas1_e2 = [round(x*percentagem_abs_vidro4,4) for x in percentagens_relativas1_e2]
# print('')
# print("Percentagens absolutas channel 0 (energia 2): ", percentagens_absolutas0_e2)
# print("Percentagens absolutas channel 1 (energia 2): ", percentagens_absolutas1_e2)


######################### ORGANIZAR A INFORMAÇÃO PARA MOSTRAR POR AMOSTRA  ####################################
print('------------------------------------------')
print('Vidro 4')
print('')
print('Percentagens Relativas')
print('percentagens relativas channel 0 (energia 1): ', percentagens_relativas0_e1[0])
print('percentagens relativas channel 1 (energia 1): ', percentagens_relativas1_e1[0])
print('percentagens relativas channel 0 (energia 2): ', percentagens_relativas0_e2[-1])
print('percentagens relativas channel 1 (energia 2): ', percentagens_relativas1_e2[-1])
print('')
print('Percentagens Absolutas')
print('percentagens absolutas channel 0 (energia 1): ', percentagens_absolutas0_e1[0])
print('percentagens absolutas channel 1 (energia 1): ', percentagens_absolutas1_e1[0])
print('percentagens absolutas channel 0 (energia 2): ', percentagens_absolutas0_e2[-1])
print('percentagens absolutas channel 1 (energia 2): ', percentagens_absolutas1_e2[-1])

print('------------------------------------------')
print('Vidro 3')
print('')
print('Percentagens Relativas')
print('percentagens relativas channel 0 (energia 1): ', percentagens_relativas0_e1[1])
print('percentagens relativas channel 1 (energia 1): ', percentagens_relativas1_e1[1])
print('percentagens relativas channel 0 (energia 2): ', percentagens_relativas0_e2[-2])
print('percentagens relativas channel 1 (energia 2): ', percentagens_relativas1_e2[-2])
print('')
print('Percentagens Absolutas')
print('percentagens absolutas channel 0 (energia 1): ', percentagens_absolutas0_e1[1])
print('percentagens absolutas channel 1 (energia 1): ', percentagens_absolutas1_e1[1])
print('percentagens absolutas channel 0 (energia 2): ', percentagens_absolutas0_e2[-2])
print('percentagens absolutas channel 1 (energia 2): ', percentagens_absolutas1_e2[-2])

print('------------------------------------------')
print('Vidro 3.2')
print('')
print('Percentagens Relativas')
print('percentagens relativas channel 0 (energia 1): ', percentagens_relativas0_e1[2])
print('percentagens relativas channel 1 (energia 1): ', percentagens_relativas1_e1[2])
print('percentagens relativas channel 0 (energia 2): ', percentagens_relativas0_e2[-3])
print('percentagens relativas channel 1 (energia 2): ', percentagens_relativas1_e2[-3])
print('')
print('Percentagens Absolutas')
print('percentagens absolutas channel 0 (energia 1): ', percentagens_absolutas0_e1[2])
print('percentagens absolutas channel 1 (energia 1): ', percentagens_absolutas1_e1[2])
print('percentagens absolutas channel 0 (energia 2): ', percentagens_absolutas0_e2[-3])
print('percentagens absolutas channel 1 (energia 2): ', percentagens_absolutas1_e2[-3])

print('------------------------------------------')
print('Vidro 1')
print('')
print('Percentagens Relativas')
print('percentagens relativas channel 0 (energia 1): ', percentagens_relativas0_e1[3])
print('percentagens relativas channel 1 (energia 1): ', percentagens_relativas1_e1[3])
print('')
print('Percentagens Absolutas')
print('percentagens absolutas channel 0 (energia 1): ', percentagens_absolutas0_e1[3])
print('percentagens absolutas channel 1 (energia 1): ', percentagens_absolutas1_e1[3])
