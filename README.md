# Draco for 3D Gaussian Splatting

This is a variant of [Google Draco Compression](https://google.github.io/draco/) to support [original 3D Gaussian splatting (3DGS)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) content.

Draco is an open-source library for compressing and decompressing 3D geometric meshes and point clouds. It is intended to improve the storage and transmission of 3D graphics.

However, this project is only focused on encode and decode 3DGS, so compressing 3D meshes or 3D point cloud is not supported.

## Build
### Build in Linux (Ubuntu)
```bash
mkdir build_dir && cd build_dir
cmake ../
make
```

## Usage
**[!] You should change the 3DGS data to ASCII format before you encode.**

## Change binary format to ASCII format
```bash
python ./mytool/3DGS_pcd_to_draco_pcd.py -i ./myData/ficus.ply -o ./myData/ficus_3dgs.ply
```

## Encode
### Simple
```bash
./build_dir/draco_encoder -point_cloud \
-i ./myData/ficus_3dgs.ply \
-o ./myData/ficus_3dgs_compressed.drc
```

### More complex setup
```bash
./build_dir/draco_encoder -point_cloud \
-i ./myData/ficus_3dgs.ply \
-o ./myData/ficus_3dgs_compressed.drc \
-qp 16 \
-qfd 16 -qfr1 16 -qfr2 16 -qfr3 16 \
-qo 16 \
-qs 16 -qr 16 \
-cl 10
```

## Decode
```bash
./build_dir/draco_decoder \
-i ./myData/ficus_3dgs_compress.drc \
-o ./myData/ficus_3dgs_distorted.ply
```

# For Experiment
## Encode (Using my_encode.py and json file)
```bash
python my_encoder.py -jp ../myJson/template_sh0.json
```

## Decode (Using my_decode.py and json file)
```bash
python my_decoder.py -jp ../myJson/template.json
```

## Configuration json file
Based on the template json file at `myJson/template.json`


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

<!-- ## License

[MIT](https://choosealicense.com/licenses/mit/) -->
