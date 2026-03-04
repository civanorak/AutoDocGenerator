# X11

> Auto-generated documentation for the **X11** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `windowdata`

**Namespace:** `internal`


### `xdnddata`

**Namespace:** `internal`


### `clipboardentry`

**Namespace:** `WindowManager`

@{ X11 atoms for various data identifiers @} @cond internal


### `icondata`

**Namespace:** `internal`


---

## Functions

### `waitfor_mapnotify(Display *d, XEvent *e, char *arg)`

**Returns:** `int`


@cond INTERNAL X11 display information Depends on monitor, might be moved Blank cursor to remove WindowManager cursor XRandr extension to query physical monitors Xinerama extension to query physical monitors, this is for legacy systems @{ X11 atoms for various data identifiers @} @{ waits for specific events


### `waitfor_propertynotify(Display *d, XEvent *e, char *arg)`

**Returns:** `int`



### `waitfor_cppropertynotify(Display *d, XEvent *e, char *arg)`

**Returns:** `int`



### `waitfor_selectionnotify(Display *d, XEvent *e, char *arg)`

**Returns:** `int`



### `return(e->type == SelectionNotify)`

**Returns:** ``



### `switchcontext(Gorgon::internal::windowdata &data)`

**Returns:** `void`



### `glXMakeCurrent(WindowManager::display, data.handle, data.context)`

**Returns:** ``



### `finalizerender(Gorgon::internal::windowdata &data)`

**Returns:** `void`



### `glFinish()`

**Returns:** ``



### `glFlush()`

**Returns:** ``



### `glXSwapBuffers(WindowManager::display, data.handle)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XdndInit(Gorgon::internal::windowdata *w)`

**Returns:** `void`


@}


### `init()`

**Returns:** `void`


@endcond


### `XFreePixmap(display, blank)`

**Returns:** ``



### `setenv("__GL_YIELD", "USLEEP", 1)`

**Returns:** ``



### `GetAtomName(Atom atom)`

**Returns:** `std::string`



### `XGetAtomName(WindowManager::display, atom)`

**Returns:** `return`



### `GetMousePosition(Gorgon::internal::windowdata *wind)`

**Returns:** `Geometry::Point`



### `FromImage(image)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `if(data->data)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `xeventname(XEvent &event)`

**Returns:** `std::string`



### `switch(event.type)`

**Returns:** ``



### `GetMousePosition(Gorgon::internal::windowdata *wind)`

**Returns:** `Geometry::Point`



### `XdndInit(Gorgon::internal::windowdata *w)`

**Returns:** `void`



### `xeventname(XEvent &event)`

**Returns:** `std::string`



### `GetAtomName(Atom atom)`

**Returns:** `std::string`



### `buttonfromx11(unsigned btn)`

**Returns:** `Input::Mouse::Button`



### `mapx11key(KeySym key, unsigned int keycode)`

**Returns:** `Input::Keyboard::Key`



### `assertkeys(Window &wind, Gorgon::internal::windowdata *data)`

**Returns:** `void`



### `xeventname(XEvent &event)`

**Returns:** `std::string`



### `waitfor_mapnotify(Display *d, XEvent *e, char *arg)`

**Returns:** `int`


X11 display information Depends on monitor, might be moved Blank cursor to remove WindowManager cursor XRandr extension to query physical monitors Xinerama extension to query physical monitors, this is for legacy systems @{ waits for specific events


### `waitfor_propertynotify(Display *d, XEvent *e, char *arg)`

**Returns:** `int`



### `waitfor_cppropertynotify(Display *d, XEvent *e, char *arg)`

**Returns:** `int`



### `waitfor_selectionnotify(Display *d, XEvent *e, char *arg)`

**Returns:** `int`



### `getanywindow()`

**Returns:** `::Window`



### `handleclipboardevent(XEvent event)`

**Returns:** `void`



### `handledndevent(XEvent event, Window &wind)`

**Returns:** `void`



### `handleinputevent(XEvent event, Window &wind)`

**Returns:** `void`



### `GetX4Prop(Atom atom, ::Window w, const T_ &def)`

**Returns:** `T_`



### `XFree(data)`

**Returns:** ``


