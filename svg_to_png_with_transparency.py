import os
import cairosvg

def convert_svg_to_png_with_transparency(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of SVG files in the input folder
    svg_files = [f for f in os.listdir(input_folder) if f.endswith('.svg')]

    # Convert each SVG file to PNG with transparency
    for svg_file in svg_files:
        # Input SVG file path
        svg_path = os.path.join(input_folder, svg_file)
        
        # Output PNG file path
        png_path = os.path.join(output_folder, os.path.splitext(svg_file)[0] + '.png')

        # Convert SVG to PNG with transparency
        cairosvg.svg2png(url=svg_path, write_to=png_path, parent_width=None, parent_height=None)

if __name__ == "__main__":
    # Input folder containing SVG files
    input_folder = "input_svgs"
    
    # Output folder for PNG files
    output_folder = "output_pngs"
    
    # Convert SVG files to PNG with transparency
    convert_svg_to_png_with_transparency(input_folder, output_folder)
