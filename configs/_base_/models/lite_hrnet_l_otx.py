norm_cfg = dict(type='SyncBN', requires_grad=True)
model = dict(
    type='EncoderDecoder',
    pretrained="https://storage.openvinotoolkit.org/repositories/openvino_training_extensions/models/custom_semantic_segmentation/litehrnetxv3_imagenet1k_rsc.pth",
    backbone=dict(
        type="LiteHRNet",
        norm_cfg=norm_cfg,
        norm_eval=False,
        extra=dict(
            stem=dict(
                stem_channels=60,
                out_channels=60,
                expand_ratio=1,
                strides=(2, 1),
                extra_stride=False,
                input_norm=False,
            ),
            num_stages=4,
            stages_spec=dict(
                weighting_module_version="v1",
                num_modules=(2, 4, 4, 2),
                num_branches=(2, 3, 4, 5),
                num_blocks=(2, 2, 2, 2),
                module_type=("LITE", "LITE", "LITE", "LITE"),
                with_fuse=(True, True, True, True),
                reduce_ratios=(2, 4, 8, 8),
                num_channels=(
                    (18, 60),
                    (18, 60, 80),
                    (18, 60, 80, 160),
                    (18, 60, 80, 160, 320),
                ),
            ),
            out_modules=dict(
                conv=dict(enable=False, channels=320),
                position_att=dict(
                    enable=False,
                    key_channels=128,
                    value_channels=320,
                    psp_size=(1, 3, 6, 8),
                ),
                local_att=dict(enable=False),
            ),
            out_aggregator=dict(enable=False),
            add_input=False,
        ),
    ),
    decode_head=dict(
        type="FCNHead",
        in_channels=[18, 60, 80, 160, 320],
        in_index=(0, 1, 2, 3, 4),
        input_transform="resize_concat",
        channels=60,
        kernel_size=1,
        num_convs=1,
        concat_input=False,
        dropout_ratio=-1,
        num_classes=2,
        norm_cfg=norm_cfg,
        align_corners=False,
        loss_decode=[
            dict(
                type="CrossEntropyLoss",
                use_sigmoid=False,
                loss_weight=1.0,
            ),
        ],
    ),
    # model training and testing settings
    train_cfg=dict(),
    test_cfg=dict(mode='slide', crop_size=(512,512), stride=(341, 341))
)