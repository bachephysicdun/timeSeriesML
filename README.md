# timeSeriesML


### Prepare Environment (for Mac M1)
1. Install lates Miniconda (from [here](https://docs.anaconda.com/free/miniconda/))
2. Create enviroment with Pytorch:
    + `conda env create -f torch.yml`
    + `conda activate torch`
    + `python -m ipykernel install --user --name torch --display-name "torch (Python 3.11)"`

3. Create enviroment with Tensorflow
    + `conda env create -f tensorflow.yml`
    + `conda activate tensorflow`
    + `python -m ipykernel install --user --name tensorflow --display-name "tensorflow (Python 3.11)"`
    + verify installation by: `python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`