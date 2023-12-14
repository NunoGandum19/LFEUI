import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

def reader (name, Chn):
    # Parse the XML data from the file
    tree = ET.parse(name)
    root = tree.getroot()
    # Access spectrum data
    spectrum_data_str = root.find(f".//Spectrum[@id='RadMeasurement-{Chn}_Spectrum-{Chn}']/ChannelData").text
    # Convert the spectrum data string to a vector of data
    spectrum_data_array = np.array([float(value) for value in spectrum_data_str.split()])

    return spectrum_data_array

def plotter (data, title = "Spectrum Data"):
    plt.plot(data)
    plt.yscale("log")  # Set y-axis to logarithmic scale
    plt.xlabel("Channel")
    plt.ylabel("Counts (log scale)")
    plt.title(title)
    plt.show()
    

def plotter_3(data1, data2, data3, title = "Spectrum Data"):
    plt.plot(data1, label = "Ch0")
    plt.plot(data2, label = "Ch1")
    plt.plot(data3, label = "Ch2")
    plt.yscale("log")  # Set y-axis to logarithmic scale
    plt.xlabel("Channel")
    plt.ylabel("Counts (log scale)")
    plt.title(title)
    plt.legend()
    plt.show()


