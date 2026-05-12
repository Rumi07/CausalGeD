python main.py \
    --document dataset-HBC \
    --device cuda:0 \
    --batch_size 64 \
    --hidden_size 1024 \
    --epoch 4000 \
    --diffusion_step 2000 \
    --learning_rate 3e-6 \
    --depth 4 \
    --noise_std 10 \
    --pca_dim 100 \
    --head 16 \
    --mask_nonzero_ratio 0.1 \
    --mask_zero_ratio 0.3 \
    --vae_sig 1 \
    --decoder_train 1 \
    --ar_step_decay 0.8 > dataset_hbc_run.log
   
   
