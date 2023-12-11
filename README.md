# Group 6 Experiment on SinDDM
This is group 6's experiment on SinDDM. The modified code adds a receptive field offset argument that can be used as part of the command that runs the SinDDM main application [main.py](main.py). We added a script to run the required sampling for the experiment found in [here](style_gen.py). We have also included the trained models in the repo if you desire to test the sampling yourself.

For training and other modes of sampling, please refer to the [original README](README_original.md).

## Installation
1. Install Miniconda or Conda
2. Create a new environment with Python 3.8
```
conda create --name sinddm python=3.8
conda activate sinddm
```
3. Download requirements
```
pip install -r requirements.txt
```

## Sampling script
Make sure you are in the sinddm conda environment before running.
```
python3 style_gen.py --prompt "Van Gogh Style"
```
If you want to sample from individual models, just replace {model}, {k}, {prompt}, {v}, and {num} to what you want to sample from.
- {model}: `cartoon`, `city`, `human_portrait`, `starry_night`
- {k}: `_small_rf`, ` ` (empty), `_big_rf`
- {prompt}: any prompt you want, for example: `Van Gogh Style`
- {v}: `-2` (for _small_rf), `0` (or omit argument, for default model), `2` (for _big_rf)
- {num}: cuda device you want to use for the sampling
```
python3 main.py --scope {model}{k} --mode clip_style_gen --clip_text '{prompt}' --dataset_folder ./datasets/{model}/ --image_name {model}.png --results_folder  ./results/ --load_milestone 2 --receptive_field_offset {v} --device_num {num}"
```
__Note:__ To run the script on a different image scale, move the desired model from the `./results/{model}_{big/small}_scale` folder to the associated `./results/{model}` folder, then run the model with an empty k and v of 0
