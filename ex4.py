# define the number of car 
cars = 100
#  define how many people  a car could take
space_in_a_car = 4.0
# define the number of driver 
drivers = 30
# define the number of passenger 
passengers = 90
# define how many cars would not be used
cars_not_driven = cars - drivers
# define how many cars could be used 
cars_driven = drivers 
# define how many people could be capacitied
carpool_capacity = cars_driven * space_in_a_car
# define how many people one car need take 
average_passengers_per_car = passengers / cars_driven

print "There are", cars , "cars avaliable. "

print "There are only", drivers, "drivers avaliable."

print "There will be", cars_not_driven, "empty cars today."

print "We can transport", carpool_capacity, "people today."

print "We have", passengers, "to carpool today."

print "We need to put about", average_passengers_per_car, "in each car."
