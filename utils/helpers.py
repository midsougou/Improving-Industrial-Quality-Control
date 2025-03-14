from PIL import Image
import matplotlib.pyplot as plt

def rotate_and_crop_image(path, angle, crop_box, plot=False):
    """
    Applique une rotation d'un angle donné et un crop sur une image, puis enregistre le résultat en .png.
    Optionnellement, affiche l'image si plot=True.
    
    Arguments :
    - input_image_path : Chemin de l'image d'entrée.
    - output_image_path : Chemin pour enregistrer l'image modifiée.
    - angle : L'angle de rotation en degrés (positif dans le sens antihoraire).
    - crop_box : Un tuple (left, upper, right, lower) définissant les points du crop en pixels.
    - plot : Booléen, si True affiche l'image modifiée.
    """
    # Ouvrir l'image
    image = Image.open(path)
    
    # Appliquer la rotation (expand=True permet d'agrandir l'image pour qu'elle s'ajuste au cadre après rotation)
    rotated_image = image.rotate(angle, expand=True)
    
    # Appliquer le crop avec les points fournis
    cropped_image = rotated_image.crop(crop_box)
    
    # Enregistrer l'image au format PNG
    cropped_image.save(path, format='PNG')
    #print(f"Image enregistrée avec succès sous {path}")
    
    # Si plot=True, afficher l'image modifiée
    if plot:
        plt.imshow(cropped_image)
        plt.axis('off')  # Masquer les axes
        plt.title(f"Image après rotation de {angle}° et crop")
        plt.show()