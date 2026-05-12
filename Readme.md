# CausalGeD: Blending Causality and Diffusion for Spatial Gene Expression Generation

We present CausalGeD, which combines diffusion and autoregressive processes to leverage these relationships. By generalizing the Causal Attention Transformer architecture from the image
generation to high-dimensional gene expression data, our model captures regulatory mechanisms without requiring predefined relationships.


## Setup
Create a conda environment using the environment.yml file
```
 conda env create -f environment.yml
```
Please consider installing any package manually via pip or conda if there is dependency issue.
## Data
All the datasets used in this paper can be downloaded from url：https://zenodo.org/records/12792074

## Preprocess data

To preprocess the data, run the `data_preprocess.py` script located in the `preprocess` directory. Use the following command:

```
python preprocess/data_preprocess.py --input data/raw_data.csv --output data/processed_data.csv
```

## Running Experiments

To train the CausalGeD , use the following command:

```
python main.py
or for HBC data the following command could be used:
bash HBC.sh
```

To evaluate the model, run:

```
python evaluate.py

```
</pre></div>
