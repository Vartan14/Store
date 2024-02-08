from products.models import Basket


def baskets(request):
    user = request.user
    baskets_set = Basket.objects.filter(user=user) if user.is_authenticated else []
    return {'baskets': baskets_set}
