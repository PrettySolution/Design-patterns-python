###### Singleton Allocator
One vary simple way of implementing a singleton in Python is by essentially rewriting the Allocator `__new__`.
Here you check whether or not some static instance has already been created, and whatever happens we return 
the same instance (Object).
However, as soon as you start sticking things into the initialize you're going to see problems: 
several Objects are going to be initialized. 
BTW, whatever happens `__init__` is called immediately after `__new__`.