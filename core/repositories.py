from django.db.models import Sum, Avg, Count, Max, Min
from django.db.models.functions import TruncMonth
from core.models import Customer, Courier, DeliveryOrder

class BaseRepository:
    def __init__(self, model):
        self.model = model
    def get_all(self):
        return self.model.objects.all()
    def get_by_id(self, entity_id):
        try: return self.model.objects.get(id=entity_id)
        except self.model.DoesNotExist: return None

class DeliveryOrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(DeliveryOrder)

    # Дохід по кур'єрам
    def get_revenue_by_courier(self):
        return self.model.objects.values('courier__name').annotate(total=Sum('price')).order_by('-total')

    # Кількість замовлень по місяцях
    def get_orders_by_month(self):
        return self.model.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).order_by('month')

    # Топ-5 клієнтів
    def get_top_customers(self):
        return self.model.objects.values('customer__full_name').annotate(total=Sum('price')).order_by('-total')[:5]

    # Середній чек по кур'єрах
    def get_avg_per_courier(self):
        return self.model.objects.values('courier__name').annotate(avg=Avg('price'))

    # Макс/Мін ціни замовлень клієнтів
    def get_client_stats(self):
        return self.model.objects.values('customer__full_name').annotate(min_p=Min('price'), max_p=Max('price'))

    # Замовлення вище середнього (складний фільтр)
    def get_expensive_orders(self):
        avg_val = self.model.objects.aggregate(Avg('price'))['price__avg'] or 0
        return self.model.objects.filter(price__gt=avg_val).values('id', 'price', 'customer__full_name')

class RepositoryManager:
    def __init__(self):
        self.orders = DeliveryOrderRepository()

repo = RepositoryManager()