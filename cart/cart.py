
from decimal import Decimal
from product.models import Product

class Cart():

    def __init__(self, request):
        self.session = request.session
        #skey is the session key 
        cart = self.session.get('skey') 
        if 'skey' not in request.session:
            #cart = self.session['skey'] = {'number':12345}
            cart = self.session['skey'] = {}
        self.cart = cart 

    def add(self, product, qty):
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id]= {'price': str(product.price), 'qty': int(qty)}
        
        #self.session.modified = True 
        self.save()

    def __iter__(self):
        prodact_ids = self.cart.keys()
        products=Product.objects.filter(id__in=prodact_ids)
        cart= self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product 
        
        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def update(self, product, qty):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        self.save()


    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['qty'] for item in self.cart.values())
        
    def delete(self, product):
        product_id=str(product)

        if product_id in self.cart:
            del self.cart[product_id]
            print(product_id)
            self.save()

    def save(self):
        self.session.modified = True            
