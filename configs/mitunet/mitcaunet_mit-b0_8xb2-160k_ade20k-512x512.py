_base_ = [
    '../_base_/models/segformer_mit-b0.py', '../_base_/datasets/ade20k.py', #'../../_base_/models/segformer_mit-b0_new.py'
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_160k.py'
]
#load_from = "checkpoints/segmentation/feedformer/ade20k/B0/iter_16000_wo.pth"
randomness = dict(seed=0) #seed setup
crop_size = (512, 512)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    pretrained='checkpoints/classification/mit_b0.pth',
    decode_head=dict(
        type='CrossAttentionUNetHead5',
        feature_strides=[4, 8, 16, 32],
        # in_channels=[32, 64, 160, 256],
        # in_index=[0, 1, 2, 3],
        # channels=128,
        dropout_ratio=0.1,
        channels=512, # num channels of very last features before #classes get predicted
        num_classes=150
    )
)

optim_wrapper = dict(
    _delete_=True,
    type='OptimWrapper',
    optimizer=dict(
        type='AdamW', lr=0.00006, betas=(0.9, 0.999), weight_decay=0.01),
    paramwise_cfg=dict(
        custom_keys={
            'pos_block': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.),
            'head': dict(lr_mult=10.)
        }))

param_scheduler = [
    dict(
        type='LinearLR', start_factor=1e-6, by_epoch=False, begin=0, end=1500),
    dict(
        type='PolyLR', #check CosineAnnealingLR: https://github.com/open-mmlab/mmengine/blob/04b0ffee76c41d10c5fd1f737cdc5306af365754/mmengine/optim/scheduler/lr_scheduler.py#L48
        eta_min=0.0,
        power=1.0,
        begin=1500,
        end=160000,
        by_epoch=False,
    )
]
train_dataloader = dict(batch_size=16, num_workers=4) # Set to 1 cause SeulKi trains on same server
val_dataloader = dict(batch_size=1, num_workers=4)
test_dataloader = val_dataloader
