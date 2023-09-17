def answer_validator(answer_type, answer:dict):
    visitor_answer = answer.get(answer_type)
    return {answer_type:visitor_answer} if visitor_answer else None
