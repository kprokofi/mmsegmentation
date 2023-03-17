bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r50-d8_512x512_20k_voc_half.py 2 --work-dir ./work-dirs/resnet_50/VOC_half
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r50-d8_512x512_20k_kitty.py 2 --work-dir ./work-dirs/resnet_50/kitty_full
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r50-d8_512x512_20k_kitty7.py 2 --work-dir ./work-dirs/resnet_50/kitty_7
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r50-d8_512x512_20k_kvasir.py 2 --work-dir ./work-dirs/resnet_50/kvasir
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r50-d8_512x512_20k_city_4.py 2 --work-dir ./work-dirs/resnet_50/city_4
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r50-d8_512x512_20k_cityscapes_half.py 2 --work-dir ./work-dirs/resnet_50/city_half