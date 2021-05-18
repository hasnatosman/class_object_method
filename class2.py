class Car:
    name = ' Filter'
    color = ' White'

    def start():
        print('Starting the Car!....................')


print('Name of the car :', Car.name)
print('Color of the car: ', Car.color)

Car.name = 'Axio'
print('New name is: ', Car.name)

Car.start()
