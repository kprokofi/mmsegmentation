_base_ = [
    '../../_base_/models/deeplabv3plus_r50-d8.py',
    '../../_base_/datasets/cityscapes_half.py', '../../_base_/default_runtime.py',
    '../../_base_/schedules/schedule_20k.py'
]
model = dict(
    pretrained='/home/kprokofi/datasets/resnet50_v1c.pth',
    decode_head=dict(num_classes=19), auxiliary_head=dict(num_classes=19))
