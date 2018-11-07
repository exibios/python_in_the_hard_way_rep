cars = 100
space_in_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven
print "There are ",cars," cars available."
print "There are only", drivers, " drivers available."
print "There will be ", cars_not_driven, " un available cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, " to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


## question
## the error might be because the variable car_pool_capacity was not declared before it was used
## Study Drill
##
## 1  NO
## 2  I already know
## 3 for what, now is useless
## 4 done
## 5 done
## 6 useless
