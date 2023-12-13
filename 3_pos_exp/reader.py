import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
"""
# Specify the path to your XML file
xml_file_path = "data.n42"

# Parse the XML data from the file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Access spectrum data
spectrum_data_str = root.find(".//Spectrum[@id='RadMeasurement-0_Spectrum-0']/ChannelData").text

# Convert the spectrum data string to a vector of data
spectrum_data_array = np.array([float(value) for value in spectrum_data_str.split()])

# Print the vector
print("Spectrum Data Vector:")
print(spectrum_data_array)

# Plot the spectrum data
plt.plot(spectrum_data_array)
plt.yscale("log")  # Set y-axis to logarithmic scale
plt.xlabel("Channel")
plt.ylabel("Counts (log scale)")
plt.title("Spectrum Data")
plt.show()"""

def reader (name):
    # Parse the XML data from the file
    tree = ET.parse(name)
    root = tree.getroot()
    # Access spectrum data
    spectrum_data_str = root.find(".//Spectrum[@id='RadMeasurement-0_Spectrum-0']/ChannelData").text
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
    




