## Singleton design pattern
A component (class) which is instantiated _only once_

## Example
* Database repository
* Object factory

## When to use 
* When the initializer call is expensive
  * -> Init once -> provide clients with the same instance
* Prevent clients from creating additional copies
* Need to take care of lazy instantiation
