import os
from PIL import Image

def compress_and_convert_images_recursive(input_folder, output_folder=None, quality=80):
    """
    Recherche récursive des images JPEG dans un dossier et ses sous-dossiers,
    puis les compresse et les convertit en WebP.

    :param input_folder: Dossier de départ contenant les images JPEG.
    :param output_folder: Dossier de sortie pour les images WebP. Si None, les images seront sauvegardées dans les mêmes dossiers que leurs originaux.
    :param quality: Qualité de compression pour le format WebP (1-100).
    """
    for root, _, files in os.walk(input_folder):
        # Définir le dossier de sortie pour ce sous-dossier
        current_output_folder = output_folder or root

        # Crée le dossier de sortie s'il n'existe pas
        if not os.path.exists(current_output_folder):
            os.makedirs(current_output_folder)

        for filename in files:
            if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, input_folder)  # Chemin relatif pour organiser les sous-dossiers
                output_subfolder = os.path.join(output_folder, relative_path) if output_folder else root

                # Assurez-vous que le sous-dossier de sortie existe
                if not os.path.exists(output_subfolder):
                    os.makedirs(output_subfolder)

                output_path = os.path.join(output_subfolder, os.path.splitext(filename)[0] + ".webp")
                
                try:
                    with Image.open(input_path) as img:
                        # Conversion et compression
                        img.convert("RGB").save(output_path, "WEBP", quality=quality)
                    print(f"Image {input_path} compressée et convertie en {output_path}")
                except Exception as e:
                    print(f"Erreur lors du traitement de l'image {input_path}: {e}")

# Exemple d'utilisation
input_folder = "Pictures/Zoom/SacreCoeur"  # Remplacez par le chemin du dossier racine
output_folder = None  # Remplacez par le chemin du dossier de sortie ou mettez None
compress_and_convert_images_recursive(input_folder, output_folder, quality=80)
