# optimizer
optimizer = dict(type='Adam', lr=0.001, weight_decay=0.0)
optimizer_config = dict()
# learning policy
lr_config = dict(policy='poly', power=0.9, min_lr=0, by_epoch=False)
# runtime settings
runner = dict(type='EpochBasedRunner', max_epochs=100)
checkpoint_config = dict(by_epoch=True, interval=100)
evaluation = dict(interval=1, metric=['mIoU', 'mDice'], pre_eval=True)
