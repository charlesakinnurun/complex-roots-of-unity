# 🔢 Fifth Roots of Unity with SymPy

This project uses **Python** and **SymPy** to solve the complex equation:

$$
z^5 = 1
$$

The program calculates all **five complex roots of unity** symbolically and displays them in a clean mathematical format using Jupyter/IPython.

## 📌 Project Overview

The equation

$$
z^5 = 1
$$

has exactly **five complex solutions**. These solutions are known as the **5th roots of unity**.

They can be expressed mathematically as:

$$
z_k = e^{2\pi i k/5}, \qquad k=0,1,2,3,4
$$

The project demonstrates how **SymPy** can automatically solve polynomial equations involving complex numbers.

## 🛠️ Technologies Used

* **Python**
* **SymPy** – symbolic mathematics and equation solving
* **IPython.display** – rendering mathematical expressions
* **Jupyter Notebook** – interactive execution and visualization

## 💻 Code

```python
import sympy as sp
from IPython.display import display, Math

z = sp.symbols('z')

equation = sp.Eq(z**5, 1)
roots = sp.solve(equation, z)

display(Math(r"\boxed{z^5 =1 }"))
display(Math(r"\text{The 5 complex roots are:}"))

for i, root in enumerate(roots, 1):
    display(Math(
        rf"z_{i} = {sp.latex(root)}"
    ))
```

## 🧠 How It Works

### 1. Import SymPy

```python
import sympy as sp
```

SymPy provides tools for symbolic mathematics, including solving equations exactly.

### 2. Create the Symbol

```python
z = sp.symbols('z')
```

This creates `z` as a symbolic variable.

### 3. Define the Equation

```python
equation = sp.Eq(z**5, 1)
```

This represents:

$$
z^5 = 1
$$

### 4. Solve the Equation

```python
roots = sp.solve(equation, z)
```

SymPy calculates all five solutions, including the complex roots.

### 5. Display the Equation

```python
display(Math(r"\boxed{z^5 =1 }"))
```

This renders the equation in LaTeX format.

### 6. Display Each Root

```python
for i, root in enumerate(roots, 1):
    display(Math(
        rf"z_{i} = {sp.latex(root)}"
    ))
```

Each solution is converted into LaTeX and displayed as a mathematical expression.

## 📐 Mathematical Background

The general formula for the \(n\)-th roots of unity is:

$$
z_k = e^{2\pi i k/n}
$$

For \(n=5\):

$$
z_k = e^{2\pi i k/5}
$$

where:

$$
k = 0,1,2,3,4
$$

Therefore, the five roots are located equally around the **unit circle** in the complex plane.

In rectangular form, they can be represented using sine and cosine:

$$
z_k =
\cos\left(\frac{2\pi k}{5}\right)
+
i\sin\left(\frac{2\pi k}{5}\right)
$$

## 🚀 Installation

Install the required packages with:

```bash
pip install sympy ipython jupyter
```

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/fifth-roots-of-unity.git
```

Navigate into the project:

```bash
cd fifth-roots-of-unity
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Run the notebook containing the Python code.

## 📊 Expected Result

The program displays:

```text
z⁵ = 1

The 5 complex roots are:

z₁ = 1
z₂ = ...
z₃ = ...
z₄ = ...
z₅ = ...
```

SymPy represents the complex solutions symbolically, allowing the exact mathematical structure of the roots to be preserved.

## 🎯 Learning Objectives

This project demonstrates:

* Solving polynomial equations with **SymPy**
* Working with **complex numbers**
* Understanding **roots of unity**
* Using symbolic mathematics in Python
* Generating LaTeX mathematical expressions
* Displaying mathematical formulas in Jupyter Notebook
* Iterating through symbolic solutions

## 🔮 Possible Improvements

Future versions could:

* Plot the five roots on the complex plane.
* Draw the unit circle.
* Add numerical approximations of the roots.
* Generalize the program to calculate the \(n\)-th roots of unity.
* Create an interactive visualization using Matplotlib.

## 📚 Key Concept

The **5th roots of unity** are five complex numbers whose fifth power equals 1:

$$
\boxed{z^5 = 1}
$$

They form a regular **pentagon** when plotted on the unit circle.

---

⭐ **If you found this project useful, consider giving the repository a star!**
