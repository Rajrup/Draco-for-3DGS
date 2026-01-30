## Build Draco for 3DGS

```bash
git clone --recursive https://github.com/Rajrup/Draco-for-3DGS.git
cd Draco-for-3DGS

conda activate livogs_cu12
pip install plyfile

mkdir build && cd build
cmake ..
make -j$(nproc)
```

## Run Draco for 3DGS

- Convert 3DGS to Draco Ply format

  - Method 1: Convert 3DGS to Draco Ply format using the script

```bash
python mytool/3DGS_pcd_to_draco_pcd.py -i /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/ply/point_cloud_29999.ply -o /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999.ply
```

  - Method 2: Convert 3DGS to Draco Ply format using the script

```bash
python mytool/3DGS_pcd_to_draco_pcd2.py -i /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/ply/point_cloud_29999.ply -o /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999_2.ply
```

- Encode 3DGS to Draco format

```bash
# Encoder: Default parameters
./build/draco_encoder -point_cloud -i /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999.ply -o /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999_compressed.drc

# Decoder: Default parameters
./build/draco_decoder -i /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999_compressed.drc -o /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999_decompressed.ply
```

```bash
# Encoder: Lossless parameters
./build/draco_encoder -point_cloud -i /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999_2.ply -o /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999_2_compressed_lossless.drc -qp 0 -qfd 0 -qfr1 0 -qfr2 0 -qfr3 0 -qo 0 -qs 0 -qr 0 -cl 10

# Decoder: Default parameters
./build/draco_decoder -i /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999_2_compressed_lossless.drc -o /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999_2_decompressed_lossless.ply
```

Notes:
```
qp: Quantization parameter for position (0 - 31, where 0 is lossless and 31 means 31 bit precision)
qfd: Quantization parameter for SH0 (DC) (0 - 31, where 0 is lossless and 31 means 31 bit precision)
qfr1: Quantization parameter for SH1 (0 - 31, where 0 is lossless and 31 means 31 bit precision)
qfr2: Quantization parameter for SH2 (0 - 31, where 0 is lossless and 31 means 31 bit precision)
qfr3: Quantization parameter for SH3 (0 - 31, where 0 is lossless and 31 means 31 bit precision)
qo: Quantization parameter for opacity (0 - 31, where 0 is lossless and 31 means 31 bit precision)
qs: Quantization parameter for scale (0 - 31, where 0 is lossless and 31 means 31 bit precision)
qr: Quantization parameter for rotation (0 - 31, where 0 is lossless and 31 means 31 bit precision)
cl: Compression level (0 - 10, 10 is fastest)
```