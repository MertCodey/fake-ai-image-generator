from firebase_functions import https_fn

def check_sufficient_credits(current: int, required: int, style: str | None = None):
    if current < required:
        style_msg = f" for {style} style" if style else ""
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.FAILED_PRECONDITION,
            message=f"Insufficient credits. You have {current} but need {required}{style_msg}."
        )

