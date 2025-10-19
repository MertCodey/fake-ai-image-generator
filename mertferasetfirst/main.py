
from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from firebase_admin import initialize_app, firestore, auth

set_global_options(max_instances=10)

initialize_app()

from services import user_service, image_service

register_this_user = user_service.register_this_user
create_fake_image_url = image_service.create_fake_image_url


