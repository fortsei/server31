from core.models import Customer, Courier, DeliveryOrder


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, entity_id):
        try:
            return self.model.objects.get(id=entity_id)
        except self.model.DoesNotExist:
            return None

    def create(self, **kwargs):
        obj = self.model.objects.create(**kwargs)
        return obj



class CustomerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Customer)



class CourierRepository(BaseRepository):
    def __init__(self):
        super().__init__(Courier)



class DeliveryOrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(DeliveryOrder)


# Єдина точка доступу (Unit of Work / RepositoryManager)
class RepositoryManager:
    def __init__(self):
        self.customers = CustomerRepository()
        self.couriers = CourierRepository()
        self.orders = DeliveryOrderRepository()
