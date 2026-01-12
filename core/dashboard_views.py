
from bokeh.resources import CDN
import pandas as pd
import plotly.express as px
import plotly.io as pio
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap

from django.shortcuts import render
from .repositories import analytics_repo


def dashboard_plotly(request):

    min_flights_filter = int(request.GET.get('min_flights', 0))
   
    min_year_filter = int(request.GET.get('min_year', 1950))

    charts = []

    # 1
    q1 = analytics_repo.get_flights_by_airport()
    df1 = pd.DataFrame(list(q1))
    if not df1.empty:
       
        df1 = df1[df1['total_flights'] >= min_flights_filter]
        
        fig1 = px.bar(df1, x='airport__name', y='total_flights', 
                      title='1. Кількість рейсів по аеропортах',
                      color='total_flights', labels={'airport__name': 'Аеропорт'})
        charts.append(pio.to_html(fig1, full_html=False))

    # 2
    q2 = analytics_repo.get_revenue_by_aircraft_type()
    df2 = pd.DataFrame(list(q2))
    if not df2.empty:
        fig2 = px.pie(df2, values='total_revenue', names='flight__aircraft__model', 
                      title='2. Частка доходу за моделями літаків')
        charts.append(pio.to_html(fig2, full_html=False))

    # 3
    q3 = analytics_repo.get_frequent_flyers()
    df3 = pd.DataFrame(list(q3))
    if not df3.empty:
        df3['full_name'] = df3['first_name'] + " " + df3['last_name']
        fig3 = px.bar(df3, x='full_name', y='booking_count', 
                      title='3. Топ пасажирів за кількістю польотів')
        charts.append(pio.to_html(fig3, full_html=False))

    #4
    q4 = analytics_repo.get_avg_ticket_price_by_nationality()
    df4 = pd.DataFrame(list(q4))
    if not df4.empty:
        fig4 = px.bar(df4, x='avg_spend', y='nationality', orientation='h',
                      title='4. Середня вартість квитка по країнах',
                      color='avg_spend')
        charts.append(pio.to_html(fig4, full_html=False))

    # 5
    q5 = analytics_repo.get_low_occupancy_flights()
    df5 = pd.DataFrame(list(q5))
    if not df5.empty:
        fig5 = px.scatter(df5, x='flight_number', y='sold_tickets', 
                          color='airport__name', size='sold_tickets',
                          title='5. Рейси з низькою завантаженістю')
        charts.append(pio.to_html(fig5, full_html=False))

    # 6
    q6 = analytics_repo.get_passenger_age_distribution()
    df6 = pd.DataFrame(list(q6))
    if not df6.empty:
        df6 = df6[df6['birth_date__year'] >= min_year_filter] 
        fig6 = px.line(df6, x='birth_date__year', y='count', markers=True,
                       title='6. Розподіл пасажирів за роком народження')
        charts.append(pio.to_html(fig6, full_html=False))

    return render(request, 'core/dashboard_plotly.html', {
        'charts': charts,
        'min_flights_filter': min_flights_filter,
        'min_year_filter': min_year_filter
    })


def dashboard_bokeh(request):
    script, divs = None, []
    
    # 1
    q1 = analytics_repo.get_flights_by_airport()
    df1 = pd.DataFrame(list(q1))
    if not df1.empty:
        source = ColumnDataSource(df1)
       
        airports = df1['airport__name'].tolist()
        p = figure(x_range=airports, height=300, title="1. Рейси по аеропортах", tools="")
        p.vbar(x='airport__name', top='total_flights', width=0.9, source=source, color="#718dbf")
        divs.append(p)
    else:
        divs.append("Немає даних")

   # 2 
    q2 = analytics_repo.get_revenue_by_aircraft_type()
    df2 = pd.DataFrame(list(q2))
    if not df2.empty:
       
        df2['total_revenue'] = df2['total_revenue'].astype(float)
        
       
        if 'avg_price' in df2.columns:
            df2['avg_price'] = df2['avg_price'].astype(float)
        
        source = ColumnDataSource(df2)
        models = df2['flight__aircraft__model'].tolist()
        p = figure(x_range=models, height=300, title="2. Дохід за моделями літаків")
        p.vbar(x='flight__aircraft__model', top='total_revenue', width=0.5, source=source, color="green")
        divs.append(p)
    else:
        divs.append("Немає даних")

    #3
    q3 = analytics_repo.get_frequent_flyers()
    df3 = pd.DataFrame(list(q3))
    if not df3.empty:
        df3['full_name'] = df3['first_name'] + " " + df3['last_name']
        source = ColumnDataSource(df3)
        names = df3['full_name'].tolist()
        p = figure(x_range=names, height=300, title="3. Топ пасажирів")
        p.vbar(x='full_name', top='booking_count', width=0.5, source=source, color="orange")
        divs.append(p)
    else:
        divs.append("Немає даних")

    # 4
    q4 = analytics_repo.get_avg_ticket_price_by_nationality()
    df4 = pd.DataFrame(list(q4))
    if not df4.empty:
        df4['avg_spend'] = df4['avg_spend'].astype(float)
        source = ColumnDataSource(df4)
        nations = df4['nationality'].tolist()
       
        p = figure(y_range=nations, height=400, title="4. Середня ціна по країнах")
        p.hbar(y='nationality', right='avg_spend', height=0.5, source=source, color="purple")
        divs.append(p)
    else:
        divs.append("Немає даних")

    # 5
    q5 = analytics_repo.get_low_occupancy_flights()
    df5 = pd.DataFrame(list(q5))
    if not df5.empty:
        source = ColumnDataSource(df5)
        p = figure(height=300, title="5. Рейси з малою кількістю квитків")
        p.circle(x='sold_tickets', y='sold_tickets', source=source, size=15, color="red", alpha=0.6)
        
        p.add_tools(HoverTool(tooltips=[("Рейс", "@flight_number"), ("Продано", "@sold_tickets")]))
        divs.append(p)
    else:
        divs.append("Немає даних")

    # 6
    q6 = analytics_repo.get_passenger_age_distribution()
    df6 = pd.DataFrame(list(q6))
    if not df6.empty:
        source = ColumnDataSource(df6)
        p = figure(height=300, title="6. Динаміка народжуваності")
        p.line(x='birth_date__year', y='count', source=source, line_width=2)
        p.circle(x='birth_date__year', y='count', source=source, size=8, fill_color="white", line_width=2)
        divs.append(p)
    else:
        divs.append("Немає даних")

   
    if divs:
        script, div_list = components(divs)
    else:
        script, div_list = "", []

   
    while len(div_list) < 6:
        div_list.append("Немає даних")

    
    resources = CDN.render()

    return render(request, 'core/dashboard_bokeh.html', {
        'resources': resources,
        'script': script,
        'div1': div_list[0],
        'div2': div_list[1],
        'div3': div_list[2],
        'div4': div_list[3],
        'div5': div_list[4],
        'div6': div_list[5],
    })