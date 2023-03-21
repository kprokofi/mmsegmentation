bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/configs_resnet_18_otx/deeplabv3plus_r50-d8_512x512_20k_voc12full.py 2 --work-dir work-dirs/resnet18/voc_full_adam
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/configs_resnet_18_otx/deeplabv3plus_r50-d8_512x512_20k_kvasir.py 2 --work-dir work-dirs/resnet18/kvasir_adam
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/configs_resnet_18_otx/deeplabv3plus_r50-d8_512x512_20k_kitty7.py 2 --work-dir work-dirs/resnet18/kitty7_adam
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/configs_resnet_18_otx/deeplabv3plus_r50-d8_512x512_20k_kitty.py 2 --work-dir work-dirs/resnet18/kitty_full_adam
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/configs_resnet_18_otx/deeplabv3plus_r50-d8_512x512_20k_dis5k.py 2 --work-dir work-dirs/resnet18/dis5k_adam
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/configs_resnet_18_otx/deeplabv3plus_r50-d8_512x512_20k_cityscapes_half.py 2 --work-dir work-dirs/resnet18/cityscapes_half_adam
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/configs_resnet_18_otx/deeplabv3plus_r50-d8_512x512_20k_city_4.py 2 --work-dir work-dirs/resnet18/city_4_adam