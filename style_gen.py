"""
A script to sample text-guided (clip) style generation from the 12 models of the experiment.
"""
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", "-p", help="Prompt for clip guided generation", required=True)
    args = parser.parse_args()

    models = {
        "city",
        "human_portrait",
        "cartoon",
        "starry_night"
    }
    rf_types = {
        "_small_rf": -2,
        "": 0,  # default receptive field
        "_big_rf": 2
    }
    for model in models:
        for k, v in rf_types.items():
            print(f"Sampling from {model}{k}")
            os.system(
                f"python main.py --scope {model}{k} --mode clip_style_gen --clip_text '{args.prompt}' "
                f"--dataset_folder ./datasets/{model}/ --image_name {model}.png --results_folder"
                f" ./results/ --load_milestone 2 --receptive_field_offset {v} --device_num 6"
            )


if __name__ == '__main__':
    main()