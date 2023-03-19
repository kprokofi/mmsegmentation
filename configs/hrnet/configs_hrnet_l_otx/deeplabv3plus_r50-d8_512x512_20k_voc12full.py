_base_ = [
    '../../_base_/models/lite_hrnet_l_otx.py',
    '../../_base_/datasets/pascal_voc12.py', '../../_base_/default_runtime.py',
    '../../_base_/schedules/schedule_20k.py'
]
model = dict(decode_head=dict(num_classes=21))
