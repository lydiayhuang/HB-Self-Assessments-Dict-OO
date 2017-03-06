"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1.1 Abstraction: Hide details we don't need and prevent errors from happening. Abstraction lets you focus on what the object does instead of how it does it.

   1.2 Encapsulation: Encapsulation means hiding the internal details or mechanics of how an object does something. For instance, a driver knows what the break pedal does when you drive a car, but a driver does not know the mechanics of how it's done inside the car.

   1.3 Polymorphism: Allows us to automatically do the correct behavior even if what we are working with can take many different forms. For instance, there are many kinds of anmials. Let's say in the Animal class there is a duck, dog, and cat. They will all speak in different forms but use the same method to speak. 

2. What is a class? 
	
	Classes are in fact objects, but different from object instances. The difference between the two is that Classes contain variables and method definitions, object instances do not. 

3. What is an instance attribute? 

	A property of an object!

4. What is a method?
	
	Methods are the procedures associated with a message and an object. They are the functions within a class, but not all functions are methods. For example, all squares are rectangles, but not all rectangles are squares.


5. What is an instance in object orientation?
	
	It's the transactiong/the individual occurance of a class. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   	The difference is that the attribute on the class is shared by all instances. The attribute on an instance is unique to that instance. For instance, a dog_greeting will be used by all dogs, but a dog_name will only be unique to one dog. 


"""


# Parts 2 through 5:
# Create your classes and class methods


class Account:
    """A bank account.

    	Attributes:
        balance: All accounts start at 0.
    	"""
    def __init__(self):
        """Return an account object and balance."""
       
        self.balance = 0
     
    def withdraw(self, amount):
        """Return the balance remaining after withdraw."""
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
    	"""Return the balance remaining after deposit."""
        self.balance += amount
        return self.balance


class MinBalance(Account):
    """This Class MinBalance will notify the users if he/she went over their minimum limit."""
	
    def __init__(self, minimum_balance):
    	"""Creates the minimum balance that must be maintained."""
        Account.__init__(self)
        self.min = minimum_balance

    def withdraw(self, amount):
    	"""Will return a message if customer goes under his/her minimum balance."""
        if self.balance - amount < self.min:
            print 'Sorry, minimum balance must be maintained.'
        else:
            Account.withdraw(self, amount)

Lydia = Account()
Henry = Account()

Lydia = MinBalance(500)
Henry = MinBalance(500)






