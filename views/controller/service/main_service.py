from flask_login import logout_user


def logout():
    logout_user()
    return 'Logged out successfully!'