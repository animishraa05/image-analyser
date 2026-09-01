# Lab 1: Image Analyzer

This script reads an image file and extracts metadata, including standard file properties (size, format, dimensions) and EXIF data (camera make/model, date taken, orientation, etc.) if available.

## Supported Formats
- Minimum: JPG/JPEG, PNG
- Bonus: TIFF, WEBP, BMP

## Usage
```bash
python image_analyzer.py <path_to_image>
```

## Requirements
- Python 3
- Pillow (`pip install Pillow`)

## System Workflow / Use Case
```mermaid
flowchart LR
    User([User])
    subgraph IA [Image Analyzer]
        UC1([Validate File Path])
        UC2([Extract Basic Properties])
        UC3([Extract EXIF Metadata])
        UC4([Generate Output Report])
    end
    
    User -->|Provides Image| UC1
    UC1 --> UC2
    UC1 --> UC3
    UC2 --> UC4
    UC3 --> UC4
    UC4 -->|View Metadata| User
```

## Sample Output
```text
================================
IMAGE METADATA REPORT
================================
File Name       : proper_image.jpg
File Size       : 273.05 KB
File Format     : JPEG
Width           : 1600 px
Height          : 1598 px
Resolution      : (72, 72)
Color Mode      : RGB

EXIF Metadata
-------------------------------
Software        : Adobe Photoshop CS4 Windows
Orientation     : 1
Date Taken      : 2009:01:31 22:25:45
```
