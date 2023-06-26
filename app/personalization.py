import os
import hashlib
from PIL import Image
from flask import current_app
from werkzeug.utils import secure_filename

def save_picture(form_picture, user_email, user_id):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = secure_filename(f'{user_email}-{user_id}{f_ext}')
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
