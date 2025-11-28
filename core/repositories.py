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
        return self.model.objects.create(**kwargs)
    
    def update(self, entity_id, **kwargs):
        obj = self.get_by_id(entity_id)
        if obj is None:
            return None
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    def delete(self, entity_id):
        obj = self.get_by_id(entity_id)
        if obj is None:
            return False
        obj.delete()
        return True


# --- Конкретні репозиторії ---
class CustomerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Customer)


class CourierRepository(BaseRepository):
    def __init__(self):
        super().__init__(Courier)


class DeliveryOrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(DeliveryOrder)


# --- Менеджер репозиторіїв (Unit of Work) ---
class RepositoryManager:
    def __init__(self):
        self.customers = CustomerRepository()
        self.couriers = CourierRepository()
        self.orders = DeliveryOrderRepository()



repo = RepositoryManager()
