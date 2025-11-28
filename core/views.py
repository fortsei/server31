from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import CustomerSerializer, CourierSerializer, DeliveryOrderSerializer
from .repositories import CustomerRepository, CourierRepository, DeliveryOrderRepository


# -------- Customers --------
class CustomerViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repo = CustomerRepository()

    def list(self, request):
        customers = self.repo.get_all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        customer = self.repo.get_by_id(pk)
        if customer is None:
            return Response({"detail": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = self.repo.create(**serializer.validated_data)
            return Response(CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            updated = self.repo.update(pk, **serializer.validated_data)
            if updated is None:
                return Response({"detail": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(CustomerSerializer(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        customer = self.repo.get_by_id(pk)
        if customer is None:
            return Response({"detail": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            updated = self.repo.update(pk, **serializer.validated_data)
            return Response(CustomerSerializer(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        deleted = self.repo.delete(pk)
        if not deleted:
            return Response({"detail": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------- Couriers --------
class CourierViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repo = CourierRepository()

    def list(self, request):
        couriers = self.repo.get_all()
        serializer = CourierSerializer(couriers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        courier = self.repo.get_by_id(pk)
        if courier is None:
            return Response({"detail": "Courier not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourierSerializer(courier)
        return Response(serializer.data)

    def create(self, request):
        serializer = CourierSerializer(data=request.data)
        if serializer.is_valid():
            courier = self.repo.create(**serializer.validated_data)
            return Response(CourierSerializer(courier).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = CourierSerializer(data=request.data)
        if serializer.is_valid():
            updated = self.repo.update(pk, **serializer.validated_data)
            if updated is None:
                return Response({"detail": "Courier not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(CourierSerializer(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        deleted = self.repo.delete(pk)
        if not deleted:
            return Response({"detail": "Courier not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------- Orders --------
class DeliveryOrderViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repo = DeliveryOrderRepository()

    def list(self, request):
        orders = self.repo.get_all()
        serializer = DeliveryOrderSerializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        order = self.repo.get_by_id(pk)
        if order is None:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DeliveryOrderSerializer(order)
        return Response(serializer.data)

    def create(self, request):
        serializer = DeliveryOrderSerializer(data=request.data)
        if serializer.is_valid():
            order = self.repo.create(**serializer.validated_data)
            return Response(DeliveryOrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = DeliveryOrderSerializer(data=request.data)
        if serializer.is_valid():
            updated = self.repo.update(pk, **serializer.validated_data)
            if updated is None:
                return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(DeliveryOrderSerializer(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        deleted = self.repo.delete(pk)
        if not deleted:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # ---- агрегований звіт ----
    @action(detail=False, methods=['get'])
    def stats(self, request):
        orders = self.repo.get_all()
        total_orders = orders.count()
        total_income = sum(order.price for order in orders)

        income_by_courier = {}
        for order in orders:
            name = order.courier.name
            income_by_courier.setdefault(name, 0)
            income_by_courier[name] += float(order.price)

        return Response({
            "total_orders": total_orders,
            "total_income": float(total_income),
            "income_by_courier": income_by_courier,
        })
