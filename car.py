from serviceable import Serviceable, needs_service


class Car(Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @needs_service
    def needs_service(self):
        pass
