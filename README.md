*AI-Powered Food Redistribution System* is a full-stack web application that connects surplus-food *Donors* (restaurants, events, households) with *Receivers* (NGOs, shelters, individuals).  
The platform uses an *AI-based matching algorithm* to intelligently pair donations with receivers based on food requirements, ensuring reduced wastage and better food accessibility.

> *Author:* [Hasan Kauchali](https://github.com/SadafKauchali)  
> *Tech Stack:* Flask • MySQL • Matplotlib • Bootstrap  
> *Status:* Completed and Demo-Ready  

---

## 🔍 Project Overview

This system streamlines the food donation process by bridging the gap between those who have surplus food and those who need it.  
It simplifies food distribution, improves transparency, and supports social good with data-driven reports.

### 🎯 Key Objectives
- Facilitate easy registration for donors and receivers  
- Record donations and requests in a centralized system  
- Implement an AI-based *donor–receiver matching engine*  
- Enable receivers to get food as per actual needs  
- Provide *reports and analytics with Matplotlib*  
- Enhance transparency with structured distribution tracking  

---

## 🖼️ Screenshots

### 🏠 Home Page
![Home](Screenshots/home.png)

### 🍛 Donor Form
![Donate Food](Screenshots/donor.png)

### 🏢 Receiver Form
![Receiver Request](Screenshots/receiver.png)

### 🤝 AI Matching
![Matching](Screenshots/match.png)

### 📊 Reports & Analytics
![Reports](Screenshots/reports.png)

---

## 🧠 Technology Stack

### Frontend – Bootstrap + Jinja Templates
- HTML5, CSS3, Bootstrap  
- Jinja2 templating for Flask  
- Responsive forms & tables  

### Backend – Flask
- Python Flask framework  
- RESTful routes for CRUD operations  
- AI-based text matching (food details ↔ food needed)  

### Database – MySQL
- Structured schema with *donors, receivers, donations, distributions*  
- Referential integrity with foreign keys  
- Sample data for quick testing  

### Analytics – Matplotlib
- Visual charts for donor/receiver stats  
- Food distribution reports over time  

---

## ⚙️ Core Functionalities

### For Donors:
- Register donor details (name, type, location)  
- Add donation details (food type, quantity)  
- View donation history  

### For Receivers:
- Register receiver details (name, type, location)  
- Request food with specific needs  
- View request history  

### AI Matching:
- Matches donor food details with receiver needs  
- Records successful distributions automatically  
- Supports scalable AI improvement (NLP/fuzzy matching)  

### Reports & Analytics:
- Donations by type (pie chart)  
- Receivers by type (bar chart)  
- Timeline of food distributions (line chart)  

---

## 🚀 Getting Started

### 1. Backend Setup (Flask)
```bash
git clone https://github.com/<your-username>/AI-Food-Redistribution.git
cd AI-Food-Redistribution
pip install -r requirements.txt
python app.py
