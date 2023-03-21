bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/hrnet/rerun/deeplabv3plus_r50-d8_512x512_20k_kvasir_s.py 2 --work-dir work-dirs/hrnet_s/kvasir
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/hrnet/rerun/deeplabv3plus_r50-d8_512x512_20k_kvasir_m.py 2 --work-dir work-dirs/hrnet_m/kvasir
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/hrnet/rerun/deeplabv3plus_r50-d8_512x512_20k_kvasir.py 2 --work-dir work-dirs/hrnet_l/kvasir
bash tools/dist_train.sh /home/kprokofi/mmsegmentation/configs/hrnet/rerun/deeplabv3plus_r50-d8_512x512_20k_kitty7.py 2 --work-dir work-dirs/hrnet_s/kitty7
