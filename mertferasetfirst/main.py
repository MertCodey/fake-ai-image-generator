
from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from firebase_admin import initialize_app, firestore, auth

set_global_options(max_instances=10)

initialize_app()
db = firestore.client()

@https_fn.on_call()
def register_this_user(req: https_fn.CallableRequest) -> dict:
    data=req.data

    if not data.get('username') or not data.get('password'):
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message="Username and password are required"
        )
    
    try:
        import uuid
        fake_uid = str(uuid.uuid4())
        
        user_ref = db.collection('users').document(fake_uid)
        user_ref.set({
            'username': data['username'],
            'createdAt': firestore.SERVER_TIMESTAMP,
            'credits': 50
        })
        
        return {"status": "success", "uid": fake_uid}
    
    except Exception as e:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INTERNAL,
            message=str(e)
        )
    
@https_fn.on_call()
def create_fake_image_url(req: https_fn.CallableRequest) -> dict:
 
    data = req.data

    if data.get('style') == "realistic":
        credits_to_deduct = 1
    elif data.get('style') == "cartoon":
        credits_to_deduct = 1
    elif data.get('style') == "abstract":
        credits_to_deduct = 1
    elif data.get('style') == "anime":
        credits_to_deduct = 2
    elif data.get('style') == "oil-painting":
        credits_to_deduct = 3
    elif data.get('style') == "watercolor":
        credits_to_deduct = 2
    elif data.get('style') == "sketch":
        credits_to_deduct = 1
    elif data.get('style') == "digital-art":
        credits_to_deduct = 2
    else:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message="Invalid image prompt"
        )
    data = req.data
    if not data.get('uid') or not data.get('imagePrompt'):
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message="User ID and image prompt are required"
        )
    
    user_ref = db.collection('users').document(data['uid'])
    user_doc = user_ref.get()
    if not user_doc.exists:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.NOT_FOUND,
            message="User not found"
        )
    user_data = user_doc.to_dict()
    current_credits = user_data.get('credits', 0)
    
    if current_credits < credits_to_deduct:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.FAILED_PRECONDITION,
            message=f"Insufficient credits. You have {current_credits} credits but need {credits_to_deduct} for {data.get('style')} style."
        )
    try:
        fake_image_url = f"https://fakeimage.com/{data['imagePrompt'].replace(' ', '_')}.png"
        user_ref.update({
            'credits': firestore.Increment(-credits_to_deduct)
        })
        return {"status": "success", "imageUrl": fake_image_url, "remainingCredits": user_data['credits'] - credits_to_deduct}

    except Exception as e:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INTERNAL,
            message=str(e)
        )
    
    
    


    





