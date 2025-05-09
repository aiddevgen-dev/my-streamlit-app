import streamlit as st

# Import Selenium for ChromeDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initialize in-memory user store
if "users" not in st.session_state:
    st.session_state.users = []

# Page title
st.title("🔐 User Registration & ChromeDriver Test (In-Memory)")

# Registration form
with st.form("registration_form", clear_on_submit=True):
    username = st.text_input("Username")
    email    = st.text_input("Email")
    pwd      = st.text_input("Password", type="password")
    confirm  = st.text_input("Confirm Password", type="password")
    submitted = st.form_submit_button("Register")

# Handle form submission
if submitted:
    if not username or not email or not pwd:
        st.error("❗ All fields are required.")
    elif pwd != confirm:
        st.error("❗ Passwords do not match.")
    else:
        st.session_state.users.append({
            "username": username.strip(),
            "email":    email.strip(),
            "password": pwd  # stored in plain-text for testing only
        })
        st.success(f"✅ Registered **{username}**")

# ChromeDriver test
st.markdown("---")
if st.button("🔍 Test ChromeDriver"):
    try:
        # Setup headless Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate and fetch title
        driver.get("https://www.google.com")
        title = driver.title
        driver.quit()

        st.success(f"ChromeDriver is working! Page title: {title}")
    except Exception as e:
        st.error(f"ChromeDriver failed: {e}")

# Optionally display all registered users
if st.checkbox("Show registered users"):
    st.subheader("📋 Registered Users")
    st.table(st.session_state.users)
