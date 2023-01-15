from PIL import Image, ImageDraw

def generate_chinese_character_practice(paper_size, margins, square_size, filename, file_format):
    # Set the paper size and margins
    paper_width, paper_height = paper_size
    margins_width, margins_height = margins

    # Create a new image with a white background
    img = Image.new('RGB', (paper_width, paper_height), 'white')

    # Create a single square image with gray lines
    gray = (192, 192, 192)
    square = Image.new('RGB', (square_size, square_size), 'white')
    square_draw = ImageDraw.Draw(square)
    square_draw.line((square_size/2, 0, square_size/2, square_size), fill=gray, width=2)
    square_draw.line((0, square_size/2, square_size, square_size/2), fill=gray, width=2)
    square_draw.line((0, 0, square_size, square_size), fill=gray, width=2)
    square_draw.line((0, square_size, square_size, 0), fill=gray, width=2)
    square_draw.rectangle((0, 0, square_size, square_size), outline=gray, width=2)
    
    # Calculate the number of squares that will fit on the paper
    num_squares_width = (paper_width - (2 * margins_width)) // square_size
    num_squares_height = (paper_height - (2 * margins_height)) // square_size
    
    # Calculate the new margins so the image is symmetric
    margins_width = int((paper_width - num_squares_width*square_size)/2)
    margins_height = int((paper_height - num_squares_height*square_size)/2)
    
    # Replicate the square image multiple times on the paper
    for i in range(margins_width, margins_width+num_squares_width*square_size, square_size):
        for j in range(margins_height, margins_height+num_squares_height*square_size, square_size):
            img.paste(square, (i, j))

    # Save the image
    img.save(f'{filename}.{file_format}', dpi=(300,300))


