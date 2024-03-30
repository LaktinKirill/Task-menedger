#Создай класс `Task`, который позволяет управлять задачами (делами).
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
#Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка
#текущих (не выполненных) задач.

class Task():
    def __init__(self):
        self.task_list = []
    def add_task(self, time, overview):
        self.task_list.append({"time": time, "overview": overview, "status": "Не выполнено"})

    def complete_task(self, overview):
        for task in self.task_list:
            if task["overview"] == overview:
                task["status"] = "Выполнено"
                print(f"Задача {overview} выполнена")
            else:
                print(f"Задача {overview} не найдена")

    def all_task(self):
        print("Текущие задачи")
        for task in self.task_list:
            if task['status'] == "Не выполнено":
                print(f"{task["overview"]} - {task["time"]}")

task = Task()
task.add_task("12:20", "Посмотреть уроки")
task.add_task("16:20", "Сделать дз")
task.add_task("17:30", "Пойти домой")

task.all_task()
task.complete_task("Посмотреть уроки")

