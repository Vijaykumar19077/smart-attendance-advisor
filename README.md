Smart Attendance Advisor

An AI + Fuzzy Logic based system that helps students understand their attendance situation and provides personalized attendance advice.

Project Overview

The Smart Attendance Advisor combines LangChain/LLM and Fuzzy Logic to analyze a student's attendance-related situation.

Students can enter their situation using natural language. The AI component understands the student's message and extracts relevant information such as attendance percentage, pending assignments, and days remaining until examinations.

The extracted information is then processed by a fuzzy inference system to calculate an attendance risk score.

Main Components

1. AI / LLM using LangChain

- Understands natural-language student queries.
- Extracts relevant attendance information.
- Generates a natural-language explanation of the final result.

2. Fuzzy Logic

The fuzzy inference system uses:

- Membership functions
- Fuzzification
- Fuzzy rules
- Rule evaluation
- Defuzzification

The system calculates an attendance risk score based on factors such as:

- Attendance percentage
- Days remaining until examination
- Pending assignments

3. User Interface

The project uses Streamlit to provide a simple web interface.

Project Flow

Student Input
↓
LangChain + LLM
↓
Information Extraction
↓
Fuzzy Inference System
↓
Risk Score
↓
AI-generated Explanation
↓
Attendance Advice

Technologies Used

- Python
- LangChain
- Large Language Model (LLM)
- Fuzzy Logic
- Streamlit
- GitHub

Project Objective

The objective of this project is to demonstrate how AI and fuzzy logic can be combined to create an intelligent attendance advisory system for students.

Author

Vijaykumar Naidu
