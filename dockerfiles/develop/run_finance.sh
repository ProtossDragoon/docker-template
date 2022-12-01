set -x
CUR_DIR=$(pwd)

LOGFILE_PATH=${CUR_DIR}/e2e_finance.log
F_GT_BASE_DIR=${CUR_DIR}/oss/src_mmocr/data/e2f1/aihub_finance/part_100of100/test/gts
F_PRED_BASE_DIR=${CUR_DIR}/oss/src_mmocr/data/e2f1/aihub_finance/part_100of100/test/preds
F_MATRIX_BASE_DIR=${CUR_DIR}/oss/src_mmocr/data/e2f1/aihub_finance/part_100of100/test/matrix
F_LOGOUTPUT_DIR=${CUR_DIR}/oss/src_mmocr/data/e2f1/aihub_finance/part_100of100/test
echo "Change directory: $(pwd)"
echo "finance_gt_base_dir: ${F_GT_BASE_DIR}"
echo "finance_pred_base_dir: ${F_PRED_BASE_DIR}"
echo "finance_matrix_base_dir: ${F_MATRIX_BASE_DIR}"

cd oss/src_mmocr
echo "Change directory: $(pwd)"
python3 -m data_utils.copy4e2e aihub_finance --logfile_path ${LOGFILE_PATH} --resize-json
python3 -m work_dirs_utils.ocr_e2e aihub_finance --logfile_path ${LOGFILE_PATH}
python3 -m work_dirs_utils.mmout2icdar aihub_finance --logfile_path ${LOGFILE_PATH}
cd ${CUR_DIR}

cd oss/OCRE2EHMean
echo "Change directory: $(pwd)"
python3 -m main ${F_GT_BASE_DIR} ${F_PRED_BASE_DIR} ${F_MATRIX_BASE_DIR} --logfile_path ${LOGFILE_PATH}
cd ${CUR_DIR}

cp e2e_finance.log ${F_LOGOUTPUT_DIR}/e2e_finance.log
cp nohup_finance.out ${F_LOGOUTPUT_DIR}/nohup_finance.out