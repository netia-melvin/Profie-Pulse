from flask import Flask, jsonify
import requests

# Initialize Flask app
app = Flask(__name__)

# GitHub API Base URL
GITHUB_API_URL = "https://api.github.com/users/"

@app.route('/api/github/<username>', methods=['GET'])
def get_github_user_stats(username):
    try:
        # Make a request to GitHub's API
        response = requests.get(f"{GITHUB_API_URL}{username}")
        
        # Check if the request was successful
        if response.status_code == 200:
            user_data = response.json()
            # Return the relevant data in JSON format
            return jsonify({
                'username': user_data['login'],
                'public_repos': user_data['public_repos'],
                'followers': user_data['followers'],
                'following': user_data['following'],
                'created_at': user_data['created_at']
            }), 200
        else:
            # Return an error message if the user is not found
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        # Return a general error if something goes wrong
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
