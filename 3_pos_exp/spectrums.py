import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import xml.etree.ElementTree as ET
from reader import reader, plotter, plotter_2, plotter_3
from sklearn.preprocessing import StandardScaler
from scipy.stats import skewnorm

"""
Energia do protão = 0.675 MeV
Energia alpha máxima (estado fundamental):
5.55901117870905
Energia alpha estado excitado central:
3.646384715851524
Energia alpha estado excitado minima:
4.008593652291615
Energia alpha estado excitado maxima:
3.2852100894369483

Energia berilio máxima (estado fundamental):
1.249777607792777
Energia berilio estado excitado central:
0.7979891346128403
Energia berilio estado excitado minima:
0.8830546752368409
Energia berilio estado excitado maxima:
0.7134633083686994
"""

##### Build the spectrum (esboço) #####
A = 100
E_alpha_max = 5.55901117870905
E_alpha_exc_mean = 3.646384715851524
E_alpha_exc_max = 4.008593652291615
E_alpha_exc_min = 3.2852100894369483

E_Be_max = 1.249777607792777
E_Be_exc_mean = 0.7979891346128403
E_Be_exc_max = 0.8830546752368409
E_Be_exc_min = 0.7134633083686994

###################### Gaussian #############################
## Alpha 1
plt.figure()
plt.plot([E_alpha_max, E_alpha_max], [0, 15], linewidth=2, color = 'dodgerblue')
plt.plot([E_alpha_exc_mean, E_alpha_exc_mean], [0, 100], linewidth=2, color = 'dodgerblue')
plt.text(0.47, 21/24, r'$\alpha_1$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.text(0.7, 1/6, r'$\alpha_0$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()

## Alpha 2
sigma_alpha = 0.75*(E_alpha_exc_max-E_alpha_exc_min)
x1 = np.linspace(E_alpha_exc_mean - 3 * sigma_alpha, E_alpha_exc_mean + 3 * sigma_alpha, 1000)
y1 = A * np.exp(-0.5 * ((x1 - E_alpha_exc_mean) / sigma_alpha)**2)

plt.figure()
plt.plot([E_alpha_max, E_alpha_max], [0, 15], linewidth=2, color = 'dodgerblue')
plt.plot(x1, y1, linewidth=2, color = 'dodgerblue')
plt.text(0.47, 21/24, r'$\alpha_1$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.text(0.7, 1/6, r'$\alpha_0$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()

## Berilium1
plt.figure()
plt.plot([E_Be_max, E_Be_max], [0, 10], linewidth=2, color = 'red')
plt.plot([E_Be_exc_mean, E_Be_exc_mean], [0, 60], linewidth=2, color = 'red')
plt.text(1/8-0.01, 7/12 - 0.05, r'$\alpha_1 (Be)$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.text(3/16, 1/6 - 0.05, r'$\alpha_0 (Be)$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()

## Berilium2
sigma_Be = (E_Be_exc_max - E_Be_exc_min)*2
x2 = np.linspace(E_Be_exc_mean - 3 * sigma_Be, E_Be_exc_mean + 3 * sigma_Be, 1000)
y2 = A * np.exp(-0.5 * ((x2 - E_Be_exc_mean) / sigma_Be*0.8)**2)
y3 = 0.6 * A * np.exp(-0.5 * ((x2 - E_Be_exc_mean) / sigma_Be*0.8)**2)
x4 = np.linspace(E_Be_max - 3*sigma_Be, E_Be_max + 3*sigma_Be, 1000)
y4 = 0.1 * A * np.exp(-0.5 * ((x4 - E_Be_max) / sigma_Be*1.5)**2)

plt.figure()
#plt.plot([E_Be_max, E_Be_max], [0, 15], linewidth=2, color = 'orangered')
plt.plot(x4, y4, linewidth=2, color = 'red')
plt.plot(x2, y3, linewidth=2, color = 'red')
plt.text(1/8, 7/12 - 0.05, r'$\alpha_1 (Be)$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.text(1/16-0.035, 1/6 - 0.05, r'$\alpha_0 (Be)$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()

## Together1
x_total = np.linspace(0, 8, 10000)
y_total = A * np.exp(-0.5 * ((x_total - E_alpha_exc_mean) / sigma_alpha)**2
            ) + 0.6 * A * np.exp(-0.5 * ((x_total - E_Be_exc_mean) / sigma_Be*0.8)**2
            ) + 0.1 * A * np.exp(-0.5 * ((x_total - E_Be_max) / sigma_Be*1.5)**2
            ) + 0.15 * A * np.exp(-0.5 * ((x_total - E_alpha_max) / 0.05)**2)

plt.figure()
plt.plot([E_alpha_max, E_alpha_max], [0, 15], linewidth=2, color = 'dodgerblue')
plt.plot(x1, y1, linewidth=2, color = 'dodgerblue', label='Primary Alpha')
plt.plot(x4, y4, linewidth=2, color = 'red')
plt.plot(x2, y3, linewidth=2, color = 'red', label='Secondary Alpha')
plt.plot(x_total, y_total, linewidth=2, color = 'purple', label='Total spectrum')
plt.legend()
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()  

## Together2
y_total2 = A * np.exp(-0.5 * ((x_total - E_alpha_exc_mean) / sigma_alpha)**2
            ) + 0.6 * A * np.exp(-0.5 * ((x_total - E_Be_exc_mean) / sigma_Be*0.8)**2
            ) + 0.1 * A * np.exp(-0.5 * ((x_total - E_Be_max) / sigma_Be*1.5)**2
            ) + 0.15 * A * np.exp(-0.5 * ((x_total - E_alpha_max) / 0.05)**2
            ) + 5 * A * np.exp(-0.5 * ((x_total - 0.675) / 0.3)**2
            ) + 2.5 * A * np.exp(-0.5 * ((x_total - 1.35) / 0.3)**2)
    
y_exp = A * np.exp(-0.5 * ((x_total - E_alpha_exc_mean) / sigma_alpha)**2
            ) + 0.6 * A * np.exp(-0.5 * ((x_total - E_Be_exc_mean) / sigma_Be*0.8)**2
            ) + 0.1 * A * np.exp(-0.5 * ((x_total - E_Be_max) / sigma_Be*1.5)**2
            ) + 0.15 * A * np.exp(-0.5 * ((x_total - E_alpha_max) / 0.05)**2
            ) + 5 * A * skewnorm(-2, 0.675, 0.4).pdf(x_total) + 0.01 * A * skewnorm(-2, 1.35, 0.4).pdf(x_total)

plt.figure()
plt.plot([E_alpha_max, E_alpha_max], [0, 15], linewidth=2, color = 'dodgerblue')
plt.plot(x1, y1, linewidth=2, color = 'dodgerblue', label='Primary Alpha')
plt.plot(x4, y4, linewidth=2, color = 'red')
plt.plot(x2, y3, linewidth=2, color = 'red', label='Secondary Alpha')
plt.plot(x2, 5 * A * np.exp(-0.5 * ((x2 - 0.675) / 0.3)**2), linewidth=2, color = 'forestgreen', label='Backscattering')
plt.plot(x2, 2.5 * A * np.exp(-0.5 * ((x2 - 1.35) / 0.3)**2), linewidth=2, color = 'darkorange', label='Pile Up')
plt.plot(x_total, y_total2, linewidth=2, color = 'purple', label='Total spectrum')
plt.plot(x_total, y_exp, linewidth=2, color = 'black', label='Experimental spectrum')
plt.legend()
plt.xlim(0, 8)
plt.ylim(0, 750)
plt.xlabel("Energy (MeV)")
plt.show()

###########################################################################################################################
#################################################### 2ª Energia ###########################################################
###########################################################################################################################

"""
Energia do protão = 0.805 MeV
Energia alpha máxima (estado fundamental):
5.581847526020704
Energia alpha estado excitado central:
3.6781676020628846
Energia alpha estado excitado minima:
4.038559836183839
Energia alpha estado excitado maxima:
3.318874395267524

Energia berilio máxima (estado fundamental):
1.2423567203049317
Energia berilio estado excitado central:
0.7950510878795073
Energia berilio estado excitado minima:
0.7114694290804404
Energia berilio estado excitado maxima:
0.8792054880596525
"""

E_alpha_max_2 = 5.581847526020704
E_alpha_exc_mean_2 = 3.6781676020628846
E_alpha_exc_min_2 = 3.318874395267524
E_alpha_exc_max_2 = 4.038559836183839

E_Be_max_2 = 1.2423567203049317
E_Be_exc_mean_2 = 0.7950510878795073
E_Be_exc_min_2 = 0.7114694290804404
E_Be_exc_max_2 = 0.8792054880596525

## Alpha 1
plt.figure()
plt.plot([E_alpha_max_2, E_alpha_max_2], [0, 15], linewidth=2, color = 'dodgerblue')
plt.plot([E_alpha_exc_mean_2, E_alpha_exc_mean_2], [0, 100], linewidth=2, color = 'dodgerblue')
plt.text(0.47, 21/24, r'$\alpha_1$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.text(0.7, 1/6, r'$\alpha_0$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.gca().set_yticklabels([])
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()

## Alpha 2
sigma_alpha_2 = 0.75*(E_alpha_exc_max_2 - E_alpha_exc_min_2)
x1_2 = np.linspace(E_alpha_exc_mean_2 - 3 * sigma_alpha_2, E_alpha_exc_mean_2 + 3 * sigma_alpha_2, 1000)
y1_2 = A * np.exp(-0.5 * ((x1 - E_alpha_exc_mean_2) / sigma_alpha_2)**2)

plt.figure()
plt.plot([E_alpha_max_2, E_alpha_max_2], [0, 15], linewidth=2, color = 'dodgerblue')
plt.plot(x1_2, y1_2, linewidth=2, color = 'dodgerblue')
plt.text(0.47, 21/24, r'$\alpha_1$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.text(0.7, 1/6, r'$\alpha_0$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.gca().set_yticklabels([])
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()

## Berilium 1
plt.figure()
plt.plot([E_Be_max_2, E_Be_max_2], [0, 10], linewidth=2, color = 'red')
plt.plot([E_Be_exc_mean_2, E_Be_exc_mean_2], [0, 60], linewidth=2, color = 'red')
plt.text(1/8-0.01, 7/12 - 0.05, r'$\alpha_1 (Be)$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.text(3/16, 1/6 - 0.05, r'$\alpha_0 (Be)$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.gca().set_yticklabels([])
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()

## Berilium 2
sigma_Be_2 = (E_Be_exc_max_2 - E_Be_exc_min_2)*2
x2_2 = np.linspace(E_Be_exc_mean_2 - 3 * sigma_Be_2, E_Be_exc_mean_2 + 3 * sigma_Be_2, 1000)
y3_2 = 0.6 * A * np.exp(-0.5 * ((x2_2 - E_Be_exc_mean_2) / sigma_Be_2*0.8)**2)
x4_2 = np.linspace(E_Be_max_2 - 3*sigma_Be_2, E_Be_max_2 + 3*sigma_Be_2, 1000)
y4_2 = 0.1 * A * np.exp(-0.5 * ((x4_2 - E_Be_max_2) / sigma_Be_2*1.5)**2)

plt.figure()
plt.plot(x4_2, y4_2, linewidth=2, color = 'red')
plt.plot(x2_2, y3_2, linewidth=2, color = 'red')
plt.text(1/8, 7/12 - 0.05, r'$\alpha_1 (Be)$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.text(1/16-0.035, 1/6 - 0.05, r'$\alpha_0 (Be)$', transform = plt.gca().transAxes, color='black', fontsize=17)
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()

## Together1
y_total_2 = A * np.exp(-0.5 * ((x_total - E_alpha_exc_mean_2) / sigma_alpha_2)**2
            ) + 0.6 * A * np.exp(-0.5 * ((x_total - E_Be_exc_mean_2) / sigma_Be_2*0.8)**2
            ) + 0.1 * A * np.exp(-0.5 * ((x_total - E_Be_max_2) / sigma_Be_2*1.5)**2
            ) + 0.15 * A * np.exp(-0.5 * ((x_total - E_alpha_max_2) / 0.05)**2)

plt.figure()
plt.plot([E_alpha_max_2, E_alpha_max_2], [0, 15], linewidth=2, color = 'dodgerblue')
plt.plot(x1_2, y1_2, linewidth=2, color = 'dodgerblue', label='Primary Alpha')
plt.plot(x4_2, y4_2, linewidth=2, color = 'red')
plt.plot(x2_2, y3_2, linewidth=2, color = 'red', label='Secondary Alpha')
plt.plot(x_total, y_total_2, linewidth=2, color = 'purple', label='Total spectrum')
plt.legend()
plt.xlim(0, 8)
plt.ylim(0, 120)
plt.xlabel("Energy (MeV)")
plt.show()  

## Together2
y_total2_2 = A * np.exp(-0.5 * ((x_total - E_alpha_exc_mean_2) / sigma_alpha_2)**2
            ) + 0.6 * A * np.exp(-0.5 * ((x_total - E_Be_exc_mean_2) / sigma_Be_2*0.8)**2
            ) + 0.1 * A * np.exp(-0.5 * ((x_total - E_Be_max_2) / sigma_Be_2*1.5)**2
            ) + 0.15 * A * np.exp(-0.5 * ((x_total - E_alpha_max_2) / 0.05)**2
            ) + 5 * A * np.exp(-0.5 * ((x_total - 0.675) / 0.3)**2
            ) + 2.5 * A * np.exp(-0.5 * ((x_total - 1.35) / 0.3)**2)

plt.figure()
plt.plot([E_alpha_max_2, E_alpha_max_2], [0, 15], linewidth=2, color = 'dodgerblue')
plt.plot(x1_2, y1_2, linewidth=2, color = 'dodgerblue', label='Primary Alpha')
plt.plot(x4_2, y4_2, linewidth=2, color = 'red')
plt.plot(x2_2, y3_2, linewidth=2, color = 'red', label='Secondary Alpha')
plt.plot(x2_2, 5 * A * np.exp(-0.5 * ((x2_2 - 0.675) / 0.3)**2), linewidth=2, color = 'forestgreen', label='Backscattering')
plt.plot(x2_2, 2.5 * A * np.exp(-0.5 * ((x2_2 - 1.35) / 0.3)**2), linewidth=2, color = 'darkorange', label='Pile Up')
plt.plot(x_total, y_total2_2, linewidth=2, color = 'purple', label='Total spectrum')
plt.legend()
plt.xlim(0, 8)
plt.ylim(0, 750)
plt.xlabel("Energy (MeV)")
plt.show()
