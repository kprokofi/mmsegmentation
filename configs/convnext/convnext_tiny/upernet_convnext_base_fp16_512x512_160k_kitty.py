_base_ = [
    '../../_base_/models/upernet_convnext.py', '../../_base_/datasets/kitty.py',
    '../../_base_/default_runtime.py', '../../_base_/schedules/schedule_20k.py'
]
crop_size = (512, 512)
checkpoint_file = 'https://download.openmmlab.com/mmclassification/v0/convnext/downstream/convnext-tiny_3rdparty_32xb128-noema_in1k_20220301-795e9634.pth'  # noqa
model = dict(
    backbone=dict(
        type='mmcls.ConvNeXt',
        arch='tiny',
        out_indices=[0, 1, 2, 3],
        drop_path_rate=0.4,
        layer_scale_init_value=1.0,
        gap_before_final_norm=False,
        init_cfg=dict(
            type='Pretrained', checkpoint=checkpoint_file,
            prefix='backbone.')),
    decode_head=dict(
        in_channels=[96, 192, 384, 768],
        num_classes=19,
    ),
    auxiliary_head=dict(in_channels=384, num_classes=19),
    test_cfg=dict(mode='slide', crop_size=crop_size, stride=(341, 341)),
)

# By default, models are trained on 8 GPUs with 2 images per GPU
data = dict(samples_per_gpu=4)
lr_config = dict(warmup_iters=360)

