from flask import Flask, request, jsonify
from flask_cors import CORS
from agent.executor import AgentExecutor

app = Flask(__name__)
CORS(app) # Allow cross-origin requests from the Electron/Vite frontend

# Initialize the Sara-Brain brain
executor = AgentExecutor()

@app.route("/api/execute", methods=["POST"])
def execute_goal():
    data = request.json
    goal = data.get("goal")
    
    if not goal:
        return jsonify({"error": "No goal provided"}), 400
        
    try:
        print(f"[API] Received goal: {goal}")
        # Execute the agent synchronously and return the final summary
        result = executor.execute(goal=goal)
        return jsonify({"result": result, "status": "success"})
    except Exception as e:
        print(f"[API Error] {str(e)}")
        return jsonify({"error": str(e), "status": "error"}), 500

if __name__ == "__main__":
    print("[SARA] Sara-Brain API Server running on port 5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
