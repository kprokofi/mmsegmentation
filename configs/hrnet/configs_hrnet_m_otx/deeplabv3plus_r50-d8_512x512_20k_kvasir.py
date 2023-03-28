_base_ = [
    '../../_base_/models/lite_hrnet_m_otx.py',
    '../../_base_/datasets/kvasir.py',
    '../../_base_/schedules/schedule_20k.py'
]
model = dict(decode_head=dict(num_classes=2))
lr_config = dict(warmup_iters=260)
