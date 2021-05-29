#!/usr/bin/python3
# In python you can use modules or classes
# Both are OK
# I am not an expert of python :(

# Modules are more structure-like programming approach
# Classes are more object oriented programming
# Classes should not contain variables - for this you should use instances
# Modules are to be used with single instance... but you could also create local "copies"
# Classes allow one class to inherit from another

# Examples:
#  math is a good item for a module - you have all the things not to be "call specific"
#  logging is a thing to be class-like - you should never re-use same instance in different places

from loguru import logger

class Example:
    '''Class can have its own documentation
    just like this - all indentation will be preserved'''

    class_variable = 'Example'  # generally it should be not mutable
    # class variables are shared among all its instances

    def __init__(self, name):
        # This is a constructor - will be called when class instance is created

        self.instance_variable = name
        # instance variables belong to the instance (other instances will have its own)

        local_variable = 'this variable will disappear after the method (constructor in this case)'

        # We can use variables in a string in 3+ ways
        # Whenever using loggers you should always pass the variables as extra values to let logger parse
        #  because those are not always shows (depends on the logger configuration)
        #  and tools can access it in other way than simple strings
        logger.debug("Created a new instance of Example class with name='{}'", name)
        # logger.debug("Created a new instance of Example class with name='%s'" % (name))
        # logger.debug("Created a new instance of Example class with name='{}'".format(name))
        # logger.debug(f"Created a new instance of Example class with name='{name}'")

    def __str__(self):
        '''This method is called when you convert this to string
        For example `print(example)`'''
        return f"<class Example>({self.class_variable}, {self.instance_variable})"

class Example2:
    def dummy():
        return

def main():
    logger.debug("Loguru works out of the box!")

    instance1 = Example("first")
    instance2 = Example("second")

    print(instance1)  # calls .__str__
    print(instance2)

    another_one = Example2()
    print(another_one)  # prints '<__main__.Example2 object at ...>'

    # The "description" of a class can be accessed
    print(Example.__doc__)
    # print(instance1.__doc__)  # this does the same


if __name__ == '__main__':
    main()
