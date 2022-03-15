class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        return f"Mening ismim {self.ism}"
    
    def get_age(self, yil):
        return f"{self.ism}ning yoshi: {yil - self.tyil}da"

    def get_lastname(self):
        return f"Mening familiyam {self.familiya}"

    def tanishtir(self):
        return f"Mening ismim: {self.ism}, familiyam: {self.familiya}, tug'ulgan yilim: {self.tyil} "

    

talaba1 = Talaba("Akbar", "Satipov", 2003)
talaba2 = Talaba("Ali", "Boburov", 2000)
talaba3 = Talaba("Mansur", "Rustamov", 2001)

# print(talaba1.get_age(2022))
# print(talaba2.get_lastname())
# print(talaba3.get_name())
# print(talaba1.tanishtir())


def main():
    print(talaba1.get_age(2022))
    print(talaba3.get_name())
    print(talaba1.tanishtir())

if  __name__ == "__main__":
    main()


