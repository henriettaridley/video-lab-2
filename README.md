# MEGA for Video Object Detection - Update for Lab Assignment Two

[![License](https://img.shields.io/badge/license-BSD-blue.svg)](LICENSE)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/memory-enhanced-global-local-aggregation-for/video-object-detection-on-imagenet-vid)](https://paperswithcode.com/sota/video-object-detection-on-imagenet-vid?p=memory-enhanced-global-local-aggregation-for)

By [Yihong Chen](https://scalsol.github.io), [Yue Cao](http://yue-cao.me), [Han Hu](https://ancientmooner.github.io/), [Liwei Wang](http://www.liweiwang-pku.com/).

This repo is an official implementation of ["Memory Enhanced Global-Local Aggregation for Video Object Detection"](https://arxiv.org/abs/2003.12063), accepted by CVPR 2020. This repository contains a PyTorch implementation of our approach MEGA based on [maskrcnn_benchmark](https://github.com/facebookresearch/maskrcnn-benchmark), as well as some training scripts to reproduce the results on ImageNet VID reported in our paper. 

Besides, this repository also implements several other algorithms like [FGFA](http://openaccess.thecvf.com/content_iccv_2017/html/Zhu_Flow-Guided_Feature_Aggregation_ICCV_2017_paper.html) and [RDN](https://arxiv.org/abs/1908.09511). Any new methods are welcomed. Hoping for your pull request! We hope this repository would help further research in the field of video object detection and beyond. :)

## Installation

Please follow [INSTALL_ENV.md](INSTALL.md) for installation instructions. These have been updated to include the correct package dependencies required for the running of this project.

If you would like to run from the download packages instead. There are several updates which need to be made to the apex package to ensure it runs with Torch 10.2.

1. **AttributeError: module 'torch.cuda' has no attribute 'amp'**
   - This error suggests that the version of PyTorch being used does not have the `amp` module available under `torch.cuda`, which is a feature introduced in PyTorch 1.6.0. 
   - The specific lines can be commented out.

2. **ImportError: cannot import name 'FP16_Optimizer' from 'apex.fp16_utils'**
   - This error suggests that there was a problem importing `FP16_Optimizer` from `apex.fp16_utils`, which could be due to a variety of reasons, such as an incorrect installation of the `apex` library or incompatible versions. 
   - These can also be commented out.

3. **AttributeError: module 'torch.distributed' has no attribute '_all_gather_base'**
   **AttributeError: module 'torch.distributed' has no attribute '_reduce_scatter_base'**
   - The methods `_all_gather_base` and `_reduce_scatter_base` are not available in the `torch.distributed` module you're using. It could be due to using a different version of PyTorch or possible changes in the PyTorch distributed API. 
   - When this error occurs, you must comment out the following lines. 

4. **cv2.error: OpenCV(4.8.1) :-1: error: (-5:Bad argument) in function 'putText'**
   - This error points to the incorrect usage of the `cv2.putText()` function within OpenCV. The `org` parameter is expected to be a tuple containing integer values, representing the bottom-left corner of the text string in the image.
   - Modify the `predictor.py` script to ensure it passes integer coordinates to the `cv2.putText()` function as required by OpenCV.


## Running the Demos

In order to run the demo, make sure you have completed the installation steps and have the necessary files in place.

### Prerequisites
- Download the `R_101.pth` checkpoint file and ensure it is located in the root of the `mega.pytorch` directory, or update the demo command with the correct path to the checkpoint file.
- Place your image/video folder within the `datasets/` directory of the `mega.pytorch` project. For example, if you have an `image_folder` containing frames of a video, it should be placed as `mega.pytorch/datasets/image_folder`.

### Steps to Run a Demo

1. Navigate to the `mega.pytorch/demo/` directory:

   ```bash
   cd mega.pytorch/demo/
   ```

2. Follow the instructions in the README within the `demo/` directory to run a demo. The README there contains specific commands and examples on how to execute the demo script with various configurations and methods.