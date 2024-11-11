from flask import Flask, request, jsonify
from sqled import generate_sql_response
import os
app = Flask(__name__)

@app.route('/generate_sql', methods=['POST'])
def generate_sql():
    data = request.json
    user_input = data.get('prompt')
    
    if not user_input:
        return jsonify({"error": "Please enter a valid query."}), 400

    # Generate SQL response using generate_sql_response function
    sql_response = generate_sql_response(user_input)
    sql_query = sql_response.candidates[0].content.parts[0].text

    # Clean SQL query
    cleaned_sql_query = sql_query.replace("```sql\n", "").replace("```", "").strip()

    # Return the cleaned SQL query as a JSON response
    return jsonify({"query": cleaned_sql_query})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
