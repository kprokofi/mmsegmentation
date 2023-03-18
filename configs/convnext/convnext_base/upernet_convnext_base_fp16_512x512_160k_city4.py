_base_ = [
    '../_base_/models/upernet_convnext.py', '../_base_/datasets/city4.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_20k.py'
]
crop_size = (512, 512)
model = dict(
    decode_head=dict(in_channels=[128, 256, 512, 1024], num_classes=4),
    auxiliary_head=dict(in_channels=512, num_classes=4),
    test_cfg=dict(mode='slide', crop_size=crop_size, stride=(341, 341)),
)

# By default, models are trained on 8 GPUs with 2 images per GPU
data = dict(samples_per_gpu=4)

