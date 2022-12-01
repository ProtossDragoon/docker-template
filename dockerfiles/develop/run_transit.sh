set -x
CUR_DIR=$(pwd)

LOGFILE_PATH=${CUR_DIR}/e2e_transit.log
T_GT_BASE_DIR=${CUR_DIR}/oss/src_mmocr/data/e2ef1/aihub_transit/part_100of100/test/gts
T_PRED_BASE_DIR=${CUR_DIR}/oss/src_mmocr/data/e2ef1/aihub_transit/part_100of100/test/preds
T_MATRIX_BASE_DIR=${CUR_DIR}/oss/src_mmocr/data/e2ef1/aihub_transit/part_100of100/test/matrix
T_LOGOUTPUT_DIR=${CUR_DIR}/oss/src_mmocr/data/e2ef1/aihub_transit/part_100of100/test
echo "Change directory: $(pwd)"
echo "transit_gt_base_dir: ${T_GT_BASE_DIR}"
echo "transit_pred_base_dir: ${T_PRED_BASE_DIR}"
echo "transit_matrix_base_dir: ${T_MATRIX_BASE_DIR}"

cd oss/src_mmocr
echo "Change directory: $(pwd)"
python3 -m data_utils.copy4e2e aihub_transit --logfile_path ${LOGFILE_PATH}
python3 -m work_dirs_utils.ocr_e2e aihub_transit --logfile_path ${LOGFILE_PATH}
python3 -m work_dirs_utils.mmout2icdar aihub_transit --logfile_path ${LOGFILE_PATH}
cd ${CUR_DIR}

cd oss/OCRE2EHMean
echo "Change directory: $(pwd)"
python3 -m main ${T_GT_BASE_DIR} ${T_PRED_BASE_DIR} ${T_MATRIX_BASE_DIR} --logfile_path ${LOGFILE_PATH}
cd ${CUR_DIR}

cp e2e_transit.log ${T_LOGOUTPUT_DIR}/e2e_transit.log
cp nohup_transit.out ${T_LOGOUTPUT_DIR}/nohup_transit.out