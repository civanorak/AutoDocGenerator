# ScrollingWidget

&gt; Auto-generated documentation for the **ScrollingWidget** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `ScrollingWidget`

**Namespace:** `Gorgon`

#### Methods

##### `MouseScroll(Input::Mouse::EventType type, Geometry::Point location, float amount)`

**Returns:** `bool`

Report mouse scroll. This function will be called automatically for regular mouse events. This function will return false if the given mouse event is not consumed.

##### `SetOverscroll(const UnitDimension &value)`

**Returns:** `void`

Sets the amount of extra scrolling distance after the bottom-most widget is completely visible in pixels. Default is 0. Does not apply if everything is visible.

##### `GetOverscroll(—)`

**Returns:** `UnitDimension`

Returns the amount of extra scrolling distance after the bottom-most widget is completely visible in pixels.

##### `DisableSmoothScroll(—)`

**Returns:** `void`

Disables smooth scrolling of the panel

##### `SetSmoothScrollSpeed(0)`

**Returns:** ``

##### `SetSmoothScrollSpeed(const UnitDimension &value)`

**Returns:** `void`

Adjusts the smooth scrolling speed of the panel. Given value is in pixels per second, default value is 500.

##### `GetSmoothScrollSpeed(—)`

**Returns:** `UnitDimension`

Returns the smooth scrolling speed of the panel. If smooth scroll is disabled, this value will be 0.

##### `IsSmoothScrollEnabled(—)`

**Returns:** `bool`

Returns if the smooth scroll is enabled.

##### `SetMaximumScrollDuration(int value)`

**Returns:** `void`

Sets the the duration that scrolling can take. This speeds up scrolling if the distance is too much. This value is not exact and scrolling will slow down as it gets close to the target. However, total scroll duration cannot exceed twice this value. The time is in milliseconds and default value is 500.

##### `GetMaximumScrollDuration(—)`

**Returns:** `int`

Returns how long a scrolling operation can take.

##### `SetScrollDistance(const UnitDimension &vert)`

**Returns:** `void`

Sets the horizontal scroll distance per click in pixels. Default depends on the default size of the panel.

##### `SetScrollDistance({scrolldist.X, vert})`

**Returns:** ``

##### `SetScrollDistance(const UnitDimension &hor, const UnitDimension &vert)`

**Returns:** `void`

Sets the scroll distance per click in pixels. Default depends on the default size of the panel.

##### `SetScrollDistance({hor, vert})`

**Returns:** ``

##### `SetScrollDistance(const UnitPoint &dist)`

**Returns:** `void`

Sets the scroll distance per click in pixels. Default depends on the default size of the panel.

##### `GetScrollDistance(—)`

**Returns:** `UnitPoint`

Returns the scroll distance per click

##### `ensurevisible(const Geometry::Bounds &region)`

**Returns:** `void`

Ensures given region is visible

##### `enablescroll(bool vertical, bool horizontal)`

**Returns:** `void`

Enables/disables scrolling

##### `scrollto(Geometry::Point location, bool clip = false)`

**Returns:** `void`

Scrolls the contents of the panel so that the given location will be at the top left. If clip is set, the scroll amount cannot go out of the scrolling region.

##### `scrollto(location.X, location.Y, clip)`

**Returns:** ``

##### `scrollto(int x, int y, bool clip = true)`

**Returns:** `void`

Scrolls the contents of the panel so that the given location will be at the top left. If clip is set, the scroll amount cannot go out of the scrolling region.

##### `scrollby(int x, int y, bool clip = true)`

**Returns:** `void`

Scrolls the contents an additional amount.

##### `scrollto(target.X + x, target.Y + y, clip)`

**Returns:** ``

##### `scrolltox(int x)`

**Returns:** `void`

##### `scrollto(x, target.Y)`

**Returns:** ``

##### `scrolltoy(int y)`

**Returns:** `void`

##### `scrollto(target.X, y)`

**Returns:** ``

##### `maxscrolloffset(—)`

**Returns:** `Geometry::Point`

Returns the current maximum scroll offset

##### `virtual` `updatescroll(—)`

**Returns:** `virtual void`

##### `virtual` `updatebars(—)`

**Returns:** `virtual void`

##### `virtual` `moved(—)`

**Returns:** `virtual void`


---

## Functions

### `if(clip)`

**Returns:** ``



### `if(scrollspeed == 0)`

**Returns:** ``



### `if(!isscrolling)`

**Returns:** ``



### `updatebars()`

**Returns:** ``



### `if(t < c)`

**Returns:** ``



### `if(c - dist <= t)`

**Returns:** ``



### `if(t > c)`

**Returns:** `else`



### `if(c + dist >= t)`

**Returns:** ``



### `doaxis(cur.X, target.X)`

**Returns:** ``



### `doaxis(cur.Y, target.Y)`

**Returns:** ``



### `moved()`

**Returns:** ``



### `if(done == 2)`

**Returns:** ``



### `if(vscroller != nullptr)`

**Returns:** ``



### `if(hscroller != nullptr)`

**Returns:** ``



### `updatebars()`

**Returns:** ``



### `scrollto(scrolloffset)`

**Returns:** ``



### `if(scrollspeedpx == 0 && isscrolling)`

**Returns:** ``



### `if(vscroller != nullptr)`

**Returns:** ``



### `if(hscroller != nullptr)`

**Returns:** ``



### `if(!vscroll && hscroll && type == Input::Mouse::EventType::Scroll_Vert)`

**Returns:** ``



### `if(type == Input::Mouse::EventType::Scroll_Vert && vscroll)`

**Returns:** ``



### `if(type == Input::Mouse::EventType::Scroll_Hor && hscroll)`

**Returns:** ``



### `if(vertical && !vscroll)`

**Returns:** ``



### `if(!vertical && vscroll)`

**Returns:** ``



### `if(horizontal && !hscroll)`

**Returns:** ``



### `if(!horizontal && hscroll)`

**Returns:** ``



### `if(hscroll)`

**Returns:** ``



### `if(cb.Left > wb.Left)`

**Returns:** ``



### `if(cb.Right < wb.Right)`

**Returns:** `else`



### `if(vscroll)`

**Returns:** ``



### `if(cb.Top > wb.Top)`

**Returns:** ``



### `if(cb.Bottom < wb.Bottom)`

**Returns:** `else`



### `if(vscroller != nullptr)`

**Returns:** ``



### `if(hscroller != nullptr)`

**Returns:** ``


