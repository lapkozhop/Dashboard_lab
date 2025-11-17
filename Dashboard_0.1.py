from dash import Dash, html

# Создание экземпляра приложения
app = Dash()

# Определение структуры дашборда
app.layout = [html.Div(children="Hello World")]

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
