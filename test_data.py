
url_main_page = 'https://qa-scooter.praktikum-services.ru/'

answers = ('Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    )


class Order:

    def __init__(self, name, surname, address, index_station, number, date, days, color, commit):
        self.name = name
        self.surname = surname
        self.address = address
        self.index_station = index_station
        self.number = number
        self.date = date
        self.days = days
        self.color = color
        self.commit = commit

    def get_order_user(self):
        return {"name": self.name, 
                "surname": self.surname, 
                "address": self.address, 
                "index_station":self.index_station, 
                "number":self.number, 
            }
    
    def get_order_about_rent(self):
        return {    
                "date":self.date, 
                "days":self.days, 
                "color":self.color, 
                "commit":self.commit
            }


order_1 = Order('антон','Горлов','Партизана д7','15','79999999999','15.06.2026','3','grey','Позвонить как доставите',)
order_2 = Order('мария','Иванова','Партизана д7 кв 77','19','79999999977','13.06.2026','3','black','оставить около двери',)