#!/usr/bin/env python3
"""
Batch processing script - detect objects in all images at once
"""

from ultralytics import YOLO
import os

def batch_detect():
    """Process all images in current directory - car detection only"""
    print("🔄 Loading YOLO model for car detection...")
    model = YOLO('yolov8n.pt')
    
    # Find all images
    image_files = []
    for ext in ['.jpg', '.jpeg', '.png', '.bmp']:
        image_files.extend([f for f in os.listdir('.') if f.lower().endswith(ext)])
    
    if not image_files:
        print("❌ No images found!")
        return
    
    print(f"📁 Processing {len(image_files)} images for car detection...")
    
    # Process all images at once (faster)
    results = model(image_files)
    
    total_cars = 0
    
    # Save results - cars only
    for i, (result, image_file) in enumerate(zip(results, image_files)):
        print(f"\n🚗 {image_file}:")
        
        car_count = 0
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            
            if class_name.lower() in ['car', 'truck', 'bus']:
                car_count += 1
                confidence = float(box.conf[0])
                print(f"     - {class_name}: {confidence:.2f}")
        
        if car_count == 0:
            print("     No cars detected")
        else:
            print(f"   Cars detected: {car_count}")
            total_cars += car_count
        
        # Save image with only car detections
        import cv2
        image = cv2.imread(image_file)
        
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            
            if class_name.lower() in ['car', 'truck', 'bus']:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(image, label, (x1, y1-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        output_name = f"cars_batch_{i+1}_{image_file}"
        cv2.imwrite(output_name, image)
    
    print(f"\n✅ Batch car detection complete!")
    print(f"🚗 Total cars found across all images: {total_cars}")

if __name__ == "__main__":
    batch_detect()