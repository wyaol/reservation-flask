from .service.teacher_service import teacher_service


def login(identity: str, id, password):
    if identity == 'teacher':
        teacher_service.login(id, password)
    pass