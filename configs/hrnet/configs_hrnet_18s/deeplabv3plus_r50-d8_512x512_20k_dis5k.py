_base_ = [
    '../../_base_/models/fcn_hr18.py',
    '../../_base_/datasets/dis5k.py', '../../_base_/default_runtime.py',
    '../../_base_/schedules/schedule_20k_sgd.py'
]
model = dict(decode_head=dict(num_classes=2), pretrained='open-mmlab://msra/hrnetv2_w18_small', backbone=dict(
        extra=dict(
            stage1=dict(num_blocks=(2, )),
            stage2=dict(num_blocks=(2, 2)),
            stage3=dict(num_modules=3, num_blocks=(2, 2, 2)),
            stage4=dict(num_modules=2, num_blocks=(2, 2, 2, 2)))))
