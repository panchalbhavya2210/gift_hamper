from .models import *

def user_data(request):
    """
    Function to retrieve user data based on the request session's user ID.
    Parameters:
        request: the request object containing the session information
    Returns:
        A dictionary containing the user data with the key 'user_data'
    """
    user_id = request.session.get('u_id')
    user_data = None
    if user_id:
        try:
            user_data = usertable.objects.get(id=user_id)
        except usertable.DoesNotExist:
            pass
    return {'user_data': user_data}