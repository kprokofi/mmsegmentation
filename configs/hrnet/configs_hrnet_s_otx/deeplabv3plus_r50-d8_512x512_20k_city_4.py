_base_ = [
    '../../_base_/models/lite_hrnet_s_otx.py',
    '../../_base_/datasets/city_4.py',
    '../../_base_/schedules/schedule_20k_old.py'
]
model = dict(decode_head=dict(num_classes=4))
lr_config = dict(warmup_iters=120)
