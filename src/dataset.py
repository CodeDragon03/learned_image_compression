import os
from pathlib import Path

from PIL import Image
from loguru import logger
import numpy as np
from tqdm import tqdm
import typer

from src.config import EXTERNAL_DATA_DIR, PROCESSED_DATA_DIR

app = typer.Typer()

@app.command()
def main(
    input_path: Path = EXTERNAL_DATA_DIR / "kodak",
    output_path: Path = PROCESSED_DATA_DIR / "kodak",
):
    # use the provided input and output paths
    DATA_PATH = str(input_path)
    PROCESSED_DATA_PATH = str(output_path)

    # List only image files (png/jpg)
    images = [
        f
        for f in os.listdir(DATA_PATH)
        if f.lower().endswith((".png", ".jpg"))
    ]
    logger.info(f"The total number of images are: {len(images)}.")
    logger.info("-" * 50)
    logger.info("The shape of the images in the Kodak dataset are:")
    logger.info("-" * 50)

    # Print input image shapes
    for img in tqdm(images, desc="Reading input image shapes", unit="image"):
        arr = np.array(Image.open(os.path.join(DATA_PATH, img)))
        logger.info(f"{img}: {arr.shape}")

    # Create processed data directory
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    # Process and save images
    for img in tqdm(images, desc="Processing images", unit="image"):
        arr = np.clip(
            np.array(Image.open(os.path.join(DATA_PATH, img))), 0, 255
        ).astype(np.uint8)
        im = (
            Image.fromarray(arr)
            .resize((256, 256))
            .convert("RGB")
        )
        im.save(os.path.join(PROCESSED_DATA_PATH, img))

    logger.info("-" * 50)
    logger.info("The shape of the images in the processed dataset are:")
    logger.info("-" * 50)

    # Print processed image shapes
    for img in tqdm(images, desc="Reading processed image shapes", unit="image"):
        arr = np.array(Image.open(os.path.join(PROCESSED_DATA_PATH, img)))
        logger.info(f"{img}: {arr.shape}")

if __name__ == "__main__":
    app()