def validate_tasks(tasks) :
    for t in tasks :
        if "id" not in t :
            return False
        elif "title" not in t :
            return False
        elif "status" not in t :
            return False
    return True