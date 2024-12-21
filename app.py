from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Facebook login route
@app.route('/login/facebook')
def login_facebook():
    # Redirect to Facebook login (placeholder logic)
    return redirect("https://www.facebook.com/")

# VK login route
@app.route('/login/vk')
def login_vk():
    # Redirect to VK login (placeholder logic)
    return redirect("https://vk.com/")

# Error handling route (optional)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
