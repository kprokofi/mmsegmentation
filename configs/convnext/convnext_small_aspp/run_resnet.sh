bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/convnext/convnext_small/upernet_convnext_base_fp16_512x512_160k_voc12_full.py 2 --work-dir work-dirs/convnext_small/voc_full
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/convnext/convnext_small/upernet_convnext_base_fp16_512x512_160k_kvasir.py 2 --work-dir work-dirs/convnext_small/kvasir
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/convnext/convnext_small/upernet_convnext_base_fp16_512x512_160k_kitty7.py 2 --work-dir work-dirs/convnext_small/kitty7
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/convnext/convnext_small/upernet_convnext_base_fp16_512x512_160k_kitty.py 2 --work-dir work-dirs/convnext_small/kitty_full
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/convnext/convnext_small/upernet_convnext_base_fp16_512x512_160k_dis5k.py 2 --work-dir work-dirs/convnext_small/dis5k
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/convnext/convnext_small/upernet_convnext_base_fp16_512x512_160k_cityscapes.py 2 --work-dir work-dirs/convnext_small/cityscapes_half
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/convnext/convnext_small/upernet_convnext_base_fp16_512x512_160k_city4.py 2 --work-dir work-dirs/convnext_small/city_4