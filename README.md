# Dynamic Workforce Optimization App

**A web-based workforce optimization tool that assigns employees to tasks efficiently based on budget, availability, and flexible skill matching using a Mixed-Integer Linear Programming (MILP) model.**  

## How it Works: The Optimization Model
This project uses a **Mixed-Integer Linear Programming (MILP) model** to allocate employees to tasks efficiently. The **objective function** minimizes the **total cost** while satisfying the necessary constraints which consider **skill matching, availability, and budgetary requirements**

### The Decision Variables
Let:
- \( x_{e,t} \) be a **binary variable** (1 if employee \( e \) is assigned to task \( t \), 0 otherwise).
- \( c_e \) be the **hourly cost** of employee \( e \).
- \( d_t \) be the **duration** of task \( t \).
- \( m_{e,t} \) be the **match score** between employee \( e \) and task \( t \).
