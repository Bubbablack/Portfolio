class Person:
    def __init__(self, name, age, gender, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def str_interest(self):
        str = ""
        for interest in self.interests:
            if interest == self.interests[0]:
                str += interest
            elif interest == self.interests[-1]:

                str += " and " + interest
            else:

                str += ", " + interest
        return str

    def hello(self):

        print(
            f"Hello, my name is  {self.name } and I am {(self.age)} years old. My intrerests are {self.str_interest()}."
        )


if __name__ == "__main__":
    person = Person("John", 36, "male", ["rain", "love", "toys"])
    person.hello()
