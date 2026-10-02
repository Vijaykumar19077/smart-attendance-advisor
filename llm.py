import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.environ["GROQ_API_KEY"],
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
Extract these three values from the student's message:

attendance_percentage
exam_days
pending_assignments

Student message:
{student_input}

Reply with ONLY three numbers separated by commas.
Example:
65, 14, 3
""")

chain = prompt | llm

def extract_attendance_info(student_input):
    response = chain.invoke({"student_input": student_input})
    return response.content
