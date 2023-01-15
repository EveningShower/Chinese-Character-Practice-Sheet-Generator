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
![chinese_character_practice](https://user-images.githubusercontent.com/83130443/212557046-9b050dd6-50d9-474b-90ee-664d3fe3c849.png)

The above example will generate an A4 paper size with 0.5cm margins, 1cm square size, and save the image in both PNG and PDF formats with the name "chinese_character_practice".

Here is an example of generating a US letter paper size with 0.5cm margins, 1cm square size:
```python
generate_chinese_character_practice((2550, 3300), (50, 50), 100, "chinese_character_practice_usletter", "png")
```
![chinese_character_practice_usletter](https://user-images.githubusercontent.com/83130443/212557123-2d2a98d0-f253-40cb-a50e-a857411082b3.png)

You can also generate a custom paper size with different margins and square sizes:
```python
generate_chinese_character_practice((5000, 7000), (100, 100), 690, "chinese_character_practice_custom", "png")
```
![chinese_character_practice_custom](https://user-images.githubusercontent.com/83130443/212557242-dc98b323-5643-4f0e-ac9f-5009ddf3487a.png)


The script will automatically calculate the number of squares that will fit on the paper, ensuring that the image is symmetric and all squares are of equal size.
