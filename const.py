rus = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
    'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
    'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '.', ',', '%', '*', ':', '"', '(', ')', '+', '-', '='
]

rus = {i: letter for i, letter in enumerate(rus)}

image_path = "letters.png"

box_size = 118
spacing_vertical = 60
start_x, start_y = 60, 60
