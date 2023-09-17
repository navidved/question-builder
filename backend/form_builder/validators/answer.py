def answer_validator(answer_type, answer):
    answer_type_test = answer.get(answer_type)
    if answer_type_test is not None and len(answer) == 1:
        return True
    return False
