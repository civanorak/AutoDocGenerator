# Animation

> Auto-generated documentation for the **Animation** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Governor`

**Namespace:** `Animation`

#### Methods

##### `virtual` `Activate(—)`

**Returns:** `virtual void`

Destroys this governor. If it is the active governor, default governor will be activated. Activates this governor, replacing current one.

##### `virtual` `Animate(—)`

**Returns:** `virtual void`

Animates the animations within this governor. This function for the animator is called every frame by the main system. Thus calling it second time within the same frame will cause animations to progress twice.

##### `Default(—)`

**Returns:** `return`

Returns the default governor. Returns the current governor. If there is no current active governor, default governor will be returned.


### `ControllerBase`

**Namespace:** `Animation`

Controllers are required to progress animations

#### Methods

##### `ControllerBase(—)`

**Returns:** ``

Default constructor

##### `ControllerBase(Governor &governor)`

**Returns:** `explicit`

##### `virtual` `Progress(unsigned timepassed)`

**Returns:** `virtual void`

Destructor Progresses this timer by moving the timer timepassed milliseconds forwards

##### `virtual` `Add(Base &animation)`

**Returns:** `virtual void`

This function attaches the given animation to this controller

##### `virtual` `Remove(Base &animation)`

**Returns:** `virtual void`

Removes the given animation

##### `virtual` `Delete(Base &animation)`

**Returns:** `virtual void`

Deletes the given animation

##### `virtual` `GetProgress(—)`

**Returns:** `virtual unsigned`

Returns the current progress of the timer

##### `virtual` `IsControlled(—)`

**Returns:** `virtual bool`

This method allows clients to determine if the progress is controlled. If the progress is not controlled, there is no way to force the animation to stop. Therefore, animations with looping capabilities should wrap around to start over. However, if the timer is a controller then the best strategy will be to stop at the end, and return the leftover time. This way, controller can decide what to do next.

##### `AutoDestruct(—)`

**Returns:** `void`

Set a flag that will automatically destroy this controller whenever it has no animations left to control

##### `Keep(—)`

**Returns:** `void`

Resets the flag that will automatically destroy this controller whenever it has no animations left to control

##### `virtual` `Reset(—)`

**Returns:** `virtual void`

Resets the animation to the start. Animation controllers that do not support this request should silently ignore it.

##### `virtual` `SetGovernor(Governor &governor)`

**Returns:** `virtual void`

Changes the governor of this controller


### `Timer`

**Namespace:** `Animation`

Whether this controller should be collected by the garbage collector when its task is finished List of animations this controller holds This class is the most basic controller and does not support any operations. It linearly progresses animation and never stops. Most animations are expected loop under these circumstances. See Controller for additional functionality.

#### Methods

##### `virtual` `SetProgress(unsigned progress)`

**Returns:** `virtual void`

Progresses this timer by moving the timer timepassed milliseconds forwards Resets the timer, basically starting the animation from the start. Sets the progress of the timer to the given value.


### `Controller`

**Namespace:** `Animation`

Returns the current progress of the timer This method allows clients to determine if the progress is controlled. If the progress is not controlled, there is no way to force the animation to stop. Therefore, animations with looping capabilities should wrap around to start over. However, if the timer is a controller then the best strategy will be to stop at the end, and return the leftover time. This way, controller can decide what to do next. Amount of time passed since the start of the animation

#### Methods

##### `Controller(double progress = 0.0)`

**Returns:** ``

Default constructor

##### `virtual` `SetProgress(unsigned progress)`

**Returns:** `virtual void`

@name Progress modification functions @{ Progresses this controller by the given time Sets the current progress of the controller

##### `SetProgress(double progress)`

**Returns:** `void`

Sets the current progress of the controller. If the progress is a negative value, it will be subtracted from the animation length. If the animation length is 0, then the controller will immediately stop and sets the progress to 0.

##### `virtual` `Play(—)`

**Returns:** `virtual void`

Resets the controller to start from the beginning. Also resets finished and paused status and modifies the speed to be 1. @} @name Progress control functions @{ Starts this controller to run once. If the controller is marked as finished, this method will set the progress to 0 or length depending on the direction of the controller. If length is 0 and the speed is negative this method will not start playing finished controller. If the animation is paused, this function works like Resume except that this function sets controller to run once mode.

##### `virtual` `Loop(—)`

**Returns:** `virtual void`

Starts this controller in looping mode. Looping will not work when the length is 0 and the speed is set to a negative value (animation is running in reverse). If the animation is paused, this function works like Resume except that this function sets controller to looping mode

##### `virtual` `Pause(—)`

**Returns:** `virtual void`

Pauses the controller, until a Resume or Reset is issued.

##### `virtual` `Resume(—)`

**Returns:** `virtual void`

Resumes the controller. This method will not have any effect if the animation is finished.

##### `virtual` `SetSpeed(float speed)`

**Returns:** `virtual void`

Changes the speed of the controller. Speed can be negative to run animations backwards. Setting speed 0 effectively pauses the controller, however, when the speed is 0 controller will **not** report that its paused.

##### `virtual` `Reverse(—)`

**Returns:** `virtual void`

Reverses the animation direction by negating the speed.

##### `virtual` `SetLength(unsigned length)`

**Returns:** `virtual void`

Informs controller about the length of the animations its controlling. This allows Controller to seek to the end of the animation

##### `virtual` `GetSpeed(—)`

**Returns:** `virtual float`

@} @name Information functions @{ Returns the current speed of the controller

##### `IsPaused(—)`

**Returns:** `bool`

Returns whether the controller is paused. Does not check if the speed is 0 or not, setting speed to 0 will effectively pause the animation without changing paused status.

##### `IsFinished(—)`

**Returns:** `bool`

Whether the controller is finished either by reaching to the end while the speed is positive or reaching to 0 while the speed is negative

##### `IsPlaying(—)`

**Returns:** `bool`

Returns whether the controller is playing its animations right now. This method does not take speed being 0 into account.

##### `IsLooping(—)`

**Returns:** `bool`

Checks whether the controller is in loop mode. It also checks the length if the speed is negative and makes sure that the controller can actually loop


### `Provider`

**Namespace:** `Animation`

@} @name Events @{ Will be fired when the controller reaches the finished state. controller is finished either by reaching to the end while the speed is positive or reaching to 0 while the speed is negative @} Paused state Looping state Current speed Whether the controller is finished Floating point progress to avoid precision loss due to speed Length of the animations controlled by this controller This interface marks a class as animation provider


### `Base`

**Namespace:** `Animation`

Virtual destructor This function moves this animation provider into a new provider. Ownership of this new object belongs to the caller and this object could be destroyed safely. This function should create a new animation with the given controller This function should create an animation and depending on the create parameter, it should create a timer for it. Timer creation is handled by Base class therefore only passing this parameter to the constructor is enough. This is the base class for all animations. It handles some common tasks and defines the animation interface.

#### Methods

##### `Base(ControllerBase &controller)`

**Returns:** `explicit`

Sets the controller for this animation to the given controller.

##### `SetController(controller)`

**Returns:** ``

##### `Base(const Base &base)`

**Returns:** ``

Copies the animation

##### `Base(bool create=false)`

**Returns:** `explicit`

This constructor creates a new controller depending on the create parameter. Animation has the right to decline to create a new timer. Animations that does not use timers should ignore create request without any errors or side effects. If create parameter is true, the controller created for this object will have dynamic life time. This means, if all animations it has is removed from it, it will be destroyed.

##### `if(create)`

**Returns:** ``

##### `SetController(*timer)`

**Returns:** ``

##### `virtual` `SetController(ControllerBase &controller)`

**Returns:** `virtual void`

Sets the controller to the given controller.

##### `if(this->controller)`

**Returns:** ``

##### `virtual` `HasController(—)`

**Returns:** `virtual bool`

Returns whether this animation has a controller

##### `if(!controller)`

**Returns:** ``

Returns the controller of this animation

##### `virtual` `RemoveController(—)`

**Returns:** `virtual void`

Removes the controller of this animation.

##### `if(controller)`

**Returns:** ``

##### `virtual` `Progress(unsigned &leftover)`

**Returns:** `virtual bool`

This function should progress the animation. Notice that this function is called internally. Unless a change to the controller has been made and instant update of the animation is required there is no need to call this function. Returning true from this function denotes that the further progress is possible. If progress should end, leftover parameter should be set to the amount of time that cannot be progressed. Progress function should also mind uncontrollable controllers.

##### `virtual` `GetDuration(—)`

**Returns:** `virtual int`

Returns the duration of the animation if it is a known apriori. If the animation can be progressed infinitely, if it is possible to derive optimal duration, it should be returned. In case when it is impossible to determine the duration, return 0.

##### `virtual` `DeleteAnimation(—)`

**Returns:** `virtual void`

Deletes this animation. Please note that some animations are also the animation provider. In these cases trying to delete the animation will delete the provider as well. This function should be called instead of delete operator to ensure no such problem occurs.


### `Animation`

**Namespace:** `Gorgon`

This class represents an animation resource. Image animations can be created using this object. An animation object can be moved. Duplicate function should be used to copy an animation.

#### Methods

##### `Animation(—)`

**Returns:** ``

Default constructor

##### `MoveOutAsBitmap(—)`

**Returns:** `Graphics::BitmapAnimationProvider`

Conversion constructor Copy constructor is disabled, use Duplicate or DeepDuplicate Copy assignment is disabled, use Duplicate Returns the Gorgon Identifier Moves the animation out of the resource system. Use Prepare and Discard before moving out to avoid copying data. !!!

##### `if(!res)`

**Returns:** ``

This function allows loading animation with a function to load unknown resources. The supplied function should call LoadObject function of File class if the given GID is unknown. This function loads an animation resource from the given file

##### `savedata(Writer &writer)`

**Returns:** `void`

Saves the given animation as a resource. If the given animation is already a resource, its own save function will be used. Extra function can be used to save extra data related with this resource.


---

## Functions

### `Animate()`

**Returns:** `void`



### `for(auto &anim : animations)`

**Returns:** ``



### `if(maxleftover)`

**Returns:** ``



### `SetProgress(progress)`

**Returns:** ``



### `if(!ispaused && !isfinished)`

**Returns:** ``



### `if(progress<0)`

**Returns:** ``



### `if(islooping)`

**Returns:** ``



### `if(length == -1)`

**Returns:** ``



### `if(length)`

**Returns:** ``



### `for(auto &anim : animations)`

**Returns:** ``



### `if(islooping && timepassed>0)`

**Returns:** ``



### `Progress(0)`

**Returns:** ``



### `if(leftover)`

**Returns:** `else`



### `Progress(0)`

**Returns:** ``



### `FinishedEvent()`

**Returns:** ``



### `if(isfinished)`

**Returns:** ``



### `if(length == -1)`

**Returns:** ``



### `if(speed>=0)`

**Returns:** ``



### `if(length)`

**Returns:** `else`



### `while(!target)`

**Returns:** ``



### `if(gid==GID::Animation_Durations)`

**Returns:** ``



### `if(loadfn)`

**Returns:** ``



### `if(resource)`

**Returns:** ``



### `for(auto &dur : durations)`

**Returns:** ``



### `for(auto &frame : frames)`

**Returns:** ``



### `for(auto &frame : frames)`

**Returns:** ``



### `savedata(writer)`

**Returns:** ``



### `if(a)`

**Returns:** ``



### `for(auto &frame : anim)`

**Returns:** ``



### `for(auto &frame : anim)`

**Returns:** ``



### `for(auto &frame : frames)`

**Returns:** ``



### `if(img)`

**Returns:** ``



### `for(auto &child : children)`

**Returns:** ``


