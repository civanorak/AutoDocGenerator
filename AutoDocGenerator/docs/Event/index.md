# Event

> Auto-generated documentation for the **Event** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `HandlerBase`

**Namespace:** `event`

#### Methods

##### `virtual` `Fire(std::mutex &locker, Source_ *, Params_...)`

**Returns:** `virtual void`


### `EmptyHandlerFn`

**Namespace:** `event`

#### Methods

##### `virtual` `Fire(std::mutex &locker, Source_ *, Params_...)`

**Returns:** `virtual void`

##### `f(—)`

**Returns:** ``


### `ArgsHandlerFn`

**Namespace:** `event`

#### Methods

##### `virtual` `Fire(std::mutex &locker, Source_ *, Params_... args)`

**Returns:** `virtual void`


### `FullHandlerFn`

**Namespace:** `event`

#### Methods

##### `virtual` `Fire(std::mutex &locker, Source_ *source, Params_... args)`

**Returns:** `virtual void`


### `Event`

**Namespace:** `event`

This class provides event mechanism. Different function signatures are allowed to as event handlers. These are:  * <b>`void fn()`</b> neither event source nor event parameters are supplied. * <b>`void fn(Params_... params)`</b> parameters will be passed * <b>`void fn(Source_ &source, Params_... params)`</b> the source and parameters will be passed  Class members or lambda functions can also be used as event handlers. An event handler can be registered using Register function.

#### Methods

##### `static_assert(std::is_same<Source_, void>::value, "Empty constructor cannot be used.")`

**Returns:** ``

Data type for tokens Constructor for empty source

##### `static_assert(!std::is_same<Source_, void>::value, "Filling constructor is not required, use the default.")`

**Returns:** ``

Constructor for class specific source

##### `ASSERT(source, "Source cannot be nullptr")`

**Returns:** ``

Constructor for class specific source

##### `static_assert(!std::is_same<Source_, void>::value, "Filling constructor is not required, use the default.")`

**Returns:** ``

##### `Swap(event)`

**Returns:** ``

Move constructor

##### `g(access)`

**Returns:** `std::lock_guard<std::mutex>`

Destructor

##### `g(access)`

**Returns:** `std::lock_guard<std::mutex>`

Copy constructor is disabled Copy assignment is disabled Move assignment, should be called synchronized

##### `Swap(other)`

**Returns:** ``

##### `Swap(Event &other)`

**Returns:** `void`

Swaps two Events, used for move semantics

##### `swap(source, other.source)`

**Returns:** ``

##### `swap(handlers, other.handlers)`

**Returns:** ``

##### `Register(F_ fn)`

**Returns:** `Token`

Registers a new function to be called when this event is triggered. This function can be called from event handler of the same event. The registered event handler will be called immediately in this case. If you register a class with a () operator, this class will be copied. If you require call to be made to the same instance, instead of using `Register(a)` use `Register(a, &decltype(a)::operator())`

##### `ASSERT(!movedout, "This event is moved out of")`

**Returns:** ``

##### `g(access)`

**Returns:** `std::lock_guard<std::mutex>`

##### `ASSERT(!movedout, "This event is moved out of")`

**Returns:** ``

Registers a new function to be called when this event is triggered. This variant is designed to be used with member functions. **Example:** @code A a; b.ClickEvent.Register(a, &A::f); @endcode  This function can be called from event handler of the same event. The registered event handler will be called immediately in this case.

##### `Register(f)`

**Returns:** `return`

##### `Unregister(Token token)`

**Returns:** `void`

Unregisters the given marked with the given token. This function performs no operation if the token is not contained within this event. A handler can be unregistered safely while the event is being fired. In this case, if the event that is being deleted is different from the current event handler, the deleted event handler might have already been fired. If not, it will not be fired.

##### `ASSERT(!movedout, "This event is moved out of")`

**Returns:** ``

##### `g(access)`

**Returns:** `std::lock_guard<std::mutex>`

##### `g(firemtx)`

**Returns:** `std::lock_guard<std::recursive_mutex>`

Fire this event. This function will never allow recursive firing from the same thread, i.e. an event handler cannot cause this event to be fired again.

##### `ASSERT(!movedout, "This event is moved out of")`

**Returns:** ``

##### `for(iterator=handlers.begin()`

**Returns:** ``

##### `catch(...)`

**Returns:** ``

##### `Clear(—)`

**Returns:** `void`

Removes all registered handlers from this event

##### `g1(firemtx)`

**Returns:** `std::lock_guard<std::recursive_mutex>`

##### `g2(access)`

**Returns:** `std::lock_guard<std::mutex>`


---

## Functions

### `createhandler_internal(F_ fn)`

**Returns:** ``



### `createhandler_internal(F_ fn)`

**Returns:** ``



### `createhandler_internal(F_ fn)`

**Returns:** ``



### `create_handler(F_ fn)`

**Returns:** ``



### `create_handler(F_ fn)`

**Returns:** ``



### `swap(Event<Source_, Args_...> &l, Event<Source_, Args_...> &r)`

**Returns:** `void`


Swaps two events

