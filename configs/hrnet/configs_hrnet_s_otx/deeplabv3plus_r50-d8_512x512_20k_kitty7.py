_base_ = [
    '../../_base_/models/lite_hrnet_s_otx.py',
    '../../_base_/datasets/kitty7.py',
    '../../_base_/schedules/schedule_20k.py'
]
model = dict(decode_head=dict(num_classes=7))
lr_config = dict(warmup_iters=360)
