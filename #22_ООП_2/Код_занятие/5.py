class Phone:

    def __init__(self, color, model):
        self.color = color
        self.model = model

    # Метод класса
    # Принимает 1) ссылку на класс Phone и 2) цвет в качестве параметров
    # Создает специфический объект класса Phone(особенность объекта в том, что это игрушечный телефон)
    # При этом вызывается инициализатор класса Phone
    # которому в качестве аргументов мы передаем цвет и модель,
    # соответствующую созданию игрушечного телефона
    @classmethod
    def toy_phone(cls, color):
        toy_phone = cls(color, 'ToyPhone')
        print(toy_phone)

my_phone = Phone('red', 'I785')
my_phone.check_sim('MTS')
