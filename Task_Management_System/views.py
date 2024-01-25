from django.shortcuts import render
from tasks.models import TaskModel

def show_tasks(request):
    tasks = TaskModel.objects.all()
    # categories_dict = {}
    # for task in tasks:
    #     # Get category names for the current task
    #     category_names = [
    #         category.categoryName for category in task.taskcategory_set.all()]
    #     categories_dict[task.id] = category_names
    # print(categories_dict)
    return render(request, 'show_tasks.html', {'tasks': tasks})
