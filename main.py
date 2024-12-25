from dataclasses import dataclass,field
# 1 misol
@dataclass
class Product:
    name:str
    __narxi:int
    maxsulot: str
    info:str = field(init=False)

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError("Narx ijobiy bo'lishi kerak!")
    def __post_init__(self):
        self.info:str = f"Person: {self.name}, {self.__narxi},{self.maxsulot}"

@dataclass
class ElectronicProduct(Product):
    kafolat:str

    def __post_init_(self):
        super().__post_init__()
        print("Product ichida bajarildi!!!!!!!!!!!!")
pd1 = Product('Soat',22000,'bor')
pd1.price= -12
print(pd1.price)

# 2 misol
@dataclass
class Vehicle:
    marka:str
    __speed:int
    info:str = field(init=False)

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        if value <= 300:
            self.__speed = value
        else:
            raise ValueError("Tezlik 300 km/soatdan oshmasligi kerak!")

    def __post_init__(self):
            self.info:str = f"Person: {self.marka}, {self.__speed}"

@dataclass
class Car(Vehicle):
    yoqilgi:str
    tormoz:str

    def __post_init__(self):
        super().__post_init__()
        print("Vehicle ichida bajarilyabdi!!")


@dataclass
class Bycycle(Vehicle):
    yoqilgi: str=field(init=False)
    tormoz: str

    def __post_init__(self):
        super().__post_init__()
        print("Vehicle ichida bajarilyabdi!!")

ps= Car("Bmw",299,"Ai-95","abc")
print(ps.info)
ps2=Bycycle("BMX",90,"dick")
print(ps2.info)

# 3 misol

@dataclass
class Book:
    title: str
    author: str
    __price: int
    info: str = field(init=False)

    @property
    def price(self):
        return self.__price

    def set_price(self, new_price, is_admin=False):
        if is_admin:
            if new_price > 0:
                self.__price = new_price
            else:
                raise ValueError("Narx musbat bo'lishi kerak!")
        else:
            raise PermissionError("Narxni faqat admin o'zgartira oladi!")

    def __post_init__(self):
        self.info = f"Kitob: {self.title}, Muallif: {self.author}, Narxi: {self.__price} USD"

@dataclass
class EBook(Book):
    file_size: int
    format: str

    def __post_init__(self):
        super().__post_init__()
        print("EBook obyekti yaratildi!")

@dataclass
class PrintedBook(Book):
    paper_type: str
    cover_type: str

    def __post_init__(self):
        super().__post_init__()
        print("PrintedBook obyekti yaratildi!")
b1=EBook("Izlash","Mehmet Jilasun",22000,23,"pdf")
print(b1.info)
b2=PrintedBook("Hamsa","Alisher Navoi",23444443,"Teri","Qogoz")
print(b2.info)

#  4 misol
@dataclass
class Employee:
    name: str
    position: str
    __salary: float
    info: str = field(init=False)

    @property
    def salary(self):
        return self.__salary

    def raise_salary(self, amount, is_director=False):
        if is_director:
            if amount > 0:
                self.__salary += amount
            else:
                raise ValueError("Maosh oshirish summasi musbat bo'lishi kerak!")
        else:
            raise PermissionError("Maoshni faqat direktor oshira oladi!")

    def __post_init__(self):
        self.info = f"Xodim: {self.name}, Lavozim: {self.position}, Maosh: {self.__salary} "

@dataclass
class Manager(Employee):
    team_size: int
    def manage_team(self):
        return f"{self.name} {self.team_size} kishilik jamoani boshqaradi."

    def __post_init__(self):
        super().__post_init__()
        print("Manager obyekti yaratildi!")

@dataclass
class Developer(Employee):
    programming_language: str
    def write_code(self):
        return f"{self.name} {self.programming_language} tilida dasturlar yozadi."
    def __post_init__(self):
        super().__post_init__()
        print("Developer obyekti yaratildi!")

ep1= Manager("Sobir","main",3000000,4)
ep2 =Developer("toxir","midle",2000000,"python")
print(ep1.info)
print(ep2.info)


# 5 misol
@dataclass
class Athlete:
    name: str
    sport_type: str
    __records: list
    info: str = field(init=False)

    @property
    def records(self):
        return self.__records

    def update_records(self, new_records):
        if all(isinstance(record, (int, float)) and record > 0 for record in new_records):
            self.__records = new_records
        else:
            raise ValueError("Rekordlar musbat sonlardan iborat bo'lishi kerak!")

    def __post_init__(self):
        self.info = f"Sportchi: {self.name}, Sport turi: {self.sport_type}, Rekordlari: {self.__records}"

@dataclass
class Runner(Athlete):
    distance: float

    def run_distance(self):
        return f"{self.name} {self.distance} metr masofaga yuguradi."

    def __post_init__(self):
        super().__post_init__()
        print("Runner obyekti yaratildi!")

@dataclass
class Swimmer(Athlete):
    pool_type: str

    def swim_in_pool(self):
        return f"{self.name} {self.pool_type} havzasida suzadi."

    def __post_init__(self):
        super().__post_init__()
        print("Swimmer obyekti yaratildi!")

sp1=Runner('Jalil',"running",["100 metrilik yugurish"],100)
sp2=Swimmer('Sobir','swimming',["suzishda 25 sekunda 50 metrga borish"],"dengiz")
print(sp1.info)
print(sp2.info)
