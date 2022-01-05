
from yoshistore.models import Product
from decimal import Decimal
from yoshistore.models import Product
class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id] = { 'price' : str(product.price), 'qty' : int(qty)}

        self.session.modified = True

    def __len__(self):
        print(self.basket)
        print(self.basket.values())
        return sum(item['qty'] for item in self.basket.values())

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item



