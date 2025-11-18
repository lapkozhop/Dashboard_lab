import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Загрузка данных
df = pd.read_csv(r"D:\other\MyPyProjects\DashBoard_Lab-rel.0\TextFile1.csv")
df1 = pd.read_csv(r"D:\other\MyPyProjects\DashBoard_Lab-rel.0\TextFile2.csv")

# Создание экземпляра приложения
app = dash.Dash(__name__)

# Определение структуры дашборда
app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Дашборд анализа данных о посещении веб-сайта deliciousfruit.com",
                    style={"textAlign": "center"},
                ),
                html.P(
                    "Этот дашборд предоставляет информацию о количестве пользователей онлайн и"
                    " среднем времени активности на сайте в зависимости от дня и времени дня",
                    style={"textAlign": "center"},
                ),
                # выпадающий список
                html.Div(
                    [
                        html.Label("Выберите дату:", style={"fontSize": 18}),
                        dcc.Dropdown(
                            id="date-dropdown",
                            options=[
                                {"label": date, "value": date} for date in df1["Date"]
                            ],
                            value=df1["Date"].iloc[0],
                            clearable=False,
                            style={"width": "50%", "margin": "0 auto"},
                        ),
                    ],
                    style={"textAlign": "center", "marginBottom": "30px"},
                ),
            ],
            style={"marginBottom": "30px"},
        ),
        html.Div(
            [
                # Линейный график
                dcc.Graph(id="line-chart"),
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [
                # Гистограмма
                dcc.Graph(id="histogram"),
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [
                # Круговая диаграмма
                dcc.Graph(id="pie-chart"),
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [
                # Ящик с усами
                dcc.Graph(id="box-plot"),
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [
                # Точечный график
                dcc.Graph(id="scatter-plot"),
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
    ],
    style={"padding": "20px"},
)


# Определение логики дашборда
@app.callback(
    Output("line-chart", "figure"),
    Output("histogram", "figure"),
    Output("pie-chart", "figure"),
    Output("box-plot", "figure"),
    Output("scatter-plot", "figure"),
    [Input("date-dropdown", "value")],
)
def update_charts(selected_date):
    # Линейный график
    line_chart = go.Figure(go.Scatter(x=df["Date"], y=df["Average_Amount_of_users"]))
    line_chart.update_layout(
        title="Линейный график",
        xaxis_title="День",
        yaxis_title="Среднее за день",
        plot_bgcolor="rgb(230, 230, 230)",
    )

    # Гистограмма
    histogram = go.Figure(go.Histogram(x=df["MiddleSession(sec)"]))
    histogram.update_layout(
        title="Гистограмма",
        xaxis_title="Time",
        yaxis_title="MiddleSession(sec)",
        plot_bgcolor="rgb(230, 230, 230)",
    )

    # Круговая диаграмма
    pie_chart = px.pie(
        df, names="Time", values="Amount_of_users", title="Круговая диаграмма"
    )

    # box_plot
    box_plot = px.box(df, x="Time", y="Amount_of_users", title="Box plot")

    # Точечный график
    scatter_plot = px.scatter(
        df, x="Amount_of_users", y="MiddleSession(sec)", title="Точечный график"
    )

    return line_chart, histogram, pie_chart, box_plot, scatter_plot


# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
