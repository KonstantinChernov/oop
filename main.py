from linked_list import LinkedList
from builder import DriverFactory

# driver_json = DriverFactory.get_driver('json')

# a = LinkedList()
# a.append(23)
# a.append(25)
# a.append(26)
#
# a.add_driver(driver_json)
#
# a.write()


b = LinkedList.read()
print(b)
print('====================================')

driver_csv = DriverFactory.get_driver('csv')
a = LinkedList()
a.append(1)
a.append(3)
a.append(5)
a.add_driver(driver_csv)

a.write()