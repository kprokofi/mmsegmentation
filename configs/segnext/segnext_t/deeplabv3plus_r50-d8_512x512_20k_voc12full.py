_base_ = [
    '../segnext_base.py',
    '../../_base_/datasets/pascal_voc12.py', '../../_base_/default_runtime.py',
    '../../_base_/schedules/schedule_20k.py'
]
model = dict(
    decode_head=dict(num_classes=21))
lr_config = dict(warmup_iters=3600)
data = dict(samples_per_gpu=4)
optimizer = dict(
    paramwise_cfg=dict(
        custom_keys={
            'pos_block': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.)
        }))