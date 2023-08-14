# Copyright (c) OpenMMLab. All rights reserved.
from .beit import BEiT
from .bisenetv1 import BiSeNetV1
from .bisenetv2 import BiSeNetV2
from .cgnet import CGNet
from .erfnet import ERFNet
from .fast_scnn import FastSCNN
from .hrnet import HRNet
from .icnet import ICNet
from .mae import MAE
from .mit import MixVisionTransformer
from .mobilenet_v2 import MobileNetV2
from .mobilenet_v3 import MobileNetV3
from .mscan import MSCAN
from .pidnet import PIDNet
from .resnest import ResNeSt
from .resnet import ResNet, ResNetV1c, ResNetV1d
from .resnext import ResNeXt
from .stdc import STDCContextPathNet, STDCNet
from .swin import SwinTransformer
from .timm_backbone import TIMMBackbone
from .twins import PCPVT, SVT
from .unet import UNet
from .vit import VisionTransformer
# from .mix_transformer import mit_b0, mit_b1, mit_b2, mit_b3, mit_b4, mit_b5 #for feedformer
from .mit import EfficientMultiheadAttention
<<<<<<< HEAD
from .mit_btn import MixVisionTransformer_btn
from .mit_btn2 import MixVisionTransformer_btn2
=======
from .lvt import lvt
from .mit_multi import MixVisionTransformerMulti
>>>>>>> skyeom

__all__ = [
    'ResNet', 'ResNetV1c', 'ResNetV1d', 'ResNeXt', 'HRNet', 'FastSCNN',
    'ResNeSt', 'MobileNetV2', 'UNet', 'CGNet', 'MobileNetV3',
<<<<<<< HEAD
    'VisionTransformer', 'SwinTransformer', 'MixVisionTransformer', 'MixVisionTransformer_new', 'MixVisionTransformer_btn', 'MixVisionTransformer_btn2',
=======
    'VisionTransformer', 'SwinTransformer', 'MixVisionTransformer',
>>>>>>> skyeom
    'BiSeNetV1', 'BiSeNetV2', 'ICNet', 'TIMMBackbone', 'ERFNet', 'PCPVT',
    'SVT', 'STDCNet', 'STDCContextPathNet', 'BEiT', 'MAE', 'PIDNet', 'MSCAN', 'lvt', 'MixVisionTransformerMulti'
    # 'mit_b0', 'mit_b1', 'mit_b2', 'mit_b3', 'mit_b4', 'mit_b5'
]
