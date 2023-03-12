
"""
This file is used for downloading models and images used in deploying hugging face demo:
https://huggingface.co/spaces/sczhou/CodeFormer
"""

import os
import torch

pretrain_model_url = {
    'codeformer': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/codeformer.pth',
    'detection': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/detection_Resnet50_Final.pth',
    'parsing': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/parsing_parsenet.pth',
    'realesrgan': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/RealESRGAN_x2plus.pth'
}

images_url = {
    '01.png': 'https://replicate.com/api/models/sczhou/codeformer/files/fa3fe3d1-76b0-4ca8-ac0d-0a925cb0ff54/06.png',
    '02.jpg': 'https://replicate.com/api/models/sczhou/codeformer/files/a1daba8e-af14-4b00-86a4-69cec9619b53/04.jpg',
    '03.jpg': 'https://replicate.com/api/models/sczhou/codeformer/files/542d64f9-1712-4de7-85f7-3863009a7c3d/03.jpg',
    '04.jpg': 'https://replicate.com/api/models/sczhou/codeformer/files/a11098b0-a18a-4c02-a19a-9a7045d68426/010.jpg',
    '05.jpg': 'https://replicate.com/api/models/sczhou/codeformer/files/7cf19c2c-e0cf-4712-9af8-cf5bdbb8d0ee/012.jpg',
}

def download_weights():
    if not os.path.exists('CodeFormer/weights/CodeFormer/codeformer.pth'):
        load_file_from_url(url=pretrain_model_url['codeformer'], model_dir='CodeFormer/weights/CodeFormer', progress=True, file_name=None)
    if not os.path.exists('CodeFormer/weights/facelib/detection_Resnet50_Final.pth'):
        load_file_from_url(url=pretrain_model_url['detection'], model_dir='CodeFormer/weights/facelib', progress=True, file_name=None)
    if not os.path.exists('CodeFormer/weights/facelib/parsing_parsenet.pth'):
        load_file_from_url(url=pretrain_model_url['parsing'], model_dir='CodeFormer/weights/facelib', progress=True, file_name=None)
    if not os.path.exists('CodeFormer/weights/realesrgan/RealESRGAN_x2plus.pth'):
        load_file_from_url(url=pretrain_model_url['realesrgan'], model_dir='CodeFormer/weights/realesrgan', progress=True, file_name=None)

def download_images():
    if not os.path.exists('01.png'):
        torch.hub.download_url_to_file(images_url['01.png'], '01.png')
    if not os.path.exists('02.jpg'):
        torch.hub.download_url_to_file(images_url['02.jpg'], '02.jpg')
    if not os.path.exists('03.jpg'):
        torch.hub.download_url_to_file(images_url['03.jpg'], '03.jpg')
    if not os.path.exists('04.jpg'):
        torch.hub.download_url_to_file(images_url['04.jpg'], '04.jpg')
    if not os.path.exists('05.jpg'):
        torch.hub.download_url_to_file(images_url['05.jpg'], '05.jpg')

        
if __name__ == "__main__":
    download_images()
    download_weights()
    
