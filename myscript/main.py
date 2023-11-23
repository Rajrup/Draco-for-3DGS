import os
import subprocess
import itertools
from pathlib import Path

scene_name = "penny"
input_dir = Path("..")/"expData"/"draco_input"/scene_name
save_drc_dir = Path("..")/"expData"/"draco_output_drc"/scene_name
save_drc_dir.mkdir(parents=True, exist_ok=True)
save_ply_dir = Path("..")/"expData"/"draco_output_ply"/scene_name
save_ply_dir.mkdir(parents=True, exist_ok=True)
save_log_dir = Path("..")/"expData"/"draco_log"/scene_name
save_log_dir.mkdir(parents=True, exist_ok=True)

numToCal = 1

qp_values = [16]
qn_values = [16] # normal don't change this
qfd_values = qfr_values = qo_values = [16]
qs_values = qr_values = [1]
cl_values = [3, 5, 7, 9]

qt_values = [0] # unuse
qg_values = [0] # unuse



    # for qp_value in qp_values:
    #     for qn_value in qn_values:
    #         for qfd_value in qfd_values:
    #             for qfr_value in qfr_values:
    #                 for qo_value in qo_values:
    #                     for qs_value in qs_values:
    #                         for qr_value in qr_values:
    

for i in range(numToCal):
    for values_combo in itertools.product(qp_values, qn_values, qfd_values, qfr_values, qo_values, qs_values, qr_values, cl_values):
        qp_value, qn_value, qfd_value, qfr_value, qo_value, qs_value, qr_value, cl_value = values_combo
        suffix = f"qp{qp_value}_qn{qn_value}_qfd{qfd_value}_qfr{qfr_value}_qo{qo_value}_qs{qs_value}_qr{qr_value}_cl{cl_value}"
        
        os.system(f"../build_dir/draco_encoder -point_cloud \
                    -i {input_dir}/point_cloud.ply \
                    -o {save_drc_dir}/{scene_name}_{suffix}.drc \
                    -qp {qp_value} -qn {qn_value} \
                    -qfd {qfd_value} -qfr {qfr_value} -qo {qo_value} \
                    -qs {qs_value} -qr {qr_value} \
                    -cl {cl_value} \
                    > {save_log_dir}/encode_{suffix}_{i}.log")

        os.system(f"../build_dir/draco_decoder \
                    -i {str(save_drc_dir)}/{scene_name}_{suffix}.drc \
                    -o {str(save_ply_dir)}/{scene_name}_{suffix}.ply \
                    > {save_log_dir}/decode_{suffix}_{i}.log")

