def validate_positive(value: float, field_name: str):
    if value < 0:
        raise ValueError(f"{field_name} must be non-negative")


def validate_days(days: int):
    if days <= 0:
        raise ValueError("Number of days must be greater than zero")
