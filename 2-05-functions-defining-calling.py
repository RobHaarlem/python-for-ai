def greet(name,language):
  print(15*"__")
  print( f"Hello {name}")
  print(15*"__")
  print(f"Welcome to {language}")
  print(15*"__")
  return(f"Hello {name}, je gaat {language} leren.")

message = greet("Rob","Python")
print(message)

def check_weather(temperature):
  if temperature>25:
    print("It's hot today")
  elif 15<temperature<25:
    print("It's nice weather")
  else:
    print("Trek een jas aan")

check_weather(26)

def print_name(name="John Do",age="unknown"):
  print(f"Hello {name} you are {age} years")

print_name()
print_name("Martin",74)
print_name(age=7,name="Dae")

def simple_numbers():
  numbers = [1, 2, 3, 4, 5]
  first_number = numbers[0]
  last_numer= numbers[-1]
  return first_number, last_numer

f, l = simple_numbers()
print(f"First number: {f}")
print(f"Last number: {l}")