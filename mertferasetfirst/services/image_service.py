from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from firebase_admin import initialize_app, firestore, auth
from constants import STYLE_COSTS
from services.credits_service import check_sufficient_credits
db = firestore.client()



@https_fn.on_call()
def create_fake_image_url(req: https_fn.CallableRequest) -> dict:
 
    data = req.data

    credits_to_deduct = STYLE_COSTS.get(data["style"])

    user_ref = db.collection('users').document(data['uid'])
    user_doc = user_ref.get()
    if not user_doc.exists:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.NOT_FOUND,
            message="User not found"
        )
    user_data = user_doc.to_dict()
    current_credits = user_data.get('credits', 0)

    if not data.get('style') or data['style'] not in STYLE_COSTS:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message="Invalid image prompt"
        )
  
    if not data.get('uid') or not data.get('imagePrompt'):
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message="User ID and image prompt are required"
        )
    
    check_sufficient_credits(current_credits, credits_to_deduct, data.get('style'))

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
    
    
    


    





