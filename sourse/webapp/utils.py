def task_validate(task, updated_at):
    errors = {}
    if not task:
        errors['task'] = "заполните поле Задачи"
    elif len(task) > 200:
        errors['task'] = "слишком много сивомволов для поле Задачи(>200)"

    if not updated_at:
        errors['updated_at'] = "заполните поле Даты"
    return errors