import os

from flask import Blueprint, request, redirect, flash
from werkzeug.utils import secure_filename

from backend.models import db, File

bp = Blueprint('main', __name__)


@bp.route('/')
def hello():
    return 'Hello, World!'


@bp.route('/ping')
def ping():
    return 'Pong!'


@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    users = request.form.get('users')
    if not users:
        flash('No users specified')
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
        file.save(file_path)

        # Save file info in the database
        new_file = File(filename=filename, users=users)
        db.session.add(new_file)
        db.session.commit()

        return f'File successfully uploaded to {file_path}', 200

    return 'File upload failed', 400


@bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    user = request.args.get('user')
    if not user:
        return 'User not specified', 400

    file_record = File.query.filter_by(filename=filename).first()
    if not file_record:
        return 'File not found', 404

    if user not in file_record.owners():
        return f'User {user} does not have access to file {filename}', 403

    return f'Downloading file {filename}', 200


@bp.route('/files', methods=['GET'])
def list_files():
    files = File.query.all()
    return {'files': [file.filename for file in files]}
