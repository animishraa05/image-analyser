import os
from PIL import Image
from PIL.ExifTags import TAGS

def analyze_image(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return

    try:
        with Image.open(file_path) as img:
            # File Info
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_size_kb = file_size / 1024
            file_format = img.format
            width, height = img.size
            resolution = img.info.get('dpi', 'Unknown')
            color_mode = img.mode

            print("================================")
            print("IMAGE METADATA REPORT")
            print("================================")
            print(f"File Name       : {file_name}")
            print(f"File Size       : {file_size_kb:.2f} KB")
            print(f"File Format     : {file_format}")
            print(f"Width           : {width} px")
            print(f"Height          : {height} px")
            print(f"Resolution      : {resolution}")
            print(f"Color Mode      : {color_mode}")

            # EXIF Metadata
            exif_data = img.getexif()
            if exif_data:
                print("\nEXIF Metadata")
                print("-------------------------------")
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    # Filter some common EXIF tags for cleaner output
                    if tag in ('Make', 'Model', 'DateTime', 'Orientation', 'Software'):
                        label = tag
                        if tag == 'Make':
                            label = 'Camera Make'
                        elif tag == 'Model':
                            label = 'Camera Model'
                        elif tag == 'DateTime':
                            label = 'Date Taken'
                        print(f"{label:15} : {value}")
            else:
                print("\nNo EXIF Metadata found.")
    except Exception as e:
        print(f"Error analyzing image: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        analyze_image(sys.argv[1])
    else:
        print("Usage: python image_analyzer.py <path_to_image>")
