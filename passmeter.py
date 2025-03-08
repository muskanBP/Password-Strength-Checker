import re
import random
import string
import streamlit as st

# Blacklist of weak passwords
BLACKLISTED_PASSWORDS = {
    "password123", "12345678", "qwerty123", "letmein", "admin", "welcome",
    "123456", "password", "123456789", "1234567", "12345", "1234567890"
}

# Function to generate a strong password
def generate_strong_password(include_special=True):
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(12))  # Fixed length of 12 characters

# Function to check password strength
def check_password_strength(password):
    if password in BLACKLISTED_PASSWORDS:
        return "❌ This password is too common and easily guessed. Choose a different one.", 0, []

    score = 0
    feedback = []

    # Customizable scoring weights
    weights = {
        "length": 2 if len(password) >= 12 else 1 if len(password) >= 8 else 0,
        "uppercase": 1 if re.search(r"[A-Z]", password) else 0,
        "lowercase": 1 if re.search(r"[a-z]", password) else 0,
        "digit": 1 if re.search(r"\d", password) else 0,
        "special": 2 if re.search(r"[!@#$%^&*]", password) else 0,
    }

    # Evaluate strength
    score = sum(weights.values())

    # Feedback based on missing criteria
    if weights["length"] == 0:
        feedback.append("Password should be at least 8 characters long.")
    elif weights["length"] == 1:
        feedback.append("For a stronger password, use at least 12 characters.")
    if not weights["uppercase"]:
        feedback.append("Include at least one uppercase letter.")
    if not weights["lowercase"]:
        feedback.append("Include at least one lowercase letter.")
    if not weights["digit"]:
        feedback.append("Add at least one number (0-9).")
    if not weights["special"]:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score >= 6:
        return "✅ Strong Password!", score, feedback
    elif score >= 4:
        return "⚠️ Moderate Password - Consider strengthening it.", score, feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", score, feedback

# Streamlit UI
def main():
    st.title("🔐 Password Strength Meter & Generator")

    # Initialize session state for password
    if "generated_password" not in st.session_state:
        st.session_state.generated_password = ""
    if "password_input" not in st.session_state:
        st.session_state.password_input = ""

    # Username input
    username = st.text_input("Enter your username")

    # Password input with real-time strength feedback
    password = st.text_input(
        "Enter your password",
        type="password",
        placeholder="Leave blank to generate a password",
        value=st.session_state.password_input,  # Bind to session state
        key="password_field"  # Unique key for the input field
    )

    # Real-time strength meter
    if password:
        message, score, feedback = check_password_strength(password)
        progress_value = min(score / 6, 1.0)  # Ensure progress value is within [0.0, 1.0]
        st.progress(progress_value)  # Normalize score to 0-1 for progress bar
        st.write(message)
        if feedback:
            with st.expander("🔍 Password Suggestions"):
                for tip in feedback:
                    st.write(f"- {tip}")

        # Show Password Generator Options only if the password is weak
        if score < 6:  # Weak or Moderate password
            st.markdown("---")  # Add a horizontal line for separation
            st.subheader("Password Generator Options")

            # Include special characters checkbox
            include_special = st.checkbox(
                "Include Special Characters (!@#$%^&*)",
                value=True,
                help="Include special characters for added security."
            )

            # Generate password button
            if st.button("Generate Strong Password"):
                st.session_state.generated_password = generate_strong_password(include_special)
                st.success(f"Generated Password: `{st.session_state.generated_password}`")

            # Show "Use This Password" button only if a password has been generated
            if st.session_state.generated_password:
                if st.button("Use This Password"):
                    st.session_state.password_input = st.session_state.generated_password  # Update the password field
                    st.rerun()  # Refresh the app to reflect the change

    # Submit button
    if st.button("Submit"):
        if username and password:
            message, score, _ = check_password_strength(password)
            if score >= 6:
                st.success("🎉 Password created successfully!")
            else:
                st.error("⚠️ Improve your password before signing up.")
        else:
            st.error("Please fill in all fields.")

if __name__ == "__main__":
    main()
