from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from firebase_admin import initialize_app, firestore, auth
from constants import DEFAULT_CREDITS_PER_NEW_USER
db = firestore.client()

@https_fn.on_call()
def register_this_user(req: https_fn.CallableRequest) -> dict:

    data = req.data

    if not data.get('username') or not data.get('password'):
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message="Username and password are required"
        )
    
    try:  
        user_ref = db.collection('users').document()
        user_ref.set({
            'username': data['username'],
            'createdAt': firestore.SERVER_TIMESTAMP,
            'credits': DEFAULT_CREDITS_PER_NEW_USER
        })
        
        return {"status": "success", "uid": user_ref.id}
    
    except Exception as e:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INTERNAL,
            message=str(e)
        )