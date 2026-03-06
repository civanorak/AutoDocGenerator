# ListboxBase

&gt; Auto-generated documentation for the **ListboxBase** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `ListboxType`

**Namespace:** `gge`


### `ListboxDragHandle`

**Namespace:** `listbox`

#### Methods

##### `virtual` `TypeID(—)`

**Returns:** `virtual int`


### `Base`

**Namespace:** `listbox`

#### Methods

##### `virtual` `IsEnabled(—)`

**Returns:** `virtual bool`

##### `virtual` `Enable(—)`

**Returns:** `virtual void`

##### `virtual` `Disable(—)`

**Returns:** `virtual void`

##### `virtual` `Draw(—)`

**Returns:** `virtual void`

##### `virtual` `Focus(—)`

**Returns:** `virtual bool`

##### `virtual` `SetBlueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `setblueprint(bp)`

**Returns:** ``

##### `virtual` `MouseHandler(input::mouse::Event::Type event, utils::Point location, int amount)`

**Returns:** `virtual bool`

##### `if(event==Event::DragOver)`

**Returns:** ``

##### `if(event==Event::DragMove)`

**Returns:** `else`

##### `if(lastdragtime!=0)`

**Returns:** ``

##### `if(lastdragtime!=0)`

**Returns:** ``

##### `if(l!=before && l+1!=before && l>=0 && l<elementcount)`

**Returns:** ``

##### `movebefore(l, before)`

**Returns:** ``

##### `if(before>l)`

**Returns:** ``

##### `if(h.index>=elementcount)`

**Returns:** `else`

##### `adjustitems(—)`

**Returns:** ``

##### `if(event==Event::DragOut)`

**Returns:** `else`

##### `if(event==Event::DragDrop)`

**Returns:** `else`

##### `virtual` `Resize(utils::Size Size)`

**Returns:** `virtual void`

##### `if(autoheight)`

**Returns:** ``

##### `adjustheight(—)`

**Returns:** ``

##### `checkelementlist(—)`

**Returns:** ``

##### `virtual` `GetSize(—)`

**Returns:** `virtual utils::Size`

##### `virtual` `draw(—)`

**Returns:** `virtual void`

##### `virtual` `movebefore(unsigned item, unsigned before)`

**Returns:** `virtual void`

##### `virtual` `loosefocus(bool force)`

**Returns:** `virtual bool`

##### `if(force)`

**Returns:** ``

##### `virtual` `detach(ContainerBase *container)`

**Returns:** `virtual bool`

##### `virtual` `containerenabledchanged(bool state)`

**Returns:** `virtual void`

##### `virtual` `located(ContainerBase* container, utils::SortedCollection<WidgetBase>::Wrapper *w, int Order)`

**Returns:** `virtual void`

##### `if(BaseLayer)`

**Returns:** ``

##### `setautoheight(const bool &value)`

**Returns:** `void`

##### `if(autoheight!=value)`

**Returns:** ``

##### `adjustheight(—)`

**Returns:** ``

##### `checkelementlist(—)`

**Returns:** ``

##### `getautoheight(—)`

**Returns:** `bool`

##### `setcolumns(const int &value)`

**Returns:** `void`

##### `if(columns!=value)`

**Returns:** ``

##### `adjustheight(—)`

**Returns:** ``

##### `checkelementlist(—)`

**Returns:** ``

##### `getcolumns(—)`

**Returns:** `int`

##### `setallowreorder(const bool &value)`

**Returns:** `void`

##### `if(allowreorder!=value)`

**Returns:** ``

##### `getallowreorder(—)`

**Returns:** `bool`

##### `adjustheight(—)`

**Returns:** `void`

##### `if(autoheight)`

**Returns:** ``

##### `checkelementlist(—)`

**Returns:** ``

##### `checkelementlist(—)`

**Returns:** `void`

##### `elementadded(*element)`

**Returns:** ``

##### `adjustitems(—)`

**Returns:** ``

##### `itemheightchanged(—)`

**Returns:** `void`

##### `setitemcount(int count)`

**Returns:** `void`

##### `virtual` `elementadded(R_ &element)`

**Returns:** `virtual void`

##### `virtual` `elementheight(—)`

**Returns:** `virtual int`

##### `virtual` `trigger(R_ &element, int index)`

**Returns:** `virtual void`

##### `virtual` `adjustitems(—)`

**Returns:** `virtual void`

##### `begindrag(IListItem &item, int index, gge::utils::Point location)`

**Returns:** `void`

##### `virtual` `wr_loaded(—)`

**Returns:** `virtual void`

##### `virtual` `setblueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`


---

## Functions

### `CastToString(const T_ &v, std::string &str)`

**Returns:** `typename std::enable_if<utils::has_stringoperator<T_>::value>::type`



### `EmptyStringConverter(const T_ &v, std::string &s)`

**Returns:** `void`



### `if(size.Width==0)`

**Returns:** ``



### `for(auto it=representations.First()`

**Returns:** ``



### `itemheightchanged()`

**Returns:** ``


