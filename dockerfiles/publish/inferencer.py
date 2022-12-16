# 내장
import json
import os

# 서드파티
from mmocr.ocr import MMOCR

# 프로젝트
from work_dirs_utils.pkl2json import convert, load_pkl


# 모델은 전역변수로 선언되어야 합니다.
# 1. MMOCR 은 동시에 하나의 모델밖에 실행하지 못합니다.
# 2. 모델이 메모리에서 내려가지 않도록 띄워두기 위함입니다.
OCR = None


def get_model_kwargs(model_name: str) -> dict:
    dbnet_base = 'configs/textdet/dbnet'
    f_dbnet_confname = 'dbnet_resnet18_fpnc_20e_aihubfinance10of100'
    t_dbnet_confname = 'dbnet_resnet18_fpnc_2e_aihubtransit100of100'
    satrn_base = 'configs/textrecog/satrn'
    f_satrn_confname = 'satrn_shallow_5e_aihubfinance10of100_pretrained_lrtune'
    t_satrn_confname = 'satrn_shallow_5e_aihubtransit1of100_pretrained_lrtune'
    model_dict = {
        # Detection models
        'Debug_Det' : {
            'det': 'DB_r18',
        },
        'AihubFinance_DBNet': {
            'det_config': f'{dbnet_base}/{f_dbnet_confname}.py',
            'det_ckpt': f'pretrained/{f_dbnet_confname}_sparkling-cloud-104.pth',
        },
        'AihubTransit_DBNet': {
            'det_config': f'{dbnet_base}/{t_dbnet_confname}.py',
            'det_ckpt': f'pretrained/{t_dbnet_confname}_hopeful-leaf-117.pth',
        },
        # Recognition models
        'Debug_Recog' : {
            'recog': 'SAR',
        },
        'AihubFinance_SATRN': {
            'recog_config': f'{satrn_base}/{f_satrn_confname}.py',
            'recog_ckpt': f'pretrained/{f_satrn_confname}_peachy-sun-152.pth',
        },
        'AihubTransit_SATRN': {
            'recog_config': f'{satrn_base}/{t_satrn_confname}.py',
            'recog_ckpt': f'pretrained/{t_satrn_confname}_desert-sunset-150.pth'
        },
    }
    if model_name not in model_dict:
        raise ValueError(f'Model {model_name} is not supported.')
    else:
        return model_dict[model_name]


def _write_empty_image(input_impath, copy_dir) -> None:
    os.makedirs(copy_dir, exist_ok=True)
    os.system(f'cp {input_impath} {copy_dir}')


def _write_empty_json(path) -> None:
    with open(path, 'w', encoding='UTF-8-sig') as f:
        content = {
            'rec_texts': [],
            'rec_scores': [],
            'det_polygons': [],
        }
        json.dump(content, f, 
                  ensure_ascii=False, 
                  indent=4)


def load_model(domain) -> None:
    
    def _rename(domain, task) -> str:
        DEBUG = ['debug', 'Debug', 'DEBUG']
        FINANCE = ['finance', 'Finance']
        TRANSIT = ['transit', 'Transit']
        DETECTION   = ['det', 'detection']
        RECOGNITION = ['recog', 'recognition']
        if (domain in DEBUG) and (task in DETECTION):
            return 'Debug_Det'
        if (domain in FINANCE) and (task in DETECTION):
            return 'AihubFinance_DBNet'
        if (domain in TRANSIT) and (task in DETECTION):
            return 'AihubTransit_DBNet'
        if (domain in DEBUG) and (task in RECOGNITION):
            return 'Debug_Recog'
        if (domain in FINANCE) and (task in RECOGNITION):
            return 'AihubFinance_SATRN'
        if (domain in TRANSIT) and (task in RECOGNITION):
            return 'AihubTransit_SATRN'

    global OCR
    kwargs = {'device': 'cpu'}
    kwargs.update(get_model_kwargs(model_name=_rename(domain, 'detection')))
    kwargs.update(get_model_kwargs(model_name=_rename(domain, 'recognition')))
    OCR = MMOCR(**kwargs)


def run_inference(input_impath, output_imdir, output_jsonpath) -> str:
    output_pklpath = output_jsonpath.replace('.json', '.pkl')
    kwargs = {'img'          : input_impath,
              'img_out_dir'  : output_imdir,
              'pred_out_file': output_pklpath}
    try:
        OCR.readtext(**kwargs)
        _status = 'Prediction Successed'
    except IndexError:
        print(f'추론값이 비어 있는 이미지입니다: {input_impath}')
        _write_empty_image(input_impath, output_imdir)
        _write_empty_json(output_jsonpath)
        _status = 'Empty prediction'
    else:
        convert(load_pkl(output_pklpath), output_jsonpath)
        _status = 'Successed'
    return _status