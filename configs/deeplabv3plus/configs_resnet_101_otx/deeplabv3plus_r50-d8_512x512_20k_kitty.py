_base_ = [
    '../../_base_/models/deeplabv3plus_r50-d8.py',
    '../../_base_/datasets/kitty.py', '../../_base_/default_runtime.py',
    '../../_base_/schedules/schedule_20k.py'
]
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101),  decode_head=dict(num_classes=19), auxiliary_head=dict(num_classes=19))
lr_config = dict(warmup_iters=360)
