from plyfile import PlyData

def read_binary_ply(file_path):
    with open(file_path, 'rb') as f:
        plydata = PlyData.read(f)
    return plydata

# Replace 'input_binary.ply' with the path to your PLY file
ply_data = read_binary_ply('../mytest/test_out.ply')

# Access elements and their properties
for element in ply_data.elements:
    print(f"Element name: {element.name}")
    for prop in element.properties:
        print(f"Property name: {prop.name}, data type: {prop.dtype}")
        # Access property data using plydata[element.name][prop.name]
        property_data = ply_data[element.name][prop.name]
        print(f"Values:")
        print(property_data)
