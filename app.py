from flask import Flask, request, jsonify
from new_optimize import optimize_workforce_with_flexible_skills  # Import the function

app = Flask(__name__)

@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        data = request.get_json()
        employees = data.get("employees", [])
        tasks = data.get("tasks", [])
        total_budget = data.get("total_budget", 10000)

        # Optional parameters
        alpha = data.get("alpha", 1.0)
        beta = data.get("beta", 0.5)
        gamma = data.get("gamma", 0.0001)
        min_match_threshold = data.get("min_match_threshold", 0.5)

        result = optimize_workforce_with_flexible_skills(
            employees, tasks, total_budget, 
            min_match_threshold=min_match_threshold, 
            alpha=alpha, beta=beta, gamma=gamma
        )

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
