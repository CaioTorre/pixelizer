# Pixelizer
Python-based image tool to create pixel art from existing images
## Usage
### Command structure
```bash
python pixel.py <image> [-w <pixel width>] [-h <pixel height>] [-s <color samples>] [-B]
```
### Arguments
- `-B`: Set big-mode
    - If big-mode is not set, the output image size is set directly with `-w` and `-h`
    - If big-mode is set, the output image size is the same as the input image size
- `-w` and `-h`: Define custom output sizes
    - If big-mode is not set, the output image size is set as the values passed
    - If big-mode is set, these arguments define the 'blockiness' of the output (still in beta, possibly leaves invisible column at the left of the image and invisible row at the bottom of the image)
    - If not passed as arguments, they will be the same as the original image
- `-s`: Define color sampling (from 1 to 256)
    - Can be used to simulate older graphics if set to a small enough value
## Output
The output image will be saved in the current folder, following the structure:
```
[original_image_name]_[output_image_width]x[output_image_height]_[big|small].png
```