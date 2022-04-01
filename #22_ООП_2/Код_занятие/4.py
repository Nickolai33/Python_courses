
class Phone:

    def __init__(self, color, model):
        self.color = color
        self.model = model

    # Обычный метод
    # Первый параметр метода - self
    def check_sim(self, mobile_operator):
        if self.model == 'I785' and mobile_operator == 'MTS':
            print('Your mobile operator is MTS')

    # Статический метод справочного характера
    # Возвращает хэш по номеру модели
    # self внутри метода отсутствует
    @staticmethod
    def model_hash(model):
        if model == 'I785':
            return 34565
        elif model == 'K498':
            return 45567
        else:
            return None

Phone.model_hash('I785')
my_phone = Phone('red', 'I785')
my_phone.check_sim('MTS')
