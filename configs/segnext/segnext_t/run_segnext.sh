bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_t/deeplabv3plus_r50-d8_512x512_20k_voc12full.py 2 --work-dir work-dirs/segnext_t/voc_full
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_t/deeplabv3plus_r50-d8_512x512_20k_kvasir.py 2 --work-dir work-dirs/segnext_t/kvasir
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_t/deeplabv3plus_r50-d8_512x512_20k_kitty7.py 2 --work-dir work-dirs/segnext_t/kitty7
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_t/deeplabv3plus_r50-d8_512x512_20k_kitty.py 2 --work-dir work-dirs/segnext_t/kitty_full
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_t/deeplabv3plus_r50-d8_512x512_20k_dis5k.py 2 --work-dir work-dirs/segnext_t/dis5k
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_t/deeplabv3plus_r50-d8_512x512_20k_cityscapes_half.py 2 --work-dir work-dirs/segnext_t/cityscapes_half
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/segnext/segnext_t/deeplabv3plus_r50-d8_512x512_20k_city_4.py 2 --work-dir work-dirs/segnext_t/city_4