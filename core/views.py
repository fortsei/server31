import pandas as pd
import plotly.express as px
import plotly.offline as opy
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .repositories import repo
from .NetworkHelper import HotelAPI


from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot


def order_list(request): 
    return render(request, 'core/order_list.html', {'orders': repo.orders.get_all()})

def order_create(request): 
    return render(request, 'core/order_form.html')

def order_detail(request, pk): 
    return render(request, 'core/order_detail.html')

def order_update(request, pk): 
    return render(request, 'core/order_form.html')

def order_delete(request, pk): 
    return render(request, 'core/order_confirm_delete.html')

def external_guests(request): 
    return render(request, 'core/external_guests.html')

def delete_external_guest(request, guest_id):
    if request.method == "POST": 
        HotelAPI.delete_guest(guest_id)
    return redirect("external_guests")


class AnalyticsAPIView(APIView):
    def get(self, request):
        data = list(repo.orders.get_revenue_by_courier())
        df = pd.DataFrame(data)
        stats = {}
        if not df.empty:
            stats = {
                "mean": float(df['total'].mean()),
                "median": float(df['total'].median()),
                "min": float(df['total'].min()),
                "max": float(df['total'].max()),
            }
        return Response({"data": data, "pandas_stats": stats})


def dashboard_v1(request):
    min_p = float(request.GET.get('min_price', 0))
    orders_qs = repo.orders.get_all().filter(price__gte=min_p)
    df = pd.DataFrame(list(orders_qs.values('courier__name', 'customer__full_name', 'price')))

    if df.empty:
        return render(request, 'core/dashboard.html', {'min_price': min_p, 'no_data': True})

    context = {
        'g1': opy.plot(px.bar(df.groupby('courier__name')['price'].sum().reset_index(), x='courier__name', y='price', title="Дохід кур'єрів"), auto_open=False, output_type='div'),
        'g2': opy.plot(px.pie(df.groupby('customer__full_name')['price'].sum().reset_index(), values='price', names='customer__full_name', title="Топ клієнтів"), auto_open=False, output_type='div'),
        'g3': opy.plot(px.line(df, y='price', title="Ціни замовлень"), auto_open=False, output_type='div'),
        'g4': opy.plot(px.scatter(df, x='courier__name', y='price', title="Розподіл замовлень"), auto_open=False, output_type='div'),
        'g5': opy.plot(px.bar(df.groupby('customer__full_name')['price'].mean().reset_index(), x='customer__full_name', y='price', title="Середній чек"), auto_open=False, output_type='div'),
        'g6': opy.plot(px.histogram(df, x='price', title="Гістограма цін"), auto_open=False, output_type='div'),
        'min_price': min_p
    }
    return render(request, 'core/dashboard.html', context)


def dashboard_v2(request):
    data = list(repo.orders.get_revenue_by_courier())
    df = pd.DataFrame(data)
    
    if df.empty:
        return render(request, 'core/dashboard_v2.html', {'div': "База даних порожня"})

    
    names = [str(x) for x in df['courier__name'].tolist()]
    totals = [float(x) for x in df['total'].tolist()]
    x_axis = list(range(len(totals))) 

    
    p1 = figure(x_range=names, title="Дохід (Bar)", height=250, width=350)
    p1.vbar(x=names, top=totals, width=0.7, color="navy")
    
    p2 = figure(title="Динаміка (Line)", height=250, width=350)
    p2.line(x_axis, totals, line_width=2, color="red")

    p3 = figure(title="Точки (Scatter)", height=250, width=350)
    p3.circle(x_axis, totals, size=10, color="green")

    p4 = figure(y_range=names, title="Рейтинг (HBar)", height=250, width=350)
    p4.hbar(y=names, right=totals, height=0.5, color="orange")

    p5 = figure(title="Маркери (Square)", height=250, width=350)
    p5.square(x_axis, totals, size=10, color="olive")

    p6 = figure(title="Сходинки (Step)", height=250, width=350)
    p6.step(x_axis, totals, line_width=2, color="purple")

    # сітка
    layout = gridplot([[p1, p2], [p3, p4], [p5, p6]])
    script, div = components(layout)
    
    return render(request, 'core/dashboard_v2.html', {'script': script, 'div': div})