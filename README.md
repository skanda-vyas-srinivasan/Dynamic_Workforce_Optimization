
# Dynamic Workforce Optimization App

**A web-based workforce optimization tool that assigns employees to tasks efficiently based on budget, availability, and flexible skill matching using a Mixed-Integer Linear Programming (MILP) model.**  

## Tech Stack
### Frontend
- React.js
- Material UI
- Axios
### Backend
- Flask
- PuLP



## How it Works: The Optimization Model
This project uses a **Mixed-Integer Linear Programming (MILP) model** to allocate employees to tasks efficiently. The **objective function** minimizes the **total cost** while satisfying the necessary constraints which consider **skill matching, availability, and budgetary requirements**

### The Decision Variables

Let:

-  $x_{e,t}$ be a **binary variable** (1 if employee \( e \) is assigned to task \( t \), 0 otherwise).
-  $c_e$ be the **hourly cost** of employee \( e \).
-  $d_t$ be the **duration** of task \( t \).
-  $m_{e,t}$ be the **match score** between employee \( e \) and task \( t \).

### The Objective Function
$$
\min \sum_{e \in E} \sum_{t \in T} x_{e,t} \left( \frac{c_e d_t}{\max(C)} - \beta m_{e,t} + \gamma c_e \right)
$$

where $\alpha$, $\beta$, and $\gamma$ are **tunable hyperparameters** to balance cost vs skill match importance.

###  Constraints
1. **Each task is assigned exactly one employee:**
   
$$
   \sum_{e \in E} x_{e,t} = 1, \quad \forall t \in T
$$

3. **Employee availability is not exceeded:**
   
$$
   \sum_{t \in T} x_{e,t} d_t \leq \text{availability}_e, \quad \forall e \in E
$$

4. **Budget constraint per task:**
   
$$
   \sum_{e \in E} x_{e,t} c_e d_t \leq \text{budget}_t, \quad \forall t \in T
  $$

5. **Total budget constraint:**
   
$$
   \sum_{e \in E} \sum_{t \in T} x_{e,t} c_e d_t \leq \text{total budget}
$$

6. **Minimum skill match constraints:**
   
$$
   x_{e,t} m_{e,t} \geq \text{threshold}, \quad \forall e, t
$$

7. **Binary assignment:**
   
$$
   x_{e,t} \in \{0,1\}, \quad \forall e, t
$$

## Contributors
#### **Developed by**: @skanda-vyas-srinivasan
#### LinkedIn: https://www.linkedin.com/in/skanda-vyas
#### email:skandavyas20@gmail.com
