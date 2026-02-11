# Quantum Computing Foundations: Mathematical Simulations

This repository is a modular exploration of the mathematical principles that govern quantum computing. Using **Python**, **NumPy** **Pandas** and **Matplotlib**, I have built simulations to visualize how linear algebra translates into quantum operations.

## 🔬 Core Modules

Each notebook is designed as an interactive experiment. You can view the code directly on GitHub or run it in Google Colab:

### 1. Vector Space & Qubit Representation
* **Focus:** Fundamental representation of qubits as unit vectors in Hilbert space.
* **Key Concepts:** Vector normalization (`np.linalg.norm`), statevector definitions, and probability amplitudes.
* **Options:**
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1eTZ9K7EdlDllk1X4dhBKq9Pu5SgW97Vt?usp=sharing)
* 📂 **[Download from Repository](./notebooks/Vector.ipynb)**: Access the source file directly for local execution or custom environments.

### 2. The Quantum Gate Simulator
* **Focus:** Visualizing how logic gates transform qubit states through matrix multiplication.
* **Key Concepts:** **Pauli-X (NOT) Gate** implementation, Determinants (area preservation), and **Eigenvectors** (symmetry axes of quantum pulses).
* **Options:**
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1RBsqKTMIrHrhSflCUk8tb8tg5QCfyBg6?usp=sharing)
* 📂 **[Download from Repository](./notebooks/The_Quantum_Gate_Simulator.ipynb)**: Access the source file directly for local execution or custom environments.

### 3. The Quantum Clock (Unitary Rotations)
* **Focus:** Demonstrating that unitary matrices rotate vectors without changing their magnitude.
* **Key Concepts:** **Rotation Matrices ($\theta$)**, verifying the Unitary property (det = 1), and tracking state evolution across the unit circle.
* **Options:**
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qVZXYojP5Sb7DkJ1vJt6hUneV4YlDKbL?usp=sharing)
* 📂 **[Download from Repository](./notebooks/The_Quantum_Clock.ipynb)**: Access the source file directly for local execution or custom environments.

---

## 🛠️ Technical Implementation
* **Language:** Python 3.x
* **Linear Algebra:** NumPy (Core engine for matrix operations and vector calculus).
* **Data Analysis:** Pandas for organizing state coordinates.
* **Visualization:** Matplotlib for plotting quantum state transformations and unit circles.

## 🎯 About this Project
This project reflects my interest in **Scientific Outreach** and **Quantum Engineering**. By building these simulators from scratch, I aim to bridge the gap between abstract complex-number mathematics and practical software development.
