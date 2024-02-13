from .models import *

def user_data(request):
    user_id = request.session.get('u_id')
   
    user_data = None
    if user_id:
        try:
            user_data = usertable.objects.get(id=user_id)
            seller=False
            if user_data.u_type=="seller":
                seller=True
            
        except usertable.DoesNotExist:
            pass
    return {'user_data': user_data,
            'seller':seller}