from flask import Flask , render_template, redirect, url_for, request, session


app = Flask(__name__)
app.secret_key = 'admin'  # Replace with a secure key


@app.route("/home")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


# Add login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return redirect(url_for('admin_dashboard'))
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html',title='Login', error=error)



# Route for admin dashboard
@app.route('/admin')
def admin_dashboard():
    if 'username' in session and session['username'] == 'admin':
        sales_data = {
            'items_delivered': 649,
            'refund_requests': 114,
            'cancelled_orders': 98,
            'new_users': 208,
        }
        return render_template(
            'admin_dashboard.html',
            data=sales_data,
            breadcrumb_item='Dashboard',
            breadcrumb_item_active='Admin',
            title='Admin Dashboard'
        )
    else:
        return redirect(url_for('login'))
    


# Route for logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/color')
def color_page():
    return render_template('bc_color.html', title='Color',breadcrumb_item='Elements',
        breadcrumb_item_active='Color')

@app.route('/typography')
def typography_page():
    return render_template(
        'bc_typography.html',
        title='Typography',breadcrumb_item='Elements',
        breadcrumb_item_active='Typography'
    )

@app.route('/icon')
def icon_page():
    return render_template(
        'icon-material.html',
        title='Icon',breadcrumb_item='Ions',
        breadcrumb_item_active='Material Icons'
    )


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/feature")
def feature():
    return render_template("feature.html")

@app.route("/how-to-use")
def how_to_use():
    return render_template("how-to-use.html")

@app.route("/testimonial")
def testimonials():
    return render_template("testimonial.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/404")
def page_not_found():
    return render_template("404.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
