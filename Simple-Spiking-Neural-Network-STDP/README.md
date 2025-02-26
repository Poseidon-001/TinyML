## Usage
You first have to install the requiered libraries from the requirements.txt.
 ```
  pip install -r requirements.txt
  ``Y
After this, you can train your own SNN.
 ```
  python3 main.py -mode training -use_tf_dataset
  ```
You can also use this script to test your own trained network and weights.
 ```
  python3 main.py -mode inference -weights_path folder/weights.csv -labels_path folder/labels.csv -image_inference_path folder/picture.png
  ```
To get a list of all possible hyperparameters use
 ```
  python3 main.py -h
```
<p align="right">(<a href="#top">back to top</a>)</p>

## Structure
<!-- Project Structure -->

    .
    ├── src                    
    │   ├── MNIST                              # Here is the entire MNIST dataset          
    │   │   ├── testing
    │   │   │   ├── 0                          # Each subfolder represents a class
    │   │   │   │   ├── 3.png
    │   │   │   │   ├── 10.png
    │   │   │   │   ├── 13.png
    │   │   │   │   ...
    │   │   │   ├── 1
    │   │   │   ├── 2
    │   │   │   ├── 3
    │   │   │   ├── 4
    │   │   │   ├── 5
    │   │   │   ├── 6
    │   │   │   ├── 7
    │   │   │   ├── 8
    │   │   │   ├── 9
    │   │   ├── training
    │   │   │   ├── 0
    │   │   │   ...
    │   │   ├── labels.csv
    ├── Notebooks
    │   │── ANN_Comparison.ipynb          # Comparison ANNs being trained in Tensorflow
    │   │── Visualization_Helper.ipynb    # Visualization of our results
    │   │── Deprecated_Training.ipynb     # Old deprecated training notebook
    ├── Pretrained              # Pretrained weights and labels for testing
    │   │── labels.csv
    │   │── weights.csv
    │── .gitignore
    │── main.py                 # Main file for executing training/inference the SNN
    │── Neuron.py
    │── Paper.pdf               # The term paper we submitted
    │── Parameters.py           # All parameters used for training/inference
    │── README.md
    │── requirements.txt
    └── SNN.py                  # The file containing all functions for training/infering 
<p align="right">(<a href="#top">back to top</a>)</p>

