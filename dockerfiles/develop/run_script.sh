set -x
ROOT_DIR=$(pwd)
nohup ./run_finance.sh > ${ROOT_DIR}/nohup_finance.out &
# nohup ./run_transit.sh > ${ROOT_DIR}/nohup_transit.out &