from flask_login import login_required, logout_user


@login_required
def logout():
    logout_user()
    return 'Logged out successfully!'