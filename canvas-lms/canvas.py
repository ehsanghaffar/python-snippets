from datetime import datetime

def get_period(canvas_dt):
    # useges: get_period(sub.assignment["due_at"])
    dt = datetime.strptime(canvas_dt, "%Y-%m-%dT%H:%M:%SZ")
    month = dt.month

    if 1 < month <= 7:
        return "SEMESTER_2"
    elif 7 < month <= 9:
        return "RESIT"

    return "SEMESTER_1"