from torch.utils.data import Dataset
import pandas as pd
import os
from PIL import Image

class CustomImageDataset(Dataset):
    def __init__(self, csv_file, img_dir, map_label_idx, transform=None):
        self.data = pd.read_csv(csv_file)  # Read CSV
        self.img_dir = img_dir  # Root directory of images
        self.transform = transform
        self.map_label_idx = map_label_idx

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name = self.data.iloc[idx]["filename"]
        img_path = os.path.join(self.img_dir, img_name)  # Full path
        label_name = self.data.iloc[idx]["Label"]
        label = self.map_label_idx[label_name]  # Convert label to int

        image = Image.open(img_path).convert("RGB")  # Load image

        if self.transform:
            image = self.transform(image)

        return image, label  # Return as tuple (image, label)
