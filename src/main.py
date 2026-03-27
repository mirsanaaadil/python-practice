import api.task
import utils.validator

get_data=api.task.get_tasks()
check_data=utils.validator.validate_tasks(get_data)

if check_data:
    print("valid data")
else :
    print("invalid data")

