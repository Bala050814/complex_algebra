import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Load custom CSS
def local_css():
    st.markdown("""
    <style>
        body {
            background-color: #12141c;
            color: #40E0D0;
            font-family: 'Courier New', monospace;
        }
        .stApp {
            background-color: #12141c;
        }
        h1, h2, h3 {
            color: #ffffff;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            transition: 0.3s ease;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #45a049;
            transform: scale(1.03);
        }
        .stTextInput input,
        .stNumberInput input {
            background-color: #1f2230;
            color: #ffffff;
            border-radius: 5px;
        }
        .stSelectbox div {
            background-color: #1f2230 !important;
            color: #ffffff !important;
        }
        .footer {
            margin-top: 30px;
            color: #888;
            text-align: center;
            font-size: 0.8rem;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Function to plot complex numbers and results
def plot_complex_numbers(z1, z2, operation):
    z1_real, z1_imag = z1.real, z1.imag
    z2_real, z2_imag = z2.real, z2.imag

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color='gray')
    ax.axvline(0, color='gray')

    ax.plot([0, z1_real], [0, z1_imag], 'ro-', label=f"z₁ = {z1}")
    ax.plot([0, z2_real], [0, z2_imag], 'bo-', label=f"z₂ = {z2}")

    try:
        if operation == "Addition":
            result = z1 + z2
            label = f"z₁ + z₂ = {result}"
            ax.plot([0, result.real], [0, result.imag], 'go-', label=label)
        elif operation == "Subtraction":
            result = z1 - z2
            label = f"z₁ - z₂ = {result}"
            ax.plot([0, result.real], [0, result.imag], 'yo-', label=label)
        elif operation == "Multiplication":
            result = z1 * z2
            label = f"z₁ × z₂ = {result}"
            ax.plot([0, result.real], [0, result.imag], 'mo-', label=label)
        elif operation == "Division":
            if z2 == 0:
                st.error("Division by zero is undefined.")
                return
            result = z1 / z2
            label = f"z₁ ÷ z₂ = {result}"
            ax.plot([0, result.real], [0, result.imag], 'co-', label=label)
        elif operation == "Modulus (|z1|)":
            result = abs(z1)
            label = f"|z₁| = {result:.2f}"
            ax.text(z1_real + 0.5, z1_imag, label, fontsize=12, color='lime')
        elif operation == "Argument (arg(z1))":
            result = np.angle(z1, deg=True)
            label = f"arg(z₁) = {result:.2f}°"
            ax.text(z1_real + 0.5, z1_imag, label, fontsize=12, color='yellow')
        elif operation == "Conjugate of z1":
            result = np.conj(z1)
            label = f"Conj(z₁) = {result}"
            ax.plot([0, result.real], [0, result.imag], 'co--', label=label)
        elif operation == "Exponentiation (z1^z2)":
            result = z1 ** z2
            label = f"z₁ ^ z₂ = {result}"
            ax.plot([0, result.real], [0, result.imag], 'ko-', label=label)
        elif operation == "Logarithm (log(z1))":
            if z1 == 0:
                st.error("Logarithm of zero is undefined.")
                return
            result = np.log(z1)
            label = f"log(z₁) = {result}"
            ax.plot([0, result.real], [0, result.imag], 'ro--', label=label)

        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_xlabel('Re(z)', color='white')
        ax.set_ylabel('Im(z)', color='white')
        ax.set_title(f'Operation: {operation}', color='white')
        ax.legend()
        ax.grid(True)
        fig.patch.set_facecolor('#1f2230')
        ax.set_facecolor('#1f2230')
        ax.tick_params(colors='white')

        st.markdown(f"### ✅ Result: `{label}`")
        st.pyplot(fig, use_container_width=True)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# Streamlit UI
st.title("🧮 Complex Number Operations Visualizer")
st.markdown("Explore mathematical operations with complex numbers and visualize them in the Argand plane.")

# Inputs
st.markdown("### 🔢 Enter Complex Numbers")

col1, col2 = st.columns(2)
with col1:
    z1_real = st.number_input("Real part of z₁", value=3.0)
    z1_imag = st.number_input("Imaginary part of z₁", value=2.0)
with col2:
    z2_real = st.number_input("Real part of z₂", value=1.0)
    z2_imag = st.number_input("Imaginary part of z₂", value=4.0)

z1 = complex(z1_real, z1_imag)
z2 = complex(z2_real, z2_imag)

operation = st.selectbox("📘 Choose Operation", [
    "Addition", "Subtraction", "Multiplication", "Division",
    "Modulus (|z1|)", "Argument (arg(z1))", "Conjugate of z1",
    "Exponentiation (z1^z2)", "Logarithm (log(z1))"
])

if st.button("🔍 Visualize Operation"):
    plot_complex_numbers(z1, z2, operation)

# Footer
st.markdown(f"<div class='footer'>© {datetime.now().year} ComplexCalc. Built with 💚 and Python</div>", unsafe_allow_html=True)

