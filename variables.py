# Let us declare few variables
name = "kalyan"
age = 25
is_employed = True
experience = 4.8
print(f"Employee Name is {name} and age {age} with experience of {experience}")
print(type(name))
int(experience)
print(name + " " +str(age))
mother_name = input("Please Enter your MOTHER NAME:")
while True:
  mother_age= input("Enter your Mother Age:")
  if mother_age.isdigit():
    mother_age= int(mother_age)
    break;
  else:
    print("Invalid Entry, Please enter an integer")


is_housewife= bool(input("Enter something if she is housewife"))
print(f"My mother name is {mother_name} and her age is {mother_age} and {is_housewife} "
      )
names = None
print(bool(names))

