# IMPORTS
import audio_utils
import os
from spleeter.separator import Separator
import soundfile as sf

# Example Usage for Utility Functions
file = "input/sinnerman.wav"

def separate_tracks(input_file, output_dir):
    # Create a separator object
    separator = Separator('spleeter:5stems')

    # Perform the separation
    separator.separate_to_file(input_file, output_dir)

    print(f"Separation complete. Output files are in {output_dir}")

if __name__ == "__main__":
    input_file = input("Enter the path to your input .wav file: ")
    output_dir = input("Enter the output directory path: ")

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    separate_tracks(input_file, output_dir)