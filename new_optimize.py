from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpStatus, PULP_CBC_CMD

def optimize_workforce_with_flexible_skills(employees, tasks, total_budget, min_match_threshold=0.5,alpha=1,beta=0.5,gamma=0.0001):

    prob = LpProblem("Dynamic_Workforce_Optimization", LpMinimize)

    # Match Score Value
    match_scores = {
        (e["id"], t["id"]): len(set(t["skills"]).intersection(set(e["skills"]))) / len(t["skills"])
        for e in employees for t in tasks
    }

    # Decision Variables
    decision_vars = LpVariable.dicts("Assign", [(e["id"], t["id"]) for e in employees for t in tasks], cat="Binary")

    # Normalize costs w.r.t max cost
    max_cost = max(e["hourly_cost"] * t["duration"] for e in employees for t in tasks)

    if(max_cost==0): max_cost = 1

    # Objective function
    prob += lpSum(
         decision_vars[e["id"], t["id"]] * ((alpha*e["hourly_cost"] * t["duration"]) / max_cost - beta * match_scores[(e["id"], t["id"])] + gamma * e["hourly_cost"] ) 
        for e in employees for t in tasks
    )

    # Constraints
    for t in tasks:
        #Only one assignment per task
        prob += lpSum(decision_vars[e["id"], t["id"]] for e in employees) == 1, f"Task_{t['id']}_Assignment"

        # Ensure the task budget is maintained
        prob += lpSum(
            decision_vars[e["id"], t["id"]] * e["hourly_cost"] * t["duration"] for e in employees
        ) <= t["budget"], f"Task_{t['id']}_Budget"

    for e in employees:
        # Ensure employee availability is maintained
        prob += lpSum(
            decision_vars[e["id"], t["id"]] * t["duration"] for t in tasks
        ) <= e["availability"], f"Employee_{e['id']}_Availability"

    # Adjust constraints to allow employees with 0 match if no other options exist
    for t in tasks:
        available_employees = [e for e in employees if match_scores[(e["id"], t["id"])] >= min_match_threshold]
        if not available_employees:  # If no employee meets the threshold, allow the best available
             best_match = min(
                employees, key=lambda e: (1 - match_scores[(e["id"], t["id"])], e["hourly_cost"])
                )
             prob += decision_vars[best_match["id"], t["id"]] == 1, f"Force_Assignment_Task_{t['id']}"

    # Total budget constraint
    prob += lpSum(
        decision_vars[e["id"], t["id"]] * e["hourly_cost"] * t["duration"]
        for e in employees for t in tasks
    ) <= total_budget, "Total_Budget_Constraint"

    # Solve the problem
    prob.solve(PULP_CBC_CMD(msg=0))

    # Check solver status
    status = LpStatus[prob.status]
    if status != "Optimal":
        return {"status": status, "objective_value": None, "assignments": []}

    # Extract results
    assignments = []
    for e in employees:
        for t in tasks:
            if decision_vars[e["id"], t["id"]].value() == 1:
                assignments.append({
                    "employee": e["name"],
                    "task": t["name"],
                    "match_score": match_scores[(e["id"], t["id"])]
                })

    return {"status": status, "assignments": assignments}

