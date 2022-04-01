
class Phone:

    def __init__(self, color, model):
        self.color = color
        self.model = model

    # Обычный метод
    # Первый параметр метода - self
    def check_sim(self, mobile_operator):
        if self.model == 'I785' and mobile_operator == 'MTS':
            print('Your mobile operator is MTS')

my_phone = Phone('red', 'I785')
my_phone.check_sim('MTS')
