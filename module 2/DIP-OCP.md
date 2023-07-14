# dependency inversion principle

## dependencies
- relationship (assoctions) between various entities
- dependency: when one entity depends on another entity
    - for example in python one package can depend on another package
- safe dependencies: when a change in one entity does not affect the other entity

## stable design
- stable design: when a change in one entity does not affect the other entity
- stable design is achieved by using abstractions

## abstraction
- abstraction: a simplified representation of a complex entity
- abstraction is achieved by using interfaces
- abstract things change less frequently than concrete things

## procedural programming vs object oriented programming
- procedural programming: code is organized around procedures or functions
- object oriented programming: code is organized around objects

# open closed principle

## open for extension, closed for modification
- open for extension: the behavior of a module can be extended
    - example: adding a new algorithm to a module
- closed for modification: the source code of a module is not modified
    - example: adding a new algorithm to a module without modifying the source code of the module
- the aim is to write code that does not have to be modified when new functionality is added

