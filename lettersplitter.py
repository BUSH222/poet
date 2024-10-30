from const import image_path, start_x, start_y, box_size, spacing_vertical, rus
from PIL import Image
import os


def fetch_letters_from_png(output_folder_local='letters'):
    """Fetches the """
    img = Image.open(image_path)
    num_letters_per_row = (img.width - start_x) // box_size
    num_rows = (img.height - start_y) // box_size

    output_folder = os.path.join(os.getcwd(), output_folder_local)
    os.makedirs(output_folder, exist_ok=True)

    for row in range(num_rows):
        for col in range(num_letters_per_row):
            left = start_x + col * box_size
            upper = start_y + row * (box_size + spacing_vertical)
            right = left + box_size
            lower = upper + box_size
            letter_img = img.crop((left, upper, right, lower))
            letter_img_cropped = letter_img.crop(letter_img.getbbox())
            if letter_img.getbbox():
                letter_path = os.path.join(output_folder, f"{rus[row]}_{col}.png")
                letter_img_cropped.save(letter_path)

    print("Done")


if __name__ == "__main__":
    fetch_letters_from_png()
