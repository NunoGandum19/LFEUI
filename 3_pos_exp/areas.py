import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import xml.etree.ElementTree as ET
from reader import reader, plotter, plotter_3

############################ READ DATA ################################

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

######################### DEF THRESHOLDS ####################################

threshold = []

######################### PLOT DATA ####################################
TTs_Chn0 = [TT7_Chn0, TT8_Chn0, TT9_Chn0, TT10_Chn0, TT11_Chn0, TT12_Chn0, TT13_Chn0, TT14_Chn0, TT15_Chn0, TT16_Chn0]
TTs_Chn1 = [TT7_Chn1, TT8_Chn1, TT9_Chn1, TT10_Chn1, TT11_Chn1, TT12_Chn1, TT13_Chn1, TT14_Chn1, TT15_Chn1, TT16_Chn1]
TTs_Chn2 = [TT7_Chn2, TT8_Chn2, TT9_Chn2, TT10_Chn2, TT11_Chn2, TT12_Chn2, TT13_Chn2, TT14_Chn2, TT15_Chn2, TT16_Chn2]
TTs_names = ["TT7", "TT8", "TT9", "TT10", "TT11", "TT12", "TT13", "TT14", "TT15", "TT16"]


######################### CUT INITIAL NOISE ####################################
TTs_Chn0 = [x[20:] for x in TTs_Chn0]
TTs_Chn1 = [x[20:] for x in TTs_Chn1]
TTs_Chn2 = [x[20:] for x in TTs_Chn2]

######################### TRANSFORM IN NP ARRAYS ####################################
TTs_Chn0 = [np.array(x) for x in TTs_Chn0]
TTs_Chn1 = [np.array(x) for x in TTs_Chn1]
TTs_Chn2 = [np.array(x) for x in TTs_Chn2]

""" def sum_chn (TTs_Chn, threshold: list, times: list):
     for i in range(len(TTs_Chn)):
         plotter(TTs_Chn[i], TTs_names[i])
         counts_chn = 0
         list_chn = []
         for j in range(threshold[i], len(TTs_Chn0[i])):
             counts_chn += TTs_Chn0[i][j]
             counts_chn = counts_chn / times[i]
         print('sai')
         list_chn.append(counts_chn)
     return list_chn"""

######################### CALCULATE INTEGRAL ####################################
list_chn0 = [np.sum(x) / time_TTS[i] for i, x in enumerate(TTs_Chn0)]
list_chn1 = [np.sum(x) / time_TTS[i] for i, x in enumerate(TTs_Chn1)]
list_chn2 = [np.sum(x) / time_TTS[i] for i, x in enumerate(TTs_Chn2)]

######################### PRINT INTEGRAL ####################################
print("Integral chn0: ", list_chn0)
print('')
print("Integral chn1: ", list_chn1)
print('')
print("Integral chn2: ", list_chn2)

    
        

