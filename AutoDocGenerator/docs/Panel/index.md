# Panel

&gt; Auto-generated documentation for the **Panel** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Panel`

**Namespace:** `gge`

#### Methods

##### `setallowmove(false)`

**Returns:** ``

##### `setupvscroll(true, true, true)`

**Returns:** ``

##### `setblueprint(*WR.Panel)`

**Returns:** ``

##### `FillContainer(—)`

**Returns:** `void`

##### `if(Container)`

**Returns:** ``

##### `Move(0, 0)`

**Returns:** ``

##### `HideScroll(—)`

**Returns:** `void`

##### `ShowScroll(—)`

**Returns:** `void`

##### `Dock(DockDirection direction)`

**Returns:** `void`

##### `prepare(—)`

**Returns:** ``

##### `margins(0)`

**Returns:** `utils::Margins`

##### `switch(direction)`

**Returns:** ``

##### `Move(-margins.Left, -margins.Top)`

**Returns:** ``

##### `Move(-margins.Left, -margins.Top)`

**Returns:** ``

##### `setPadding(const utils::Margins &value)`

**Returns:** `void`

##### `getPadding(—)`

**Returns:** `utils::Margins`

##### `wr_loaded(—)`

**Returns:** `void`

##### `setblueprint(*WR.Panel)`

**Returns:** ``


### `Panel`

**Namespace:** `Gorgon`

#### Methods

##### `Panel(const UI::Template &temp)`

**Returns:** `explicit`

##### `distributeparentboundschanged(—)`

**Returns:** ``

##### `GetCalculatedInteriorSize(UI::Dimension::Unit unit)`

**Returns:** `UI::UnitSize`

##### `virtual` `EnableScroll(bool vertical, bool horizontal)`

**Returns:** `virtual void`

Controls whether scrolling will be enabled vertically or horizontally. It is possible to use ScrollTo function without enabling scrolling but the user will not be able to scroll in this case. Enabling scrolling will also display a scrollbar. Depending on the theme it might not be visible until there is something to scroll. Disabling scrolling will not take the scroll position to top.

##### `IsVerticalScrollEnabled(—)`

**Returns:** `bool`

Whether vertical scrolling is enabled

##### `IsHorizontalScrollEnabled(—)`

**Returns:** `bool`

Whether horizontal scrolling is enabled

##### `distributeparentenabled(value)`

**Returns:** ``

Sets the width of the widget Sets the height of the widget

##### `SetSizes(int spacing, int unitwidth)`

**Returns:** `void`

The spacing should be left between widgets Returns the unit width for a widget. This size is enough to have a bordered icon. Widgets should be sized according to unit width and spacing. A single unit width would be too small for most widgets. Overrides default spacing and unitwidth

##### `UseDefaultSizes(—)`

**Returns:** `void`

Return to use default sizes

##### `ScrollTo(Geometry::Point location, bool clip = false)`

**Returns:** `void`

Scrolls the contents of the panel so that the given location will be at the top left. If clip is set, the scroll amount cannot go out of the scrolling region.

##### `ScrollTo(location.X, location.Y, clip)`

**Returns:** ``

##### `ScrollTo(int x, int y, bool clip = true)`

**Returns:** `void`

Scrolls the contents of the panel so that the given location will be at the top left. If clip is set, the scroll amount cannot go out of the scrolling region.

##### `scrollto(x, y, clip)`

**Returns:** ``

##### `ScrollTo(int y, bool clip = true)`

**Returns:** `void`

Scrolls the contents of the panel so that the given location will be at the top.

##### `ScrollTo(target.X, y, clip)`

**Returns:** ``

##### `ScrollBy(int y, bool clip = true)`

**Returns:** `void`

Scrolls the contents an additional amount.

##### `ScrollTo(target.X, target.Y + y, clip)`

**Returns:** ``

##### `ScrollBy(int x, int y, bool clip = true)`

**Returns:** `void`

Scrolls the contents an additional amount.

##### `ScrollTo(target.X + x, target.Y + y, clip)`

**Returns:** ``

##### `ScrollOffset(—)`

**Returns:** `Geometry::Point`

Returns the current scroll offset, updates during animations

##### `ScrollTarget(—)`

**Returns:** `Geometry::Point`

Returns the current scroll offset target.

##### `MaxScrollOffset(—)`

**Returns:** `Geometry::Point`

Returns the current maximum scroll offset

##### `maxscrolloffset(—)`

**Returns:** `return`

##### `Resize(size, {false, false})`

**Returns:** ``

##### `Resize(const UI::UnitSize &size, std::pair<bool, bool> interiorsized)`

**Returns:** `void`

##### `distributeparentboundschanged(—)`

**Returns:** ``

##### `virtual` `updatecontent(—)`

**Returns:** `virtual void`

##### `distributeparentenabled(state)`

**Returns:** ``

##### `distributeparentenabled(state)`

**Returns:** ``

##### `distributeparentboundschanged(—)`

**Returns:** ``


---

## Enums

### `DockDirection`

**Namespace:** `gge`


---

## Functions

### `MouseScroll(type, location, amount)`

**Returns:** `return`



### `enablescroll(true, false)`

**Returns:** ``



### `switch(key)`

**Returns:** ``



### `ScrollBy(scrolldistpx.Y)`

**Returns:** ``



### `ScrollBy(-scrolldistpx.Y)`

**Returns:** ``



### `FocusFirst()`

**Returns:** ``



### `if(state)`

**Returns:** ``



### `switch(key)`

**Returns:** ``



### `if(size.Width==0 && size.Height==0)`

**Returns:** ``



### `if(interiorsized.first != true)`

**Returns:** ``



### `if(interiorsized.second != true)`

**Returns:** ``



### `if(interiorsized.first || interiorsized.second)`

**Returns:** ``



### `childboundschanged(nullptr)`

**Returns:** ``



### `distributeparentboundschanged()`

**Returns:** ``



### `for(auto &w : widgets)`

**Returns:** ``



### `FocusFirst()`

**Returns:** ``



### `RemoveFocus()`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `RemoveFocus()`

**Returns:** ``



### `updatecontent()`

**Returns:** ``



### `updatebars()`

**Returns:** ``



### `for(auto &c : widgets)`

**Returns:** ``



### `ensurevisible(wb)`

**Returns:** ``



### `enablescroll(vertical, horizontal)`

**Returns:** ``



### `if(ans.Extender)`

**Returns:** ``



### `if(!ans.Transformed)`

**Returns:** ``



### `if(issizesset)`

**Returns:** ``



### `if(issizesset)`

**Returns:** ``


