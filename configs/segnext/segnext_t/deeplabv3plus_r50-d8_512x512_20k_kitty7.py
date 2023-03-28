_base_ = [
    '../segnext_base.py',
    '../../_base_/datasets/kitty7.py', '../../_base_/default_runtime.py',
    '../../_base_/schedules/schedule_20k_old.py'
]
model = dict(
    decode_head=dict(num_classes=7))
lr_config = dict(warmup_iters=360)
data = dict(samples_per_gpu=4)
optimizer = dict(
    paramwise_cfg=dict(
        custom_keys={
            'pos_block': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.)
        }))