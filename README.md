# Jetson Nano YOLO Car Detection Demo

## Quick Start (3 minutes)

### Step 1: Clone Repository First
```bash
mkdir ~/yolo_demo && cd ~/yolo_demo
git clone https://github.com/QMay17/sjsu_summer2025.git
cd sjsu_summer2025
```

### Step 2: Download Sample Images Into Repository Folder
```bash
# Download sample images with cars (into the same folder as the Python scripts)
wget https://tinyurl.com/2k5rc87t -O cars1.jpg
wget https://tinyurl.com/n2krc25y -O cars2.jpg
wget https://tinyurl.com/4cfx7me8 -O street_cars.jpg
```

### Step 3: Install Requirements and Run
```bash
pip3 install -r requirements.txt

# Simple detection (processes first image found)
python3 simple_yolo.py

# Full detection (processes all images)
python3 yolo_demo.py

# Batch processing (fastest for multiple images)
python3 batch_detect.py
```

## What This Demo Does

✅ **Loads YOLOv8** (state-of-the-art object detection)  
✅ **Detects cars, trucks, and buses only** (focused detection)  
✅ **Shows confidence scores** for each car detected  
✅ **Draws green bounding boxes** around detected vehicles  
✅ **Saves results** as new image files with car detection  
✅ **Counts total cars** found in each image

## Available Scripts

- **`simple_yolo.py`** - Detect cars in one image (beginner-friendly)
- **`yolo_demo.py`** - Detect cars in all images with detailed output
- **`batch_detect.py`** - Fast batch car detection for multiple images

## Vehicle Types Detected

🚗 **Cars** - Sedans, hatchbacks, coupes  
🚚 **Trucks** - Pickup trucks, delivery trucks  
🚌 **Buses** - City buses, school buses, coaches  

Perfect for traffic monitoring, parking lot analysis, or autonomous vehicle projects!

## Expected Output

When you run the detection, you'll see:
```
🚗 Car Detection Results:
  1. car: 0.85
  2. car: 0.92
  3. truck: 0.78

Saved car detection results as: cars_detected_cars1.jpg
Total cars found: 3
```

## File Structure After Running

```
~/yolo_demo/
└── sjsu_summer2025/             # Your repository folder
    ├── simple_yolo.py           # Python scripts
    ├── yolo_demo.py
    ├── batch_detect.py
    ├── requirements.txt
    ├── README.md
    ├── cars1.jpg                # Downloaded images
    ├── cars2.jpg                
    ├── street_cars.jpg          
    ├── cars_detected_cars1.jpg      # Results with bounding boxes
    ├── cars_detected_cars2.jpg      
    └── cars_detected_street_cars.jpg
```

## Troubleshooting

**First run is slow?**  
YOLO downloads the model file (~6MB) automatically on first use.

**"No images found" error?**  
Make sure you downloaded the sample images using the wget commands in Step 2, or add your own .jpg/.png files to the `sjsu_summer2025` folder.

**No GPU acceleration warning?**  
That's normal on Jetson Nano. CPU detection works fine for this demo.

**Out of memory error?**  
Try using smaller images or restart the Jetson Nano to free up memory.

**Import error for ultralytics?**  
Run: `pip3 install ultralytics opencv-python`

## Real-World Applications

🚦 **Traffic monitoring** - Count cars at intersections  
🅿️ **Parking lot management** - Monitor available spaces  
🚨 **Security systems** - Vehicle access control  
📊 **Smart city data** - Traffic flow analysis

## Next Steps

After mastering car detection, you can:
- Add detection for motorcycles and bicycles
- Count cars in video files
- Set up real-time detection with a camera
- Create a traffic counting system
- Build a parking space monitoring app

## Questions?

If you encounter issues, check that:
1. You have internet connection (for model download)
2. Image files are in the correct location
3. All required packages are installed
4. You have enough free disk space (~100MB)