## Installation

### Requirements:
- PyTorch 1.3
- torchvision from master
- cocoapi
- yacs
- matplotlib
- GCC >= 4.9
- OpenCV
- CUDA >= 9.2

### 1. Using the `environment.yml`

Run the following command to create a conda environment using the `environment.yml` file:

```bash
conda env create -f environment.yml
```

This will set up the MEGA environment as specified in the `environment.yml` file which should include all the necessary dependencies and packages. Make sure to activate the new environment with:

```bash
conda activate MEGA
```

Once activated, you can proceed with the installation of other dependencies, if they are not included in the `environment.yml` file. 


### 2. Step-by-Step Installation - from Folders

```bash
# Create a conda environment named MEGA
conda create --name MEGA -y python=3.7
conda activate MEGA

# Install essential packages
conda install ipython pip
pip install ninja yacs cython matplotlib tqdm opencv-python scipy

# Install PyTorch and torchvision (CUDA 10.0 for this example)
conda install pytorch=1.2.0 torchvision cudatoolkit=10.0 -c pytorch

# Install pycocotools
cd cocoapi/PythonAPI
python setup.py build_ext install

# Install cityscapesScripts
cd cityscapesScripts/
python setup.py build_ext install

# Install NVIDIA Apex
cd apex
python setup.py build_ext install

# Clone the mega.pytorch repository and install
cd mega.pytorch
python setup.py build develop

# Install an older version of Pillow, if necessary
pip install 'pillow<7.0.0'
```

In case you encounter issues with the manual installation, you can use the `environment.yml` file if provided in the same directory.

### Step-by-Step Installation - from Scratch, see errors encountered

```bash
# Create a conda environment named MEGA
conda create --name MEGA -y python=3.7
conda activate MEGA

# Install essential packages
conda install ipython pip
pip install ninja yacs cython matplotlib tqdm opencv-python scipy

# Install PyTorch and torchvision (CUDA 10.0 for this example)
conda install pytorch=1.2.0 torchvision cudatoolkit=10.0 -c pytorch

# Install pycocotools
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
python setup.py build_ext install

# Install cityscapesScripts
git clone https://github.com/mcordts/cityscapesScripts.git
cd cityscapesScripts/
python setup.py build_ext install

# Install NVIDIA Apex
git clone https://github.com/NVIDIA/apex.git
cd apex
python setup.py build_ext install

# Clone the mega.pytorch repository and install
git clone https://github.com/Scalsol/mega.pytorch.git
cd mega.pytorch
python setup.py build develop

# Install an older version of Pillow, if necessary
pip install 'pillow<7.0.0'
```

### Error Handling

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



```