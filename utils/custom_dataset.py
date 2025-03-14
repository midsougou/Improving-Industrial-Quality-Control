from torch.utils.data import Dataset
import pandas as pd
import os
from PIL import Image

class CustomDataset(Dataset):
    """
    This is the custom dataset class for the test images (so no labels provided)

    Args:
        Dataset (_type_): _description_
    """
    def __init__(self, data_path, transform=None):
        self.data_path = data_path
        self.transform = transform
        self.images = []


        for img_name in os.listdir(self.data_path):
            img_path = os.path.join(self.data_path, img_name)
            self.images.append(img_path)


    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = self.images[idx]
        image = Image.open(img_path).convert("RGB")  # Charger l'image
    
        # Appliquer les transformations
        if self.transform:
            image = self.transform(image)  # Appliquer les transformations à l'image

        filename = os.path.basename(img_path)

        return filename, image                               
