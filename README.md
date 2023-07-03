# Efficient-use-of-visual-transformers
This repository is for the "Efficient use of visual transformers" project.
This includes 2 jupyter notebooks to run on kaggle.
"ViT Quantization" is meant to test quantization on the ViT model from PyTorch.
"ViT Inference" is meant to test speeding inference time on the ViT model from huggingface.

# How to run
simply download the notebook and run it on kaggle.
to do so you will need to access the validation dataset we have prepared manually.

[1]: https://www.kaggle.com/datasets/matanmillionshik/imagenet-val "ImageNet-1k validation set"

# Prepare the dataset on your own
To access IMageNet validation set you will need to create a user and download it from the officail imagenet website.

[2]: https://image-net.org/ "ImageNet"

Download the validation set locally to your PC, all other needed files are in the '/datafiles' folder.
Please put the validation set inside the 'imagenet_val' folder.
To prepare the dataset simply download the repository to your local machine and run the 'Dataset.py' function.

# Possible errors
1. If you encounter an issue with the relative paths in 'Dataset.py' - change them to absolute.
2. If you see unmatching labels - it means you didn't use 'Dataset.py' correctly, and the labels are still used according to the official
dictionary instead of the one ViT creators used.
3. If you encounter problems during quantization - sorry :(
4. If you encounter a problem with loading huggingface's 'imagenet-1k' try using our validation set instead.

