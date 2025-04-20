import streamlit as st
from app.main import generate_learning_report
import io
from reportlab.pdfgen import canvas

# Set page configuration
st.set_page_config(page_title="AI Learning Assistant", layout="wide")
st.title("📚 Enhanced Learning Assistant")

# Step 1: User Input for Topic and Learning Objectives
topic = st.text_input("🎯 Enter a learning topic:")
objectives = st.text_area("📌 What are your learning objectives?", height=120)

# Step 2: Interactive follow-up questions
subtopics = st.text_input("🔍 Any specific subtopics or areas you’re interested in? (Optional)")

knowledge_level = st.selectbox(
    "🧠 How would you describe your current knowledge level?",
    ["Beginner", "Intermediate", "Advanced"]
)

learning_format = st.multiselect(
    "🧾 Preferred learning format (Select all that apply):",
    ["Text", "Examples", "Code Snippets", "Step-by-step explanations", "Visual Diagrams"]
)

# Session state to manage the generated report and interaction steps
if "report_generated" not in st.session_state:
    st.session_state.report_generated = False
if "final_report" not in st.session_state:
    st.session_state.final_report = ""
if "regeneration_requested" not in st.session_state:
    st.session_state.regeneration_requested = False

# Step 3: Trigger the Report Generation
if st.button("Generate Report") and topic and objectives:
    with st.spinner("Generating your personalized learning report..."):
        report = generate_learning_report(
            topic=topic,
            objectives=objectives,
            subtopics=subtopics,
            knowledge_level=knowledge_level,
            learning_format=learning_format
        )
        st.session_state.final_report = report
        st.session_state.report_generated = True
        st.session_state.regeneration_requested = False

# Step 4: Display Report and Ask for Feedback
if st.session_state.report_generated:
    st.markdown(st.session_state.final_report, unsafe_allow_html=True)

    st.subheader("💬 Is this report what you were looking for?")
    satisfied = st.radio("Please select one:", ["", "Yes, it's great!", "No, I want changes"], index=0)

    if satisfied == "No, I want changes":
        feedback = st.text_area("🛠️ What would you like to improve or change in the report?")
        if st.button("Regenerate with Feedback") and feedback:
            with st.spinner("Updating your report based on feedback..."):
                modified_objectives = f"{objectives}\n\nAdditional Feedback: {feedback}"
                new_report = generate_learning_report(
                    topic=topic,
                    objectives=modified_objectives,
                    subtopics=subtopics,
                    knowledge_level=knowledge_level,
                    learning_format=learning_format
                )
                st.session_state.final_report = new_report
                st.success("✅ Report successfully updated. Please scroll up to check it.")

# Step 5: Offer PDF download if report exists
if st.session_state.get("report_generated"):
    if st.button("📥 Download Report as PDF"):
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)
        lines = st.session_state["final_report"].split('\n')
        x, y = 40, 800
        for line in lines:
            if y < 50:
                pdf.showPage()
                y = 800
            pdf.drawString(x, y, line.strip())
            y -= 15
        pdf.save()
        buffer.seek(0)

        st.download_button(
            label="📄 Click here to download your report as PDF",
            data=buffer,
            file_name="learning_report.pdf",
            mime="application/pdf"
        )
