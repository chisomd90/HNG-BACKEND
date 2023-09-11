from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate track and calculate UTC time
    if slack_name is None or track is None:
        return jsonify({'error': 'Missing parameters'}), 400

    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get GitHub URLs
    script_url = os.environ.get('SCRIPT_URL', 'https://github.com/HNG-BACKEND/main.py')
    source_code_url = os.environ.get('SOURCE_CODE_URL', 'https://github.com/HNG-BACKEND')

    # Construct the response JSON
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': script_url,
        'github_repo_url': source_code_url,
        'status_code': 200
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)