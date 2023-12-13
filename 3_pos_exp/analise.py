import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import xml.etree.ElementTree as ET
from reader import reader, plotter

############################ READ DATA ################################
### Read TT4 ###
TT4_Chn0 = reader("../2_exp/TT_4/UNFILTERED/CH0@N6781_21198_Espectrum_TT_4_20231205_163512.n42", 0)
TT4_Chn1 = reader("../2_exp/TT_4/UNFILTERED/CH1@N6781_21198_Espectrum_TT_4_20231205_163512.n42", 1)
TT4_Chn2 = reader("../2_exp/TT_4/UNFILTERED/CH2@N6781_21198_Espectrum_TT_4_20231205_163512.n42", 2)

### Read TT5 ###
TT5_Chn0 = reader("../2_exp/TT_5/UNFILTERED/CH0@N6781_21198_Espectrum_TT_5_20231205_163512.n42", 0)
TT5_Chn1 = reader("../2_exp/TT_5/UNFILTERED/CH1@N6781_21198_Espectrum_TT_5_20231205_163512.n42", 1)
TT5_Chn2 = reader("../2_exp/TT_5/UNFILTERED/CH2@N6781_21198_Espectrum_TT_5_20231205_163512.n42", 2)

### Read TT7 ###
TT7_Chn0 = reader("../2_exp/TT_7/UNFILTERED/CH0@N6781_21198_Espectrum_TT_7_20231205_163512.n42", 0)
TT7_Chn1 = reader("../2_exp/TT_7/UNFILTERED/CH1@N6781_21198_Espectrum_TT_7_20231205_163512.n42", 1)
TT7_Chn2 = reader("../2_exp/TT_7/UNFILTERED/CH2@N6781_21198_Espectrum_TT_7_20231205_163512.n42", 2)

### Read TT8 ###
TT8_Chn0 = reader("../2_exp/TT_8/UNFILTERED/CH0@N6781_21198_Espectrum_TT_8_20231205_163512.n42", 0)
TT8_Chn1 = reader("../2_exp/TT_8/UNFILTERED/CH1@N6781_21198_Espectrum_TT_8_20231205_163512.n42", 1)
TT8_Chn2 = reader("../2_exp/TT_8/UNFILTERED/CH2@N6781_21198_Espectrum_TT_8_20231205_163512.n42", 2)

### Read TT9 ###
TT9_Chn0 = reader("../2_exp/TT_9/UNFILTERED/CH0@N6781_21198_Espectrum_TT_9_20231205_163512.n42", 0)
TT9_Chn1 = reader("../2_exp/TT_9/UNFILTERED/CH1@N6781_21198_Espectrum_TT_9_20231205_163512.n42", 1)
TT9_Chn2 = reader("../2_exp/TT_9/UNFILTERED/CH2@N6781_21198_Espectrum_TT_9_20231205_163512.n42", 2)

### Read TT10 ###
TT10_Chn0 = reader("../2_exp/TT_10/UNFILTERED/CH0@N6781_21198_Espectrum_TT_10_20231205_163512.n42", 0)
TT10_Chn1 = reader("../2_exp/TT_10/UNFILTERED/CH1@N6781_21198_Espectrum_TT_10_20231205_163512.n42", 1)
TT10_Chn2 = reader("../2_exp/TT_10/UNFILTERED/CH2@N6781_21198_Espectrum_TT_10_20231205_163512.n42", 2)

### Read TT11 ###
TT11_Chn0 = reader("../2_exp/TT_11/UNFILTERED/CH0@N6781_21198_Espectrum_TT_11_20231205_163512.n42", 0)
TT11_Chn1 = reader("../2_exp/TT_11/UNFILTERED/CH1@N6781_21198_Espectrum_TT_11_20231205_163512.n42", 1)
TT11_Chn2 = reader("../2_exp/TT_11/UNFILTERED/CH2@N6781_21198_Espectrum_TT_11_20231205_163512.n42", 2)

### Read TT12 ###
TT12_Chn0 = reader("../2_exp/TT_12/UNFILTERED/CH0@N6781_21198_Espectrum_TT_12_20231205_163512.n42", 0)
TT12_Chn1 = reader("../2_exp/TT_12/UNFILTERED/CH1@N6781_21198_Espectrum_TT_12_20231205_163512.n42", 1)
TT12_Chn2 = reader("../2_exp/TT_12/UNFILTERED/CH2@N6781_21198_Espectrum_TT_12_20231205_163512.n42", 2)

### Read TT13 ###
TT13_Chn0 = reader("../2_exp/TT_13/UNFILTERED/CH0@N6781_21198_Espectrum_TT_13_20231205_163512.n42", 0)
TT13_Chn1 = reader("../2_exp/TT_13/UNFILTERED/CH1@N6781_21198_Espectrum_TT_13_20231205_163512.n42", 1)
TT13_Chn2 = reader("../2_exp/TT_13/UNFILTERED/CH2@N6781_21198_Espectrum_TT_13_20231205_163512.n42", 2)

### Read TT14 ###
TT14_Chn0 = reader("../2_exp/TT_14/UNFILTERED/CH0@N6781_21198_Espectrum_TT_14_20231205_163512.n42", 0)
TT14_Chn1 = reader("../2_exp/TT_14/UNFILTERED/CH1@N6781_21198_Espectrum_TT_14_20231205_163512.n42", 1)
TT14_Chn2 = reader("../2_exp/TT_14/UNFILTERED/CH2@N6781_21198_Espectrum_TT_14_20231205_163512.n42", 2)

### Read TT15 ###
TT15_Chn0 = reader("../2_exp/TT_15/UNFILTERED/CH0@N6781_21198_Espectrum_TT_15_20231205_163512.n42", 0)
TT15_Chn1 = reader("../2_exp/TT_15/UNFILTERED/CH1@N6781_21198_Espectrum_TT_15_20231205_163512.n42", 1)
TT15_Chn2 = reader("../2_exp/TT_15/UNFILTERED/CH2@N6781_21198_Espectrum_TT_15_20231205_163512.n42", 2)

### Read TT16 ###
TT16_Chn0 = reader("../2_exp/TT_16/UNFILTERED/CH0@N6781_21198_Espectrum_TT_16_20231205_163512.n42", 0)
TT16_Chn1 = reader("../2_exp/TT_16/UNFILTERED/CH1@N6781_21198_Espectrum_TT_16_20231205_163512.n42", 1)
TT16_Chn2 = reader("../2_exp/TT_16/UNFILTERED/CH2@N6781_21198_Espectrum_TT_16_20231205_163512.n42", 2)

### Read TT18 ###
TT18_Chn0 = reader("../2_exp/TT_18/UNFILTERED/CH0@N6781_21198_Espectrum_TT_18_20231205_163512.n42", 0)
TT18_Chn1 = reader("../2_exp/TT_18/UNFILTERED/CH1@N6781_21198_Espectrum_TT_18_20231205_163512.n42", 1)
TT18_Chn2 = reader("../2_exp/TT_18/UNFILTERED/CH2@N6781_21198_Espectrum_TT_18_20231205_163512.n42", 2)


