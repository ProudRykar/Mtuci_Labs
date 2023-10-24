from fastapi import FastAPI, Request, status

app = FastAPI()

# PATH запрос
@app.get("/from_path/{equation}")
def search_by_path(request: Request, equation: str):
    result = None  # Инициализируем результат как None
    for eq in equation.split():
        if eq != "":
            try:
                eq = eq.replace(':', '/')
                result = eval(eq)
            except ZeroDivisionError:
                return "Ошибка: Деление на ноль", status.HTTP_400_BAD_REQUEST
            except Exception as e:
                return f"Ошибка в математическом выражении: {str(e)}", status.HTTP_400_BAD_REQUEST

    if result is not None:
        return result, status.HTTP_200_OK
    else:
        return "Уравнение не найдено", status.HTTP_500_INTERNAL_SERVER_ERROR