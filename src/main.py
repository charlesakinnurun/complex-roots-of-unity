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