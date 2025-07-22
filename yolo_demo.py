#!/usr/bin/env python3
"""
Simple YOLO Object Detection Demo for Jetson Nano
Uses YOLOv8 to detect objects in images
"""

import cv2
import os
from ultralytics import YOLO

class YOLODetector:
    def __init__(self):
        print("🔄 Loading YOLO model...")
        # Load YOLOv8 nano model (smallest, fastest for Jetson Nano)
        self.model = YOLO('yolov8n.pt')
        print("✅ YOLO model loaded successfully!")
    
    def detect_objects(self, image_path):
        """Detect objects in an image"""
        if not os.path.exists(image_path):
            print(f"❌ Image not found: {image_path}")
            return None
        
        print(f"\n🔍 Processing: {image_path}")
        
        # Load image
        image = cv2.imread(image_path)
        if image is None:
            print(f"❌ Could not load image: {image_path}")
            return None
        
        # Run YOLO detection
        results = self.model(image)
        
        # Get the first result (we only passed one image)
        result = results[0]
        
        # Draw bounding boxes on image
        annotated_image = result.plot()
        
        # Print detection results
        print(f"📊 Detection Results for {os.path.basename(image_path)}:")
        print("-" * 40)
        
        # Filter for cars only (class_id 2 = car in YOLO)
        car_boxes = []
        car_count = 0
        
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = self.model.names[class_id]
            
            # Only keep cars (you can also add 'truck', 'bus' if needed)
            if class_name.lower() in ['car', 'truck', 'bus']:
                car_boxes.append(box)
                car_count += 1
                confidence = float(box.conf[0])
                print(f"   🚗 {car_count}. {class_name}: {confidence:.2f} confidence")
        
        if car_count == 0:
            print("   No cars detected in this image")
        else:
            print(f"   Total cars found: {car_count}")
        
        # Create new result with only car detections
        if car_boxes:
            # Create a copy of the original image
            filtered_image = cv2.imread(image_path)
            
            # Draw only car bounding boxes
            for box in car_boxes:
                # Get bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                class_name = self.model.names[class_id]
                
                # Draw rectangle
                cv2.rectangle(filtered_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Add label
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(filtered_image, label, (x1, y1-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            return filtered_image
        else:
            return None
        
        return annotated_image
    
    def save_result(self, image, original_path):
        """Save the detection result"""
        if image is None:
            return
        
        # Create output filename
        base_name = os.path.splitext(os.path.basename(original_path))[0]
        output_path = f"{base_name}_cars_detected.jpg"
        
        # Save image
        cv2.imwrite(output_path, image)
        print(f"💾 Car detection results saved as: {output_path}")

def main():
    """Main function"""
    print("🚀 Starting YOLO Object Detection Demo")
    print("=" * 50)
    
    # Initialize detector
    detector = YOLODetector()
    
    # Find image files
    image_extensions = ['.jpg', '.jpeg']
    image_files = []
    
    # Check current directory
    for file in os.listdir('.'):
        if any(file.lower().endswith(ext) for ext in image_extensions):
            image_files.append(file)
    
    # Check images folder if it exists
    if os.path.exists('images'):
        for file in os.listdir('images'):
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(f'images/{file}')
    
    if not image_files:
        print("❌ No image files found!")
        print("   Please add some .jpg or .png files to the current directory")
        print("   or create an 'images' folder with your images")
        return
    
    print(f"📁 Found {len(image_files)} image(s)")
    
    # Process each image
    for image_file in image_files:
        print(f"\n{'='*60}")
        
        # Detect objects
        result_image = detector.detect_objects(image_file)
        
        # Save result
        detector.save_result(result_image, image_file)
    
    print(f"\n🎉 Processed {len(image_files)} images successfully!")
    print("🚗 Check the '*_cars_detected.jpg' files to see the car detection results")

if __name__ == "__main__":
    main()