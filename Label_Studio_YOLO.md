# Label Studio + YOLO Auto-Annotation Guide

## 🚀 Part 1: Install Label Studio

### Step 1.1: Install Label Studio
Open your **first terminal** and type:
```bash
pip install label-studio
```
Wait for it to finish installing.

### Step 1.2: Start Label Studio
In the **same terminal**, type:
```bash
label-studio
```

**✅ Success Check:**
- Your terminal should show: "Label Studio is running at http://localhost:8080"
- A web browser should open automatically
- If not, manually go to: http://localhost:8080

**⚠️ IMPORTANT: Keep this terminal open! Don't close it!**

---

## 🏗️ Part 2: Create Your Project

### Step 2.1: Create Account
- In the web browser, create a Label Studio account
- Use any email and password you want

### Step 2.2: Create New Project
1. Click **"Create Project"**
2. Give it a name like "My Object Detection Project"
3. Click **"Next"**

### Step 2.3: Choose Template
1. Select **"Computer Vision"** → **"Object Detection with Bounding Boxes"**
2. Click **"Next"**

### Step 2.4: Upload Your Images
1. Click **"Upload"** or drag and drop your images
2. Upload images 
3. Click **"Save"**

**✅ Success Check:**
- You should see your project with uploaded images
- Each image should appear as a thumbnail

---

## 🤖 Part 3: Set Up YOLO AI (The Magic Part!)

### Step 3.1: Download YOLO Code
Open a **NEW terminal window** (keep the first one running!). In this second terminal:

```bash
git clone https://github.com/HumanSignal/label-studio-ml-backend.git
cd label-studio-ml-backend
```

### Step 3.2: Install the YOLO Backend
In the **same second terminal**:
```bash
pip install -e .
```
Wait for installation to complete.

### Step 3.3: Go to YOLO Example
Still in the **second terminal**:
```bash
cd label_studio_ml/examples/yolo
```

### Step 3.4: Install YOLO Requirements
In the **second terminal**:
```bash
pip install -r requirements.txt
```
This will take several minutes as it downloads the YOLO AI model.

### Step 3.5: Start YOLO Service
In the **second terminal**:
```bash
label-studio-ml start . --port 9090
```

**✅ Success Check:**
- Terminal should show: "Starting Label Studio ML backend server"
- Go to http://localhost:9090 in your browser
- You should see: `{"model_class":"YOLO","status":"UP"}`

**⚠️ IMPORTANT: Keep both terminals open now!**

---

## 🔗 Part 4: Connect YOLO to Label Studio

### Step 4.1: Go Back to Label Studio
- Open http://localhost:8080 in your browser
- Click on your project

### Step 4.2: Access Machine Learning Settings
1. Click **"Settings"** (gear icon)
2. Click **"Model"** from the menu

### Step 4.3: Add YOLO Model
1. Click **"Add Model"**
2. In the URL field, type: `http://localhost:9090`
3. Click **"Validate and Save"**

**✅ Success Check:**
- You should see "YOLO" model listed as "Connected" with a green checkmark

---

## 🎪 Part 5: Use Auto-Annotation (The Fun Part!)

### Update labels
1. Click on **"Settings"**
2. Go to **"Label Interface"**
3. Update the code based on the object you want to detect
4. Click **"Save"**
5. Go back to **"Your Project Name"**

### Method 1: Batch Predictions (Recommended)
1. Go back to your project's main page
2. **Select multiple images** by checking ID box
3. Click **"Dropdown arrow"** next to Tasks
4. Select **"Retrieve Predictions"**
5. Wait 10-30 seconds
6. **Magic!** YOLO will automatically draw boxes around objects it finds

### Method 2: Individual Image Predictions
1. Click on any image to open the labeling interface
2. Look for **"Get Predictions"** or **"Auto-Label"** button
3. Click it to get YOLO predictions for that single image

---

## 🎯 Part 6: Understanding the Results

### What YOLO Can Detect
YOLO can automatically find and label these objects:
- People (person)
- Vehicles (car, truck, bicycle, motorcycle)
- Animals (dog, cat, horse, bird)
- Food items (banana, apple, sandwich, pizza)
- Sports equipment (ball, frisbee, skateboard)
- And 70+ other common objects!

### What You'll See
After running predictions:
- **Colored boxes** around detected objects
- **Labels** like "person", "car", "dog"
- **Confidence scores** (how sure YOLO is)

### Your Job
- **Review** the AI predictions
- **Fix** any mistakes (wrong labels, missing objects)
- **Add** objects YOLO missed
- **Delete** incorrect detections

---

## 🛠️ Troubleshooting

### Problem: "Command not found" errors
**Solution:** Make sure Python and pip are installed correctly.

### Problem: YOLO not connecting
**Solutions:**
1. Make sure both terminals are still running
2. Check that http://localhost:9090 shows the YOLO status
3. Try refreshing the Label Studio page

### Problem: No predictions appearing
**Solutions:**
1. Make sure your images are JPG or PNG format
2. Check that your project uses "Object Detection" template
3. Try with smaller images (under 5MB each)

### Problem: Wrong objects detected
This is normal! YOLO uses pre-trained knowledge. Your job is to:
- Correct wrong labels
- Add missing objects
- Delete false detections

---

## 📚 Summary

**What you accomplished:**
1. ✅ Set up Label Studio for image labeling
2. ✅ Connected YOLO AI for automatic object detection
3. ✅ Created a system that pre-labels your images
4. ✅ Learned to review and correct AI predictions

**Two terminals you need running:**
- **Terminal 1:** `label-studio` (Port 8080)
- **Terminal 2:** `label-studio-ml start . --port 9090` (Port 9090)

**Time saved:** Instead of manually drawing every box (2-3 minutes per image), you now just review AI predictions (10-30 seconds per image)!

---

## 🚀 Next Steps

1. **Practice:** Try with different types of images
2. **Export:** Use Label Studio's export feature to get your labeled data
3. **Train:** Use your labeled data to train custom AI models
4. **Share:** Show your friends this cool AI labeling setup!

**Remember:** The AI isn't perfect - your human review makes the final labels accurate and valuable for machine learning projects!

---

*Happy labeling! 🎉*