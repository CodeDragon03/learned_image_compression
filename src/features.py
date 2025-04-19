from pathlib import Path
import numpy as np
from PIL import Image
from loguru import logger
from tqdm import tqdm
import typer
import os

from src.config import PROCESSED_DATA_DIR

app = typer.Typer()

@app.command()
def main(
    input_path: Path = PROCESSED_DATA_DIR / "kodak",
    output_path: Path = PROCESSED_DATA_DIR / "features.csv",
):
    logger.info("Generating features from dataset...")
    
    # List all processed images
    images = [f for f in os.listdir(input_path) if f.lower().endswith(('.png', '.jpg'))]
    
    # Initialize feature array
    features = []
    
    # Extract features from each image
    for img in tqdm(images, desc="Extracting features"):
        image = Image.open(os.path.join(input_path, img))
        image_array = np.array(image)
        
        # Calculate basic statistical features
        mean = image_array.mean(axis=(0,1))
        std = image_array.std(axis=(0,1))
        features.append(np.concatenate([mean, std]))
    
    # Save features
    features = np.array(features)
    np.savetxt(output_path, features, delimiter=',')
    
    logger.success("Features generation complete.")

if __name__ == "__main__":
    app()