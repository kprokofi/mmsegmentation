_base_ = [
    '../../_base_/models/upernet_convnext.py', '../../_base_/datasets/kvasir.py',
    '../../_base_/default_runtime.py', '../../_base_/schedules/schedule_20k_sgd.py'
]
crop_size = (512, 512)
model = dict(
    decode_head=dict(in_channels=[128, 256, 512, 1024], num_classes=2),
    auxiliary_head=dict(in_channels=512, num_classes=2),
    test_cfg=dict(mode='slide', crop_size=crop_size, stride=(341, 341)),
)
optimizer = dict(lr=0.001)

# By default, models are trained on 8 GPUs with 2 images per GPU
data = dict(samples_per_gpu=4)

