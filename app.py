import streamlit as st
import random

# Title of the app
st.title("🌱 Growth Mindset App")
st.subheader("Boost your mindset with motivation & self-reflection!")

# Sidebar navigation
menu = st.sidebar.radio("📌 Select a Page", ["Home", "Daily Motivation", "Reflection Journal"])

# ---------------- Home Page ----------------
if menu == "Home":
    st.header("🏠 Welcome to the Growth Mindset App!")
    st.write("This app helps you stay motivated and develop a growth mindset with daily reflections.")

# ---------------- Daily Motivation Page ----------------
elif menu == "Daily Motivation":
    st.header("💡 Daily Motivation")

    # List of Motivational Quotes
    quotes = [
        "م پاکستان ایک مضبوط ملک ہے، اور کوئی بھی اسے ختم نہیں کر سکتا۔",
        "ہمیں اپنی زندگی میں سب سے پہلے محنت، محنت اور صرف محنت کو ترجیح دینی چاہیے۔",
        "امیابی کے لیے ہمیں اتحاد، سچے ایمان، اور قربانی کی روح کو اپنانا ہوگا۔",
        "Every day is a new beginning.",
        "Success comes from learning and persistence.",
        "Believe in yourself and your ability to improve."
        "We must always strive to be better than we were yesterday, and then be better than we were the day before, and so on."
    ]
    
    # Display a Random Quote
    if st.button("Show Motivation"):
        st.write(random.choice(quotes))

# ---------------- Reflection Journal Page ----------------
elif menu == "Reflection Journal":
    st.header("📖 Your Growth Reflection")

    # Text input for reflection
    reflection = st.text_area("Write about today's learning experience:")
    
    if st.button("Save Reflection"):
        if reflection:
            st.success("✅ Your reflection has been saved!")
        else:
            st.warning("⚠️ Please enter something before saving.")

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
st.sidebar.write("Made by💻 Rizwan Hussain")

