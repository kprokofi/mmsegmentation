_base_ = [
    '../../_base_/models/lite_hrnet_s_otx.py',
    '../../_base_/datasets/kvasir.py', '../../_base_/default_runtime.py',
    '../../_base_/schedules/schedule_20k.py'
]
lr_config = dict(warmup_iters=260)
model = dict(decode_head=dict(num_classes=2))