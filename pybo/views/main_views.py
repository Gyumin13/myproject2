from flask import Blueprint, render_template


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def main_site():
   return render_template('main_cover.html')


@bp.route('/language')
def language_site():
   return render_template('language.html')


@bp.route('/science')
def science_site():
   return render_template('science.html')


@bp.route('/computer_engineering')
def ComputerEngineering_site():
   return render_template('ComputerEngineering.html')


@bp.route('/nursing')
def nursing_site():
   return render_template('nursing.html')