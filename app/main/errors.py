from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('notfound.html'),404

@main.app_errorhandler(500)
def internal_error(error):
    return render_template('notfound.html'),500