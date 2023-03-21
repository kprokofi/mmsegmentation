# optimizer
optimizer = dict(type='AdamW', lr=0.001, betas=(0.9, 0.999), weight_decay=1e-4, paramwise_cfg={'bias_decay_mult ': 0.0, 'norm_decay_mult ': 0.0})
optimizer_config = dict()
# learning policy
lr_config = dict(policy='poly',  warmup='linear',  warmup_iters=260, warmup_ratio=1e-5, power=0.9,  min_lr=1e-6, by_epoch=False)
# runtime settings
runner = dict(type='EpochBasedRunner', max_epochs=100)
checkpoint_config = dict(by_epoch=True, interval=100)
evaluation = dict(interval=1, metric=['mIoU', 'mDice'], pre_eval=True)
