#!/usr/bin/env python3
"""
Simple Car Detection Script for Jetson Nano
Detects cars, trucks, and buses in all images from the 'images' folder
"""

import cv2
import os
from ultralytics import YOLO

def detect_vehicles():
    """Detect vehicles in all images from the images folder"""
    
    print("🚗 Starting Vehicle Detection Demo")
    print("=" * 50)
    
    # Check if images folder exists
    if not os.path.exists('images'):
        print("❌ Error: 'images' folder not found!")
        print("   Please create an 'images' folder and add some .jpg files")
        return
    
    # Find all image files in the images folder
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    image_files = []
    
    for file in os.listdir('images'):
        if any(file.lower().endswith(ext) for ext in image_extensions):
            image_files.append(f'images/{file}')
    
    if not image_files:
        print("❌ No image files found in the 'images' folder!")
        print("   Please add some .jpg or .png files to the 'images' folder")
        return
    
    print(f"📁 Found {len(image_files)} image(s) in 'images' folder")
    
    # Load YOLO model
    print("\n🔄 Loading YOLO model...")
    model = YOLO('yolov8n.pt')  # Downloads automatically on first run
    print("✅ YOLO model loaded successfully!")
    
    # Vehicle types we want to detect
    vehicle_types = ['car', 'truck', 'bus']
    
    total_vehicles_found = 0
    
    # Process each image
    for i, image_file in enumerate(image_files, 1):
        print(f"\n{'='*60}")
        print(f"🔍 Processing Image {i}/{len(image_files)}: {os.path.basename(image_file)}")
        print("-" * 40)
        
        # Load image
        image = cv2.imread(image_file)
        if image is None:
            print(f"❌ Could not load image: {image_file}")
            continue
        
        # Run YOLO detection
        results = model(image)
        result = results[0]
        
        # Filter for vehicles only
        vehicles_found = 0
        vehicle_detections = []
        
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])
            
            # Check if it's a vehicle type we want
            if class_name.lower() in vehicle_types:
                vehicles_found += 1
                total_vehicles_found += 1
                vehicle_detections.append((box, class_name, confidence))
                print(f"   🚗 {vehicles_found}. {class_name}: {confidence:.2f} confidence")
        
        if vehicles_found == 0:
            print("   No vehicles detected in this image")
            continue
        
        print(f"   📊 Total vehicles in this image: {vehicles_found}")
        
        # Draw bounding boxes on the image
        for box, class_name, confidence in vehicle_detections:
            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # Choose color based on vehicle type
            if class_name == 'car':
                color = (0, 255, 0)  # Green for cars
            elif class_name == 'truck':
                color = (0, 0, 255)  # Red for trucks
            else:  # bus
                color = (255, 0, 0)  # Blue for buses
            
            # Draw rectangle
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            
            # Add label with background
            label = f"{class_name}: {confidence:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            cv2.rectangle(image, (x1, y1 - label_size[1] - 10), 
                         (x1 + label_size[0], y1), color, -1)
            cv2.putText(image, label, (x1, y1 - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Save the result
        output_name = f"detected_{os.path.basename(image_file)}"
        cv2.imwrite(output_name, image)
        print(f"   💾 Results saved as: {output_name}")
    
    # Final summary
    print(f"\n{'='*60}")
    print(f"🎉 Detection Complete!")
    print(f"📊 Total vehicles found across all images: {total_vehicles_found}")
    print(f"📁 Processed {len(image_files)} images")
    print("📁 Check the 'detected_*.jpg' files to see the results")
    
    # Legend
    print(f"\n🌈 Color Legend:")
    print(f"   🟢 Green = Cars")
    print(f"   🔴 Red = Trucks") 
    print(f"   🔵 Blue = Buses")

if __name__ == "__main__":
    detect_vehicles()