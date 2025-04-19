import os

from PIL import Image
from loguru import logger
import matplotlib.pyplot as plt
import numpy as np
import typer

from src.config import EXTERNAL_DATA_DIR, FIGURES_DIR

app = typer.Typer()

def plot_pixel_distribution(images, data_path, save_path):
    """Plot histogram of pixel distributions for all images."""
    fig, ax = plt.subplots(6, 4, figsize=(20, 20))
    fig.suptitle('Pixel values in Kodak dataset', fontsize=20, fontweight='bold')
    
    axes = ax.flatten()
    
    for img, ax in zip(images, axes):
        image = Image.open(os.path.join(data_path, img))
        image = np.array(image)
        ax.hist(image.ravel(), bins=256, color='gray', alpha=0.5)
        ax.set_title(img.capitalize().replace('.png', '').replace('.jpg', ''), 
                    fontsize=10, fontweight='bold')   
        ax.set_xlim([0, 255])
        ax.set_ylim([0, 20000])
        ax.set_xlabel('Pixel Value')
        ax.set_ylabel('Frequency')
        ax.grid()
    
    plt.tight_layout(pad=2)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

def plot_dataset_preview(images, data_path, save_path):
    """Plot preview of all images in the dataset."""
    fig, ax = plt.subplots(6, 4, figsize=(20,20))
    fig.suptitle('Kodak Dataset', fontsize=20, fontweight='bold')
    
    axes = ax.flatten()
    
    for img, ax in zip(images, axes):
        if img.endswith('.png'):
            try:
                image = Image.open(os.path.join(data_path, img))
                image = image.resize((100, 100))
                ax.set_title(img.capitalize().replace('.png', ''), 
                           fontsize=10, fontweight='bold')
                ax.imshow(image)
                ax.axis('off')
            except Exception as e:
                logger.error(f"Error loading image {img}: {e}")
    
    # Remove empty subplots
    for ax in axes[len(images):]:
        ax.remove()
    
    plt.tight_layout(pad=2)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

@app.command()
def main(
    data_path: str = os.path.join(EXTERNAL_DATA_DIR, "kodak"),
    figure_path: str = FIGURES_DIR,
):
    """Generate and save dataset visualization plots."""
    logger.info("Generating dataset visualization plots...")
    
    # Get list of images
    images = [img for img in os.listdir(data_path) 
             if img.endswith(('.png', '.jpg'))]
    
    # Create plots
    plot_pixel_distribution(
        images, 
        data_path, 
        os.path.join(figure_path, 'pixel_distribution.png')
    )
    logger.info("Pixel distribution plot saved.")
    
    plot_dataset_preview(
        images, 
        data_path, 
        os.path.join(figure_path, 'kodak_dataset.png')
    )
    logger.info("Dataset preview plot saved.")

if __name__ == "__main__":
    app()