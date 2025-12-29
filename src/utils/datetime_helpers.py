from datetime import datetime


def calculate_days(start_date: str, end_date: str) -> int:
    """
    Calculate number of days between two dates (YYYY-MM-DD).
    """
    start = datetime.fromisoformat(start_date)
    end = datetime.fromisoformat(end_date)

    days = (end - start).days
    if days <= 0:
        raise ValueError("End date must be after start date")

    return days
