
# TASK

"""
fname, lname, gender, birth_year, this_year, job = "John", "Malkovic", "male", 1980, 2021, "artist"
age = this_year-birth_year
# "My name is John Malkovic.I am male and I am an artist. I am 41 years old." ifadesini print("".format()) ve print(f{}) yöntemleri ile iki kere yazdırın.

"""

"""
fname, lname, gender, birth_year, this_year, job = "John", "Malkovic", "male", 1980, 2021, "artist"
age = this_year-birth_year
# "My name is John Malkovic.I am male and I am an artist. I am 41 years old." ifadesini print("".format()) ve print(f{}) yöntemleri ile yazdırın.


print(
    f"My name is {fname} {lname}. I am {gender} and I am an {job}. I am {age} years old.")

print(
    "My name is {} {}. I am {} and I am an {}. I am {} years old.".format(fname, lname, gender, job, age))

"""



text = "Günler gitgide kısalıyor, yağmurlar başlamak üzre. Kapım ardına kadar açık bekledi seni! Niye böyle geç kaldın?"
# metindeki 'üzre' kelimesini 'üzere' yapın
# metnin tamamını küçük harfli yapın
# boşlukların yerine tire(-) koyun
# bütün noktalama işaretlerini kaldırın
# bütün türkçe karakterleri ingilizce karşılıkları ile değiştirin

result=text.replace("üzre","üzere")
result=text.lower()
result=text.lower()
result=text.replace(" ","-")
result=text.replace(",","").replace(".","").replace("!","").replace("?","")
result=text.replace("ü","u").replace("ş","s").replace("İ","I").replace("ı","i").replace("ç","c").replace("ğ","g") .replace("o","ö")
print (result)




