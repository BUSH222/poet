from PIL import Image
import os


rus = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
    'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
    'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '.', ',', '%', '*', ':', '"', '(', ')', '+', '-', '='
]

rus = {i: letter for i, letter in enumerate(rus)}

image_path = "letters.png"
img = Image.open(image_path)

box_size = 118
spacing_vertical = 60
start_x, start_y = 60, 60

num_letters_per_row = (img.width - start_x) // box_size
num_rows = (img.height - start_y) // box_size

output_folder = os.path.join(os.getcwd(), 'letters')
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
