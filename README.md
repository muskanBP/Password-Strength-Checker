# Password Strength Meter & Generator

A Python-based **Password Strength Meter & Generator** built using Streamlit. This tool helps users evaluate the strength of their passwords and generate strong, secure passwords.

---

## Features

1. **Password Strength Meter**:
   - Evaluates the strength of a password based on:
     - Length (minimum 8 characters, recommended 12+).
     - Presence of uppercase and lowercase letters.
     - Inclusion of digits (0-9).
     - Use of special characters (!@#$%^&*).
   - Provides real-time feedback and suggestions for improving weak passwords.

2. **Password Generator**:
   - Generates strong, secure passwords with:
     - Fixed length of 12 characters.
     - Option to include/exclude special characters.
   - Allows users to automatically use the generated password.

3. **Weak Password Blacklist**:
   - Rejects commonly used weak passwords (e.g., `password123`, `12345678`).
   - Displays a list of weak passwords to avoid.

4. **User-Friendly Interface**:
   - Built using Streamlit for a clean and intuitive GUI.
   - Real-time progress bar to visualize password strength.

---

## How to Use

1. **Enter a Password**:
   - Type your password in the input field.
   - The tool will evaluate its strength and provide feedback.

2. **Generate a Strong Password**:
   - If your password is weak, click **"Generate Strong Password"**.
   - A strong password will be generated for you.
   - Click **"Use This Password"** to automatically fill the password field.

3. **Submit**:
   - Click **"Submit"** to check if your password meets the strength requirements.
   - If the password is strong, you'll see a success message.

---

## Installation

### Prerequisites
- Python 3.7 or higher.
- Streamlit library.

### Steps
1. Clone the repository:
   ```bash
   git clone (https://github.com/muskanBP/password-strength-meter.git)
   cd password-strength-meter
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501` to use the tool.

---

## Code Structure

- **`app.py`**:
  - Main script containing the Streamlit UI and password evaluation logic.
  - Functions for password generation and strength checking.

- **`README.md`**:
  - Documentation for the project.

---



### Password Strength Meter
![Password Strength Meter](screenshots/strength_meter.png)

### Password Generator
![Password Generator](screenshots/password_generator.png)

### Weak Password Warning
![Weak Password Warning](screenshots/weak_password.png)

---


## Acknowledgments

- Built with ❤️ using (https://password-strength-checker-by-lisabp.streamlit.app/)).
- Inspired by the need for stronger password security practices.

---

## Contact

For questions or feedback, feel free to reach out:

- **Email**: ahchandio22@gmail.com
- **GitHub**: [muskanBP](https://github.com/muskanBP))

---

Enjoy using the **Password Strength Meter & Generator**! 🚀

---

 🚀

