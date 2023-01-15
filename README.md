# Chinese Character Practice Sheet Generator
# Introduction
This script allows you to easily generate customizable Chinese character practice sheets. You can set the paper size, margins, and square size to fit your needs. The script outputs the image in both PNG and PDF formats.

# Requirements
* Python 3
* PIL (Python Imaging Library)
# Usage
The script defines a function generate_chinese_character_practice that takes in 5 parameters:

* paper_size: Tuple of width and height in pixels (default is A4 paper size)
* margins: Tuple of width and height margins in pixels (default is 0.5cm horizontally and 0.85cm vertically)
* square_size: Size of each square in pixels (default is 1cm)
* filename: Name of the output file (default is "chinese_character_practice")
* file_format: Format of the output file (default is "png")
```python
generate_chinese_character_practice((2100, 2970), (50,50), 100, "chinese_character_practice", "png")
generate_chinese_character_practice((2100, 2970), (50,50), 100, "chinese_character_practice", "pdf")
```
The above example will generate an A4 paper size with 0.5cm margins, 1cm square size, and save the image in both PNG and PDF formats with the name "chinese_character_practice".

Here is an example of generating a US letter paper size with 0.5cm margins, 1cm square size:
```python
generate_chinese_character_practice((2550, 3300), (50, 50), 100, "chinese_character_practice_usletter", "png")
```
You can also generate a custom paper size with different margins and square sizes:
```python
generate_chinese_character_practice((5000, 7000), (150, 150), 200, "chinese_character_practice_custom", "png")
```
The script will automatically calculate the number of squares that will fit on the paper, ensuring that the image is symmetric and all squares are of equal size.
