# 🍽️ SmartChef AI

## RAG Based Indian Recipe Preparation Agent using IBM watsonx.ai & IBM Granite

![IBM](https://img.shields.io/badge/IBM-watsonx.ai-blue)
![Granite](https://img.shields.io/badge/IBM-Granite%204.0-blue)
![RAG](https://img.shields.io/badge/RAG-Enabled-green)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-orange)

---

# 📖 Project Overview

SmartChef AI is an intelligent Recipe Preparation Agent developed using IBM Build on IBM (BOB), IBM watsonx.ai, IBM Granite Models, and Retrieval-Augmented Generation (RAG).

The system helps users prepare delicious Indian recipes based on the ingredients available at home. Instead of searching the internet, SmartChef AI retrieves information from a trusted recipe knowledge base and generates personalized cooking recommendations.

---

# 🎯 Problem Statement

Many users struggle to decide what to cook with the ingredients available at home. Existing recipe platforms provide generic suggestions and often ignore dietary preferences, ingredient availability, cooking time, and regional tastes.

SmartChef AI solves this problem by using Retrieval-Augmented Generation (RAG) to retrieve recipes from a trusted knowledge base and generate accurate, personalized cooking recommendations.

---

# 🚀 Key Features

- Ingredient-Based Recipe Recommendation
- Indian Recipe Knowledge Base
- Smart Recipe Search using RAG
- Step-by-Step Cooking Instructions
- Ingredient Substitution Suggestions
- Preparation Time Estimation
- Serving Size Recommendation
- Cooking Tips
- Personalized Recipe Suggestions

---

# 🛠️ Technologies Used

- IBM Build on IBM (BOB)
- IBM watsonx.ai
- IBM Granite 4.0-8B-Instruct
- IBM Cloud Lite
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database

---

# 🏗️ System Architecture

User

↓

Chat Interface

↓

IBM Granite Model

↓

Recipe Knowledge Base (RAG)

↓

Vector Search

↓

Recipe Recommendation Agent

↓

Cooking Assistant

↓

SmartChef AI Response

---

# 📚 Knowledge Base

The knowledge base contains:

- Indian Recipes
- Ingredients
- Cooking Instructions
- Preparation Time
- Serving Size
- Cooking Tips

Supported Formats

- PDF
- JSON

---

# 💬 Sample Queries

• I have potato, tomato and onion.

• Suggest a healthy breakfast.

• Give me a paneer recipe.

• Suggest dinner under 30 minutes.

• What can I cook with rice and eggs?

---

# 📂 Project Structure

```
SmartChef-AI/
│
├── app.json
├── README.md
├── requirements.txt
├── LICENSE
│
├── docs/
│   ├── Project_Report.pdf
│   ├── Presentation.pptx
│
├── knowledge_base/
│   ├── Indian_Recipes.pdf
│   └── recipes.json
│
├── screenshots/
│
└── src/
    ├── app.py
    ├── rag.py
    ├── prompts.py
    └── utils.py
```

---

# 🔮 Future Scope

- Voice-Based Recipe Assistant
- Multi-Language Support
- Nutrition Analysis
- Grocery List Generation
- Meal Planner
- Smart Kitchen Integration

---

# 👨‍💻 Developer

**Utsav Singh**

B.Tech (Information Technology)

Dr. A.P.J. Abdul Kalam Technical University (AKTU)

📧 utsavsinghthc@gmail.com

---

# 📜 License

This project is developed for the **IBM SkillsBuild AICTE Project Submission 2026**.

MIT License

---

⭐ If you like this project, don't forget to star the repository.
