import os
from PIL import Image
from flask import current_app
from werkzeug.utils import secure_filename  # Add this line

def save_picture(form_picture):
    picture_fn = secure_filename(form_picture.filename)
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
