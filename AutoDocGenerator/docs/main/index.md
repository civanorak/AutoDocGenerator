# Main

> Auto-generated documentation for the **Main** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Runner`

**Namespace:** `internal`

Defines the abstract class of Runner. Runners take the control of the code execution, calling any necessary functions as the events occur.

#### Methods

##### `virtual` `Run(—)`

**Returns:** `virtual void`

Takes the control of the execution until Quit is called.

##### `virtual` `Step(—)`

**Returns:** `virtual void`

Runs a single frame

##### `virtual` `Quit(—)`

**Returns:** `virtual void`

Should quit after the current frame is completed for a graceful exit.


---

## Enums

### `Type`

**Namespace:** `AutosizeModes`


---

## Functions

### `Animate()`

**Returns:** `void`



### `gorgon_exit()`

**Returns:** `void`



### `Initialize(const std::string &name)`

**Returns:** `void`



### `atexit(&gorgon_exit)`

**Returns:** ``



### `Tick()`

**Returns:** `void`



### `if(!inited)`

**Returns:** ``



### `for(auto &fn : once)`

**Returns:** ``



### `fn()`

**Returns:** ``



### `for(auto &p : timeouts)`

**Returns:** ``



### `if(p.second.first <= Time::internal::deltatime)`

**Returns:** ``



### `for(auto it=timeouts.begin()`

**Returns:** ``



### `if(it->second.first == 0 || it->second.first == -1)`

**Returns:** ``



### `for(auto &p : intervals)`

**Returns:** ``



### `for(auto it=intervals.begin()`

**Returns:** ``



### `Render()`

**Returns:** `void`



### `for(auto &w : Window::Windows)`

**Returns:** ``



### `NextFrame(bool render)`

**Returns:** `void`



### `Render()`

**Returns:** ``



### `if(currentdelta<16)`

**Returns:** ``



### `Tick()`

**Returns:** ``



### `BeforeFrameEvent()`

**Returns:** ``



### `UpdateFrame()`

**Returns:** `void`



### `Render()`

**Returns:** ``



### `Tick()`

**Returns:** ``



### `BeforeFrameEvent()`

**Returns:** ``



### `grd(once_mtx)`

**Returns:** `std::lock_guard<std::mutex>`



### `AlterTimeout(size_t timeout, unsigned long after)`

**Returns:** `void`



### `DisableTimeout(size_t timeout)`

**Returns:** `void`



### `TimeoutExists(size_t timeout)`

**Returns:** `bool`



### `AlterInterval(size_t timeout, unsigned long after)`

**Returns:** `void`



### `DisableInterval(size_t timeout)`

**Returns:** `void`



### `IntervalExists(size_t timeout)`

**Returns:** `bool`



### `Initialize(const std::string &systemname)`

**Returns:** `void`


Initializes the entire system except for graphics and UI. Graphics should be initialized after a window is created and UI should be initialized last.


### `GetSystemName()`

**Returns:** `inline std::string`


Returns the name of the current system


### `Tick()`

**Returns:** `void`


Performs various operations that are vital to system execution. These include OS message handling, animation and sound progressions, time progression and delta time calculation. NextFrame function should be preferred if the frame delay is tolerable.


### `Render()`

**Returns:** `void`


This function calls the starts the rendering pipeline. Rendering should be last operation of a frame.


### `NextFrame(bool render = true)`

**Returns:** `void`


This function marks the end of current frame and starts the next one. This function calls the Tick function at start of the next frame. Additionally, this function calls end of frame tasks such as rendering. Before starting the next frame, a certain delay is performed. This delay aims to set each frame duration to 16ms, this duration sets the frames per second to 62.5. This delay greatly reduces the system load of simple games/applications.


### `UpdateFrame()`

**Returns:** `inline void`


This method works similar to next frame, however, no delay is done. This function allows an application to update the display and perform OS tasks while still continuing operation.


### `RegisterOnce(F_ fn, A_ && ...args)`

**Returns:** `void`


Registers a function to be run at the start of the next frame.


### `RegisterTimeout(unsigned long after, F_ fn, A_ && ...args)`

**Returns:** `size_t`


Registers a function to be run after given time in milliseconds.


### `AlterTimeout(size_t timeout, unsigned long after)`

**Returns:** `void`


Alters timeout to fire after the given time from now in milliseconds


### `DisableTimeout(size_t timeout)`

**Returns:** `void`



### `TimeoutExists(size_t timeout)`

**Returns:** `bool`



### `RegisterInterval(unsigned long after, F_ fn, A_ && ...args)`

**Returns:** `size_t`


Registers a function to be run regularly at given time in milliseconds. Do not use this system for games! Use timebased simulation and animations.


### `AlterInterval(size_t timeout, unsigned long after)`

**Returns:** `void`


Alters interval time in milliseconds


### `DisableInterval(size_t timeout)`

**Returns:** `void`



### `IntervalExists(size_t timeout)`

**Returns:** `bool`



### `TopLevel(0)`

**Returns:** `VirtualPanel`



### `Draw_Signal(IntervalObject &interval)`

**Returns:** `void`



### `for(utils::Collection<WidgetBase>::Iterator i=DrawQueue.First()`

**Returns:** ``



### `deactivatetoplevels(VirtualPanel *except)`

**Returns:** `void`



### `for(auto it=toplevels.First()`

**Returns:** ``



### `RegisterLoaders(resource::File &File)`

**Returns:** `void`



### `Initialize(GGEMain &Main, int TopLevelOrder)`

**Returns:** `void`



### `loadwidgets(const std::string &filename, bool prepare=true)`

**Returns:** `gge::resource::File &`



### `RegisterLoaders(WidgetFile)`

**Returns:** ``



### `LoadWidgets(const std::string &filename)`

**Returns:** `gge::resource::File &`



### `loadwidgets(filename, true)`

**Returns:** `return`



### `loadwidgets(bool prepare=true)`

**Returns:** `gge::resource::File &`



### `RegisterLoaders(WidgetFile)`

**Returns:** ``



### `for(auto it=filenamelist.begin()`

**Returns:** ``



### `if(filename=="")`

**Returns:** ``



### `LoadWidgets()`

**Returns:** `gge::resource::File &`



### `loadwidgets(true)`

**Returns:** `return`



### `InitializeApplication(const std::string &systemname, const std::string &windowtitle, const std::string &uifile, int width, int height, os::IconHandle icon)`

**Returns:** `void`



### `loadwidgets(uifile, false)`

**Returns:** ``



### `Initialize(Main)`

**Returns:** ``



### `InitializeApplication(const std::string &systemname, const std::string &windowtitle, int width, int height, os::IconHandle icon)`

**Returns:** `void`



### `loadwidgets(false)`

**Returns:** ``



### `Initialize(Main)`

**Returns:** ``



### `RegisterLoaders(resource::File &File)`

**Returns:** `void`



### `RegisterLoaders(resource::File *File)`

**Returns:** `inline void`



### `InitializeApplication(const std::string &systemname, const std::string &windowtitle, const std::string &uifile, int width=700, int height=550, os::IconHandle icon=0)`

**Returns:** `void`



### `InitializeApplication(const std::string &systemname, const std::string &windowtitle, int width, int height, const std::string &uifile, os::IconHandle icon=0)`

**Returns:** `inline void`



### `InitializeApplication(systemname, windowtitle, uifile, width, height, icon)`

**Returns:** ``



### `InitializeApplication(const std::string &systemname, const std::string &windowtitle, int width=700, int height=550, os::IconHandle icon=0)`

**Returns:** `void`



### `Initialize(GGEMain &Main, int TopLevelOrder=1)`

**Returns:** `void`


