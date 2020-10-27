from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
weekday_names = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
                 4: "Friday", 5: "Saturday", 6: "Sunday"}


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def print_menu():
    print("1) Today's tasks")
    print("2) Week's tasks")
    print('3) All tasks')
    print('4) Missed tasks')
    print('5) Add task')
    print('6) Delete task')
    print('0) Exit')


def print_tasks_for_day(date_to_print, print_type):
    day_tasks = session.query(Table).filter(Table.deadline == date_to_print.date()).all()
    current_day = date_to_print.day
    month_name = date_to_print.strftime('%b')

    if print_type == 'today':
        print(f"Today {current_day} {month_name}:")
    elif print_type == 'weekly':
        weekday_name = weekday_names[date_to_print.weekday()]
        print(f"{weekday_name} {current_day} {month_name}:")

    if len(day_tasks) == 0:
        print('Nothing to do!')
    else:
        for i in range(len(day_tasks)):
            print(f'{i + 1}. {day_tasks[i].task}')

    print('')


def print_tasks_compactly(tasks_to_print):
    for i in range(len(tasks_to_print)):
        this_row = tasks_to_print[i]
        this_day = this_row.deadline.day
        this_month = this_row.deadline.strftime('%b')
        print(f'{i + 1}. {this_row.task}. {this_day} {this_month}')


def print_today_tasks():
    today = datetime.today()
    print_tasks_for_day(today, 'today')


def print_week_tasks():
    today = datetime.today()
    for delta in range(7):
        print_tasks_for_day(today + timedelta(days=delta), 'weekly')


def print_all_tasks():
    tasks_to_print = session.query(Table).order_by(Table.deadline).all()
    print('All tasks:')
    if len(tasks_to_print) == 0:
        print('Nothing to do!')
    else:
        print_tasks_compactly(tasks_to_print)
    print('')


def print_missed_tasks():
    tasks_to_print = session.query(Table) \
        .filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
    print('Missed tasks:')
    if len(tasks_to_print) == 0:
        print('Nothing is missed!')
    else:
        print_tasks_compactly(tasks_to_print)
    print('')


def add_task():
    print('Enter task')
    new_task = input()

    print('Enter deadline')
    deadline = input()
    date_field = datetime.strptime(deadline, '%Y-%m-%d').date()

    created_task = Table(task=new_task, deadline=date_field)
    session.add(created_task)
    session.commit()
    print('The task has been added!')


def delete_task():
    tasks_to_print = session.query(Table).order_by(Table.deadline).all()
    print('Choose the number of the task you want to delete:')
    if len(tasks_to_print) == 0:
        print('Nothing to delete')
    else:
        print_tasks_compactly(tasks_to_print)
        chosen_number = int(input())
        task_to_delete = tasks_to_print[chosen_number - 1]
        session.delete(task_to_delete)
        session.commit()


print_menu()
menu_item = int(input())
while menu_item != 0:
    if menu_item == 1:
        print_today_tasks()
    elif menu_item == 2:
        print_week_tasks()
    elif menu_item == 3:
        print_all_tasks()
    elif menu_item == 4:
        print_missed_tasks()
    elif menu_item == 5:
        add_task()
    elif menu_item == 6:
        delete_task()
    else:
        break

    print_menu()
    menu_item = int(input())

print('Bye!')
