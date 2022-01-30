import datetime
year=datetime.datetime.now().year

name=input("whats your name:  ")
age=int(input("how old are you:  "))

hunderd =(year-age)+100
def hunderd_years():
    print(f"Hello {name}. You will be 100 years old , in year {hunderd}.")

hunderd_years()