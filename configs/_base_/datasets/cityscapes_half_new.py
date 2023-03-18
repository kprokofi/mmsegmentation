dataset_type='CityscapesHalf'
data_root='data/citiscapes_semisl'

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
crop_size = (512, 512)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='TrainPre', config=dict(img_mean=img_norm_cfg["mean"],
                                      img_std=img_norm_cfg["std"],
                                      train_scale_array=[0.5, 0.75, 1, 1.5, 1.75, 2.0],
                                      image_height=512,
                                      image_width=512)),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        flip=False,
        img_scale=(512, 512),
        transforms=[
            dict(type='ValPre', config=dict(img_mean=img_norm_cfg["mean"],
                                      img_std=img_norm_cfg["std"],
                                      train_scale_array=[0.5, 0.75, 1, 1.5, 1.75, 2.0],
                                      image_height=512,
                                      image_width=512)),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]

data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='train_set/images',
        ann_dir='train_set/masks',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='val_set/images',
        ann_dir='val_set/masks',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='val_set/images',
        ann_dir='val_set/images',
        pipeline=test_pipeline))
