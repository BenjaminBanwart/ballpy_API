from flask import Blueprint, request, jsonify
from . import models
import json

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        reptile = request.form['reptile']
        name = request.form['name']

        new_reptile = models.Reptile(reptile=reptile, name=name)
        models.db.session.add(new_reptile)
        models.db.session.commit()

        return 'success!'

    big_dict = {
        'data': []
    }
    results = models.Reptile.query.all()
    for result in results:
        big_dict['data'].append({
            'id': result.id,
            'reptile': result.reptile,
            'name': result.name
        })

    return big_dict

@bp.route('/<int:id>')
def show(id):
    result = models.Reptile.query.filter_by(id=id).first()
    result_dict = {
        'id': result.id,
        'reptile': result.reptile,
        'name': result.name
    }
    return result_dict
