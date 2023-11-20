from plyfile import PlyData
import numpy as np
import os
from pathlib import Path
import pandas as pd

def read_binary_ply(file_path):
    with open(file_path, 'rb') as f:
        ply_data = PlyData.read(f)
    return ply_data

def read_ascii_ply(file_path):
    ply_data = PlyData.read(file_path)
    return ply_data

def get_file_size(file_path):
    return os.path.getsize(file_path)

def base():
    # Replace 'input_binary.ply' with the path to your PLY file
    ply_data = read_binary_ply('../mytest/out.ply')
    in_ply_data = read_ascii_ply('../mytest/in.ply')
    

    # Access elements and their properties
    out_attribute_name = []
    out_data = []
    for element in ply_data.elements:
        print(f"Element name: {element.name}")
        for prop in element.properties:
            # print(f"Property name: {prop.name}, data type: {prop.dtype}")
            # Access property data using plydata[element.name][prop.name]
            out_attribute_name.append(prop.name)
            property_data = ply_data[element.name][prop.name]
            out_data.append(np.array(property_data))

    # Access elements and their properties
    in_attribute_name = []
    in_data = []
    for element in in_ply_data.elements:
        print(f"Element name: {element.name}")
        for prop in element.properties:
            # print(f"Property name: {prop.name}, data type: {prop.dtype}")
            # Access property data using plydata[element.name][prop.name]
            property_data = in_ply_data[element.name][prop.name]
            in_attribute_name.append(prop.name)
            in_data.append(np.array(property_data))
    results = [(in_item-out_item).mean() for in_item, out_item in zip(in_data, out_data)]
    print(in_attribute_name)
    print(out_attribute_name)
    print(results)

def test_diff_qp(qp_value):
    # Replace 'input_binary.ply' with the path to your PLY file
    in_ply_data = read_ascii_ply('../mytest/in.ply')
    out_ply_data = read_binary_ply(f'../mytest/out_{qp_value}.ply')
    
    in_file_size = get_file_size(f'../mytest/in.ply')
    drc_file_size = get_file_size(f"../mytest/out_{qp_value}.drc")
    out_file_size = get_file_size(f"../mytest/out_{qp_value}.ply")

    # Access elements and their properties
    out_attribute_name = []
    out_data = []
    for element in out_ply_data.elements:
        # print(f"Element name: {element.name}")
        for prop in element.properties:
            # print(f"Property name: {prop.name}, data type: {prop.dtype}")
            # Access property data using plydata[element.name][prop.name]
            out_attribute_name.append(prop.name)
            property_data = out_ply_data[element.name][prop.name]
            out_data.append(np.array(property_data))

    # Access elements and their properties
    in_attribute_name = []
    in_data = []
    for element in in_ply_data.elements:
        # print(f"Element name: {element.name}")
        for prop in element.properties:
            # print(f"Property name: {prop.name}, data type: {prop.dtype}")
            # Access property data using plydata[element.name][prop.name]
            property_data = in_ply_data[element.name][prop.name]
            in_attribute_name.append(prop.name)
            in_data.append(np.array(property_data))
    
    results = [np.absolute(in_item-out_item).mean() for in_item, out_item in zip(in_data, out_data)]
    # print(in_attribute_name)
    # print(out_attribute_name)
    # print(f"qp: {qp_value}")
    # print(results)
    return [qp_value] + results + [in_file_size, drc_file_size, out_file_size]
    

if __name__ == "__main__":
    # base()
    
    # test
    arr = []
    for qp_value in [1, 2, 4, 8, 16, 30, 0]:
        arr.append(test_diff_qp(qp_value))
    
    saveDir = Path("..")/"myresult"
    saveDir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(arr, columns=['qp', 'x', 'y', 'z', \
                                    'nx', 'ny', 'nz', \
                                    'my_nx', 'my_ny', 'my_nz', \
                                    'in_file_size', 'drc_file_size', 'out_file_size'])
    df.to_csv(saveDir/"mytest.csv", index=False)