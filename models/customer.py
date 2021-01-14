class Customer():

    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
