class phone:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        phone.count+=1

    def get_info(self):
        print(f"the name of phone is {self.name} and price is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"the number of phones are {cls.count}")

    @staticmethod
    def cal_discount(price,discount):
        final_price=price-(price*discount/100)
        return final_price

phone1=phone("iphone",10000)
phone2=phone("samsung",20000)

phone1.get_info()
phone2.get_info()
phone.get_count()
print(phone.cal_discount(10000, 10))