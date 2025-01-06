# Dynamic Workforce Optimization App

**A web-based workforce optimization tool that assigns employees to tasks efficiently based on budget, availability, and flexible skill matching using a Mixed-Integer Linear Programming (MILP) model.**  

## How it Works: The Optimization Model
This project uses a **Mixed-Integer Linear Programming (MILP) model** to allocate employees to tasks efficiently. The **objective function** minimizes the **total cost** while satisfying the necessary constraints which consider **skill matching, availability, and budgetary requirements**

### The Decision Variables
Let:

$$
x_{e,t} \text{ is a binary variable} \quad (1 \text{ if employee } e \text{ is assigned to task } t, 0 \text{ otherwise}).
$$

$$
c_e \text{ is the hourly cost of employee } e.
$$

$$
d_t \text{ is the duration of task } t.
$$

$$
m_{e,t} \text{ is the match score between employee } e \text{ and task } t.
$$
