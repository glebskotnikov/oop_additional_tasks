"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
from time import perf_counter, sleep

class Timer:

    def __enter__(self):
        self.perf_counter = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = perf_counter() - self.perf_counter


with Timer() as timer:
    sleep(1)

print("Execution time:", timer.elapsed_time)
