# Monitor

> Auto-generated documentation for the **Monitor** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `monitordata`

**Namespace:** `internal`


---

## Functions

### `GetMonitorInfo(hMonitor, &mi)`

**Returns:** ``



### `GetScaleFactorForMonitor(hMonitor, &factor)`

**Returns:** ``



### `EnumDisplaySettings(mi.szDevice, ENUM_CURRENT_SETTINGS, &devmode)`

**Returns:** ``



### `if(mon->isprimary)`

**Returns:** ``



### `EnumDisplayMonitors(nullptr, nullptr, &internal::monitordata::MonitorEnumProc, 0)`

**Returns:** ``



### `addpadding(const Monitor *monitor, int l, int t, int r, int b)`

**Returns:** `void`



### `for(auto &mon2 : Monitor::monitors)`

**Returns:** ``



### `if(mon)`

**Returns:** ``



### `fixmonitorworkarea(int parent = 0, int x = 0, int y = 0)`

**Returns:** `static void`



### `XQueryTree(display, parent, &w, &w, &children, &child_count)`

**Returns:** ``



### `for(int i=0; i<child_count; i++)`

**Returns:** ``



### `XGetWindowAttributes(display, children[i], &xwa)`

**Returns:** ``



### `if(status == Success && item_count)`

**Returns:** ``



### `if(monitor)`

**Returns:** ``



### `addpadding(monitor, cardinals[0], cardinals[2], cardinals[1], cardinals[3])`

**Returns:** ``



### `XFree(data)`

**Returns:** ``



### `fixmonitorworkarea(children[i], x+xwa.x, y+xwa.y)`

**Returns:** ``



### `if(xrandr)`

**Returns:** ``



### `if(!sr)`

**Returns:** ``



### `for(int i=0; i<sr->ncrtc; i++)`

**Returns:** ``



### `for(int j=0; j<ci->noutput; j++)`

**Returns:** ``



### `if(oi->connection==0)`

**Returns:** ``



### `XRRFreeOutputInfo(oi)`

**Returns:** ``



### `XRRFreeCrtcInfo(ci)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `XRRFreeScreenResources(sr)`

**Returns:** ``



### `if(ci)`

**Returns:** ``



### `XRRFreeCrtcInfo(ci)`

**Returns:** ``



### `if(oi)`

**Returns:** ``



### `XRRFreeOutputInfo(oi)`

**Returns:** ``



### `XRRFreeScreenResources(sr)`

**Returns:** ``



### `if(Monitor::primary==nullptr)`

**Returns:** ``



### `fixmonitorworkarea()`

**Returns:** ``



### `fixmonitorworkarea()`

**Returns:** ``


