class BMI:
	def __init__(self, name, weight, height):
		self.name = name
		self.weight = weight
		self.height = height
		
	def get_name(self):
		return self.name

	def get_weight(self):
		return float(self.weight)

	def get_height(self):
		return self.height

	def calc_bmi(self, weight, height):
		return (D.get_name() + " your bmi is " + str(
			(float(weight))/(float(height**2))))

D = BMI('Debbie', 52, 1.6)
print(D.get_name())
print(D.calc_bmi(52, 1.6))

class Car(object):
	def __init__(self, name):
		self.name = name

user_name = input("What name do you want?")
first_car = Car(user_name)