import streamlit as st

st.write("🚀 Hello, Streamlit is running!")
# Initialize in-memory “database”
if "users" not in st.session_state:
    st.session_state.users = []

st.title("🔐 User Registration (In-Memory, No DB)")

with st.form("registration_form", clear_on_submit=True):
    st.subheader("Create a new account (test only)")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    submitted = st.form_submit_button("Register")

if submitted:
    # Basic validation
    if not username or not email or not password:
        st.error("❗ All fields are required.")
    elif password != confirm:
        st.error("❗ Passwords do not match.")
    else:
        # “Persist” in session_state
        st.session_state.users.append({
            "username": username.strip(),
            "email": email.strip(),
            "password": password  # plain-text here just for testing!
        })
        st.success(f"✅ Registered **{username}** (in-memory)")

# For testing: show the list of “registered” users
if st.checkbox("Show registered users"):
    st.subheader("📋 Registered Users")
    st.table(st.session_state.users)
