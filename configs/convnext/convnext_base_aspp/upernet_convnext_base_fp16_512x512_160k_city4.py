_base_ = [
    '../../_base_/models/upernet_convnext.py', '../../_base_/datasets/city_4.py',
    '../../_base_/default_runtime.py', '../../_base_/schedules/schedule_20k.py'
]
_num_classes=4
_decode_head_base=dict(
        _delete_=True,
        type='DepthwiseSeparableASPPHead',
        in_channels=1024,
        in_index=3,
        channels=512,
        dilations=(1, 12, 24, 36),
        c1_in_channels=128,
        c1_channels=48,
        dropout_ratio=0.1,
        norm_cfg=dict(type='SyncBN', requires_grad=True),
        align_corners=False,
        num_classes=_num_classes,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0))
crop_size = (512, 512)
model = dict(
    decode_head=_decode_head_base,
    auxiliary_head=dict(in_channels=512, num_classes=_num_classes),
    test_cfg=dict(mode='slide', crop_size=crop_size, stride=(341, 341)),
)


# By default, models are trained on 8 GPUs with 2 images per GPU
data = dict(samples_per_gpu=4)

