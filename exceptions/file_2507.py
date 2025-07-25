# try - пробовать
# except - поймать
# else - тогда
# finally - завершение

# ------------------------------

try:
    a, b = int(input()), int(input())
except ValueError:
    print("Введите целое число")
except KeyboardInterrupt:
    print("Принудительная остановка программы!")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
else:
    print(a + b)
finally:
    print("Завершение программы!")

# ------------------------------

try:
    a, b = int(input()), int(input())
    res: float = a / b
# except ValueError:
#     print("Введите целое число")
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
except (ValueError, ZeroDivisionError) as err:
    print(f"[ERROR]: {err}")
except Exception as err:
    print(f"Отправить разработчикам логи {err}")
else:
    print(res)
finally:
    print("Завершение программы!")
