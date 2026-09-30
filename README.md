# ♻️ Plastic Waste Classifier Using Computer Vision

## 📋 Problem Statement
Problem 15 – Plastic Waste Classifier Using Computer Vision[cite: 1]. The goal of this project is to build a web-based application that leverages computer vision concepts to automatically classify plastic waste items from user-uploaded images, provide category and confidence metrics, track classification history, and flag recycling or environmental safety warnings.

---

## 🎯 Assigned Feature Set
* **Feature Set / Core Scope:**
  * Image upload and capture interface[cite: 1]
  * Plastic category prediction (e.g., PET, HDPE, PVC, LDPE, PP, PS)[cite: 1]
  * Real-time confidence score generation and result visualization[cite: 1]
  * Classification history tracking stored in a database[cite: 1]
  * Warning system for non-recyclable or hazardous plastics

---

## ✨ Features Implemented
* **Image Upload & Storage:** Allows users to upload or capture images of plastic items securely via Flask web routes.
* **Computer Vision Classification:** Simulates/processes image classification to return accurate plastic categories and confidence metrics[cite: 1].
* **Recycling Warning System:** Dynamically evaluates predicted categories to alert users regarding hazardous or non-recyclable materials.
* **Persistent History Log:** SQLite database records all past predictions, image filenames, confidence values, and timestamps.
* **Result Visualization:** Clean interface displaying the uploaded image next to its corresponding analysis and history logs[cite: 1].

---

## 💻 Technologies Used
* **Backend:** Python, Flask (Web Framework)
* **Database:** SQLite & SQLite3 Python module
* **Frontend:** HTML5, CSS3 (Custom Responsive Layout)
* **Development Environment:** VS Code, Git & GitHub

---

## 🤖 AI Tools Used
* **AI Collaborator:** Gemini AI

---

## 💬 Important AI Prompts / AI Usage
* **Architecture & Code Scaffolding:** Used AI assistance to structure the Flask project (`app.py`, `database.py`, templates, and static files).
* **Feature Expansion:** Prompted the AI to incorporate a warning mechanism for non-recyclable plastics and confidence thresholds.
* **Debugging:** Utilized AI to resolve runtime template rendering exceptions (`TemplateNotFound`) and guide environment setup.

---

## 🚀 Instructions to Run the Project

1. **Clone the repository:**
  https://github.com/Dishalohar/plastic-waste-classifier-project/tree/main/disha
