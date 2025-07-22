#!/usr/bin/env python3
"""
Ultra-simple YOLO demo - One image, basic detection
"""

from ultralytics import YOLO
import cv2
import os

def simple_detect(image_path):
    """Simple car detection function"""
    print(f"Loading YOLO model for car detection...")
    model = YOLO('yolov8n.pt')  # Downloads automatically first time
    
    print(f"Looking for cars in {image_path}...")
    results = model(image_path)
    
    # Show results - filter for cars only
    result = results[0]
    car_count = 0
    
    print(f"\n🚗 Car Detection Results:")
    
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        
        # Only show cars, trucks, and buses
        if class_name.lower() in ['car', 'truck', 'bus']:
            car_count += 1
            confidence = float(box.conf[0])
            print(f"  {car_count}. {class_name}: {confidence:.2f}")
    
    if car_count == 0:
        print("  No cars detected in this image")
        return
    
    # Save result with only car bounding boxes
    import cv2
    image = cv2.imread(image_path)
    
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        
        if class_name.lower() in ['car', 'truck', 'bus']:
            # Draw bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])
            
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{class_name}: {confidence:.2f}"
            cv2.putText(image, label, (x1, y1-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    output_name = f"cars_detected_{os.path.basename(image_path)}"
    cv2.imwrite(output_name, image)
    print(f"\nSaved car detection results as: {output_name}")
    print(f"Total cars found: {car_count}")

if __name__ == "__main__":
    # Find first image file
    image_files = [f for f in os.listdir('.') 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if image_files:
        simple_detect(image_files[0])
    else:
        print("Please add an image file (.jpg or .png) to this directory")