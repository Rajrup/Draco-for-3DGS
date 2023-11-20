import os
import subprocess

for qp_value in [1, 2, 4, 8, 16, 30]:
    os.system(f"../build_dir/draco_encoder -point_cloud \
                -i ../mytest/in.ply \
                -o ../mytest/out_{qp_value}.drc \
                -qp {qp_value} -qt {qp_value} -qn {qp_value} -qg {qp_value}")
    os.system(f"../build_dir/draco_decoder \
                -i ../mytest/out_{qp_value}.drc \
                -o ../mytest/out_{qp_value}.ply")
