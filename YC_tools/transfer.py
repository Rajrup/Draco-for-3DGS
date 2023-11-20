from plyfile import PlyData, PlyElement
import numpy as np

def convert_binary_to_ascii(input_file, output_file):
    # Load the binary PLY file
    ply_data = PlyData.read(input_file)

    # Create lists to hold ASCII data
    ascii_elements = []

    # Iterate over elements
    for element in ply_data.elements:
        ascii_data = []
        for prop in element.properties:
            # Convert the binary data to numpy array
            prop_data = np.array(ply_data[element.name][prop.name])
            ascii_data.append(prop_data)
        ascii_elements.append(PlyElement.describe(ascii_data, element.name))

    # Write the ASCII PLY file
    ascii_ply = PlyData(ascii_elements)
    ascii_ply.write(output_file)

# Replace 'input_binary.ply' and 'output_ascii.ply' with your file names
convert_binary_to_ascii('../mytest/test_out.ply', '../mytest/out_ascii.ply')