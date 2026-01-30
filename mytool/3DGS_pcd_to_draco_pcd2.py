import sys
import os
from pathlib import Path
from argparse import ArgumentParser

# Add parent directory to path so 'submodules' can be found
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from submodules.GSInterface import io_3dgs

if __name__ == "__main__":

    parser = ArgumentParser(description="Change binary 3DGS to ASCII pcd")
    parser.add_argument('--inputPath', '-i', required=True, type=str)
    parser.add_argument('--outputPath', '-o', required=True, type=str)
    args = parser.parse_args()

    in_ply_file = args.inputPath
    out_ply_file = args.outputPath

    if not os.path.exists(out_ply_file):
        os.makedirs(os.path.dirname(out_ply_file), exist_ok=True)

    gs_ply = io_3dgs.GaussianModelV2(in_ply_file)
    print(f"Loaded {gs_ply.num_of_point} points")

    gs_ply.export_gs_to_ply(out_ply_file, ascii=True)
    print(f"Exported {gs_ply.num_of_point} points to {out_ply_file}")

    print("Done!")

'''
Usage:
python mytool/3DGS_pcd_to_draco_pcd2.py -i /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/ply/point_cloud_29999.ply -o /home/rajrup/Project/LiVoGS/gsplat/results/actorshq_l1_0.5_ssim_0.5_alpha_1.0/Actor01/Sequence1/4x/0/draco_ply/point_cloud_29999.ply
'''