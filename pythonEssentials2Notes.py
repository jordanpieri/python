#import math

#for name in dir(math):
#    print(name, end="\t")

# for name in dir(print):
#     print(name, end="\n")

# from random import random, seed
#
# seed(0)
#
# for i in range(5):
#     print(random())



# # 3.2.5 The object approach: a stack from scratch
# class TheSimplestClass:
#     pass
#
#
# my_first_object = TheSimplestClass()
#
#
# # print(my_first_object)
#
# class This_Is_A_Class:
#     pass
#
#
# this_is_an_object = This_Is_A_Class()
#
#
# class Stack:  # Defining the 'Stack' class.
#     def __init__(self):  # Defining the constructor function, declaring the parameter 'self' to identify the object
#         # the constructor's name is always __init__;
#         # it has to have at least one parameter (we'll discuss this later); the parameter is used to represent the newly created object – you can use the parameter to manipulate the object, and to enrich it with the needed properties; you'll make use of this soon;
#         # note: the obligatory parameter is usually named self – it's only a convention, but you should follow it – it simplifies the process of reading and understanding your code.
#         #     print("Hi!",self)
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#
# class AddingStack(Stack): # Invoking the superclass 'Stack' while Defining the Sub-Class 'AddingStack'.
#     def __init__(self): # Defining the constructor function for Sub-Class 'AddingStack'
#         Stack.__init__(self) # Explicitly invoking the 'Stack' superclass's constructor
#         self.__sum = 0 # Initializing new property (and private variable) 'sum' in the Sub-Class 'AddingStack'
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
#
#     def get_sum(self):
#         return self.__sum
#
#
#
#
# # Follow-up Notes for later, read over this several times but still didn't absorb...:
# # https://www.netacad.com/launch?id=a0ad2851-c6d4-4980-a9a7-98b3f3108166&tab=curriculum&view=c4a4bacf-39c2-51f0-a56d-7a882cbdbdce
# # The second line of the constructor's body creates a property named __sum – it will store the total of all the stack's values.
# #
# # But the line before it looks different. What does it do? Is it really necessary? Yes, it is.
# #
# # Contrary to many other languages, Python forces you to explicitly invoke a superclass's constructor. Omitting this point will have harmful effects – the object will be deprived of the __stack_list list. Such a stack will not function properly.
# #
# # This is the only time you can invoke any of the available constructors explicitly – it can be done inside the subclass's constructor.
# #
# # Note the syntax:
# #
# # you specify the superclass's name (this is the class whose constructor you want to run)
# # you put a dot (.)after it;
# # you specify the name of the constructor;
# # you have to point to the object (the class's instance) which has to be initialized by the constructor – this is why you have to specify the argument and use the self variable here; note: invoking any method (including constructors) from outside the class never requires you to put the self argument at the argument's list – invoking a method from within the class demands explicit usage of the self argument, and it has to be put first on the list.
# #
# #
# #
#
# newstack = AddingStack()
# newstack.push(4)
# print(newstack.get_sum())
# newstack.push(11)
# print(newstack.get_sum())
# print(newstack.pop())
#
# print(newstack.get_sum())
#
#
#
#
#
#
# #
# #
# # stack_object = Stack()  # Instantiating the object.
# # # print(len(stack_object.__stack_list))
# #
# # stack_object.push(3)
# # stack_object.push(2)
# # stack_object.push(1)
# # # print(len(stack_object.__stack_list))
# #
# # print(stack_object.pop())
# # print(stack_object.pop())
# # print(stack_object.pop())
# # # print(len(stack_object.__stack_list))
# #
# # stack_object_1 = Stack()
# # stack_object_2 = Stack()
# #
# # stack_object_1.push(3)
# # stack_object_2.push(stack_object_1.pop())
# #
# # print(stack_object_2.pop())
# #
# # little_stack = Stack()
# # another_stack = Stack()
# # funny_stack = Stack()
# #
# # little_stack.push(1)
# # another_stack.push(little_stack.pop() + 1)
# # funny_stack.push(another_stack.pop() - 2)
# #
# # print(funny_stack.pop())

# # # 3.2.8 LAB Counting stack
# # We showed you recently how to extend Stack possibilities by defining a new class (i.e., a subclass) which retains all inherited traits and adds some new ones.
# #
# # Your task is to extend the Stack class behavior in such a way so that the class is able to count all the elements that are pushed and popped (we assume that counting pops is enough). Use the Stack class we've provided in the editor.
# #
# # Follow the hints:
# #
# # introduce a property designed to count pop operations and name it in a way which guarantees it is hidden;
# # initialize it to zero inside the constructor;
# # provide a method which returns the value currently assigned to the counter (name it get_counter()).
# # Complete the code in the editor. Run it to check whether your code outputs 100.
#
# class Stack:
#     def __init__(self):
#         self.__stk = []
#
#     def push(self, val):
#         self.__stk.append(val)
#
#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val
#
#
# class CountingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__ops_counter = 0
#
#     def get_counter(self):
#         return self.__ops_counter
#
#     def pop(self):
#         self.__ops_counter += 1
#
#
#
# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())

# # 3.2.9   LAB   Queue aka FIFO
# # As you already know, a stack is a data structure realizing the LIFO (Last In – First Out) model. It's easy and you've already grown perfectly accustomed to it.
# #
# # Let's try something new now. A queue is a data model characterized by the term FIFO: First In – First Out. Note: a regular queue (line) you know from shops or post offices works exactly in the same way – a customer who came first is served first too.
# #
# # Your task is to implement the Queue class with two basic operations:
# #
# # put(element), which puts an element at end of the queue;
# # get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.)
# # Follow the hints:
# #
# # use a list as your storage (just like we did with the stack)
# # put() should append elements to the beginning of the list, while get() should remove the elements from the end of the list;
# # define a new exception named QueueError (choose an exception to derive it from) and raise it when get() tries to operate on an empty list.
# # Complete the code we've provided in the editor. Run it to check whether its output is similar to ours.
#
# class QueueError(IndexError):  # Choose base class for the new exception.
#     # def __init__(self):
#     #     self.IndexError
#     pass
#
# class Queue:
#     def __init__(self):
#         self.q=[]
#
#     def put(self, elem):
#         self.q.insert(0,elem)
#
#     def get(self):
#         if len(self.q) > 0:
#             elem = self.q[-1]
#             del self.q[-1]
#             return(elem)
#         else: raise QueueError
#
# # que = Queue()
# # que.put(1)
# # que.put("dog")
# # que.put(False)
# # try:
# #     for i in range(4):
# #         print(que.get())
# # except:
# #     print("Queue error")
#
# # 3.2.10   LAB   Queue aka FIFO: part 2
# # Your task is to slightly extend the Queue class's capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.
# #
# # Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.
# #
# # Below you can copy the code we used in the previous lab:
#
# class SuperQueue(Queue):
#     #def __init__(self):
#         #Queue __init__(self):
#     def isempty(self):
#         if len(self.q) == 0:
#             return True
#         if len(self.q) > 0:
#             return False
#
# que = SuperQueue()
# que.put(1)
# que.put("dog")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Queue empty")

#
# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val
#
#     def set_second(self, val):
#         self.second = val
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
#
# example_object_2.set_second(3)
#
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5
#
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

# # 3.3.2 Class variables
# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)
#
# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)

# # 3.3.3 Checking an attribute's existence
# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object = ExampleClass(1)
# print(example_object.a)
#
# if hasattr(example_object, 'b'):
#     print(example_object.b)
#
# class ExampleClass:
#     attr = 1
#
#
# print(hasattr(ExampleClass, 'attr'))
# print(hasattr(ExampleClass, 'prop'))

#
# class ExampleClass:
#     a = 1
#     def __init__(self):
#         self.b = 2
#
#
# example_object = ExampleClass()
#
# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

