bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_l/deeplabv3plus_r50-d8_512x512_20k_voc12full.py 2 --work-dir work-dirs/segnext_l/voc_full
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_l/deeplabv3plus_r50-d8_512x512_20k_kvasir.py 2 --work-dir work-dirs/segnext_l/kvasir
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_l/deeplabv3plus_r50-d8_512x512_20k_kitty7.py 2 --work-dir work-dirs/segnext_l/kitty7
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_l/deeplabv3plus_r50-d8_512x512_20k_kitty.py 2 --work-dir work-dirs/segnext_l/kitty_full
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_l/deeplabv3plus_r50-d8_512x512_20k_dis5k.py 2 --work-dir work-dirs/segnext_l/dis5k
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_l/deeplabv3plus_r50-d8_512x512_20k_cityscapes_half.py 2 --work-dir work-dirs/segnext_l/cityscapes_half
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_l/deeplabv3plus_r50-d8_512x512_20k_city_4.py 2 --work-dir work-dirs/segnext_l/city_4