from .models import *
from django.db.models import Sum

def user_data(request):
    """
    Function to retrieve user data based on the request session's user ID.
    Parameters:
        request: the request object containing the session information
    Returns:
        A dictionary containing the user data with the key 'user_data'
    """
    user_id = request.session.get('u_id')
    seller = False

    user_data = None
    fetchCartData = 0
    fetchCart = None

    if user_id:
        try:
            user_data = usertable.objects.get(id=user_id)
            fetchCartData = carttable.objects.filter(userid=user_data).count()
            fetchCart = carttable.objects.filter(userid=usertable.objects.get(id=request.session['u_id']))
            
            if user_data.u_type == "seller":
                seller = True

        except usertable.DoesNotExist:
            pass

    return {'user_data': user_data,
            'seller': seller, 'cartCount': fetchCartData, 'cartData': fetchCart, 'fetchCart': fetchCart}
