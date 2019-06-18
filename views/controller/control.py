from .service.teacher_service import teacher_service


def login(identity: str, id, password):
    if identity == 'teacher':
        if teacher_service.check_login(id, password) is True:
            teacher_service.login(id)
    pass