import numpy as np

# Number of samples
n_samples = 100

# Adjusting the parameters based on the architectural style
height = np.zeros(n_samples)
width = np.zeros(n_samples)
height_to_width_ratio = np.zeros(n_samples)
num_windows = np.zeros(n_samples, dtype=int)
columns = np.zeros(n_samples, dtype=int)
symmetry = np.zeros(n_samples)
decorative_elements = np.zeros(n_samples)
styles = np.chararray(n_samples, itemsize=20)  # For storing the styles

for i in range(n_samples):
    style = np.random.choice(['Gothic', 'Baroque', 'Neoclassical'])
    styles[i] = style

    if style == 'Gothic':
        height[i] = np.random.normal(20, 5)  # Gothic: Height 20m
        width[i] = np.random.normal(12, 3)   # Gothic: Average width
        num_windows[i] = np.random.randint(15, 30)  # Many narrow windows
        columns[i] = np.random.choice([0, 1])  # Few columns
        symmetry[i] = np.random.uniform(0.8, 1)  # High symmetry
        decorative_elements[i] = np.random.uniform(10, 40)  # Less decoration

    elif style == 'Baroque':
        height[i] = np.random.normal(25, 7)  # Baroque: Height 25m
        width[i] = np.random.normal(15, 4)   # Baroque: Wider facades
        num_windows[i] = np.random.randint(20, 50)  # Many large windows
        columns[i] = np.random.choice([1, 1])  # Many thick columns
        symmetry[i] = np.random.uniform(0.5, 0.7)  # Moderate symmetry
        decorative_elements[i] = np.random.uniform(50, 90)  # High decoration
    else:  # Neoclassical
        height[i] = np.random.normal(18, 4)  # Neoclassical: Height 18m
        width[i] = np.random.normal(14, 3)   # Neoclassical: Balanced proportions
        num_windows[i] = np.random.randint(10, 25)  # Medium-sized windows
        columns[i] = np.random.choice([1, 1])  # Symmetrical columns
        symmetry[i] = np.random.uniform(0.7, 1)  # High symmetry
        decorative_elements[i] = np.random.uniform(10, 30)  # More sober decoration

    # Calculating the height-to-width ratio
    height_to_width_ratio[i] = height[i] / width[i]

# Stack the arrays into one matrix
data = np.column_stack((height, width, height_to_width_ratio, num_windows, columns, symmetry, decorative_elements, styles))

# Save the data into a CSV file
header = 'Height (m),Width (m),Height-to-Width Ratio,Number of Windows,Columns,Symmetry,Decorative Elements (%),Architectural Style'
np.savetxt('historical_facades.csv', data, delimiter=',', header=header, fmt='%s', comments='')

print("CSV generated successfully: 'historical_facades.csv'")
