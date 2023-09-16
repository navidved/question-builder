def answer_validator(answer_type, answer):
    if answer_type in answer and len(answer) == 1:
        return True
    return False