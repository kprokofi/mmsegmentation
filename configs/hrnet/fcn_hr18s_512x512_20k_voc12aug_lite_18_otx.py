_base_ = './fcn_hr18_512x512_20k_voc12aug.py'
model = dict(
    pretrained='https://storage.openvinotoolkit.org/repositories/openvino_training_extensions/models/custom_semantic_segmentation/litehrnet18_imagenet1k_rsc.pth',
    backbone=dict(
        type='LiteHRNet',
        extra=dict(
            stem=dict(
                stem_channels=32,
                out_channels=32,
                expand_ratio=1,
                strides=(2, 2),
                extra_stride=False,
                input_norm=False),
            num_stages=3,
            stages_spec=dict(
                num_modules=(2, 4, 2),
                num_branches=(2, 3, 4),
                num_blocks=(2, 2, 2),
                module_type=('LITE', 'LITE', 'LITE'),
                with_fuse=(True, True, True),
                reduce_ratios=(8, 8, 8),
                num_channels=((40, 80), (40, 80, 160), (40, 80, 160, 320))),
            out_modules=dict(
                conv=dict(enable=False, channels=320),
                position_att=dict(
                    enable=False,
                    key_channels=128,
                    value_channels=320,
                    psp_size=(1, 3, 6, 8)),
                local_att=dict(enable=False)),
            out_aggregator=dict(enable=False),
            add_input=False)),
    decode_head=dict(
            type='FCNHead',
            in_channels=[40, 80, 160, 320],
            channels=sum([40, 80, 160, 320]),
            dropout_ratio=0.1,
            num_classes=21))
