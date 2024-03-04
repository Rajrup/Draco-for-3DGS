# Build
## Build in Linux (Ubuntu)
```bash
mkdir build_dir && cd build_dir
cmake ../
make
```

# Encode
## Simple
```bash
./build_dir/draco_encoder -point_cloud \
-i ./myData/ficus_3dgs.ply \
-o ./myData/ficus_3dgs_compress.drc
```

## More complex setup
```bash
./build_dir/draco_encoder -point_cloud \
-i ./myData/ficus_3dgs.ply \
-o ./myData/ficus_3dgs_compress.drc \
-qp 16 \
-qfd 16 -qfr1 16 -qfr2 16 -qfr3 16 \
-qo 16 \
-qs 16 -qr 16 \
-cl 10
```

# Decode
```bash
./build_dir/draco_decoder \
-i ./myData/ficus_3dgs_compress.drc \
-o ./myData/ficus_3dgs_distorted.ply
```