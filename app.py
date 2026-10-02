import streamlit as st
from fuzzy_logic import calculate_risk
from llm import extract_attendance_info

st.title("Smart Attendance Advisor")
st.write("AI + Fuzzy Logic based attendance advisory system")

st.subheader("Student Message")

student_message = st.text_area(
    "Describe your attendance situation",
    placeholder="Example: I attended 65 out of 90 classes, my exam is in 14 days and I have 3 assignments pending."
)

if st.button("Analyze with AI"):
    if student_message:
        result = extract_attendance_info(student_message)
        attendance, exam_days, assignments = map(float, result.split(","))

        st.subheader("AI Extracted Information")
        st.write(f"Attendance: {attendance}%")
        st.write(f"Days Until Exam: {int(exam_days)}")
        st.write(f"Pending Assignments: {int(assignments)}")

        score, category = calculate_risk(
            attendance,
            int(exam_days),
            int(assignments)
        )

        st.subheader("Attendance Risk")
        st.write(f"Risk Score: {score}")
        st.write(f"Risk Level: {category}")
    else:
        st.warning("Please enter your attendance situation.")
