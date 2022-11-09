# Jupyter Notebook Render

$f(x)$


## code block

```python
print(1+2)
```

``` py title="bubble_sort.py"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```


## Math Jax3

A random variable $X$ is continuous if its distribution function $F(X) = P(X \leq x)$ can be written as

$$F(X) = \int_x^\infty f(u) du$$

for some integrable $f:R \to [0, \infty)$. The function  is called the probability density function of the continuous random variable . For instance, the probability density function of the normal distribution is


$$
\begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_t \\ \vdots \\ y_N \end{bmatrix} = \begin{bmatrix} 1 & x_{12} & \cdots & x_{1k} \\ 1 & x_{22} & \cdots & x_{2k} \\ \vdots & \vdots & \vdots \\ 1 & x_{t2} & \cdots & x_{tk} \\ \vdots & \vdots & \vdots \\ 1 & x_{N2} & \cdots & x_{Nk} \end{bmatrix} \begin{bmatrix} \beta_1 \\ \beta_2 \\ \vdots \\ \beta_t \\ \vdots \\ \beta_k \end{bmatrix} + \begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_t \\ \vdots \\ u_N \end{bmatrix}
$$