# optimizer
optimizer = dict(type='SGD', lr=0.01, weight_decay=1e-4)
optimizer_config = dict()
# learning policy
lr_config = dict(policy='poly', power=0.9, min_lr=1e-5, by_epoch=False)
# runtime settings
runner = dict(type='EpochBasedRunner', max_epochs=100)
checkpoint_config = dict(by_epoch=True, interval=100)
evaluation = dict(interval=1, metric=['mIoU', 'mDice'], pre_eval=True)
