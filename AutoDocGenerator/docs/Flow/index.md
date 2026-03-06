# Flow

&gt; Auto-generated documentation for the **Flow** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Flow`

**Namespace:** `Organizers`


### `BreakTag`

**Namespace:** `Organizers`

Is used to mark line breaks


### `Modifier`

**Namespace:** `Organizers`


### `Flower`

**Namespace:** `Organizers`


---

## Enums

### `Type`

**Namespace:** `Organizers`


---

## Functions

### `if(tight)`

**Returns:** ``



### `if(align == Graphics::TextAlignment::Center)`

**Returns:** ``



### `if(align == Graphics::TextAlignment::Right)`

**Returns:** `else`



### `if(fractionals)`

**Returns:** ``



### `for(auto &cell : row)`

**Returns:** ``



### `for(auto &widget : att)`

**Returns:** ``



### `for(auto it = p.first; it != p.second; it++)`

**Returns:** ``



### `switch(it->second.type)`

**Returns:** ``



### `if(x + w + xoff > width && rowc > 0 && breaks == 0)`

**Returns:** ``



### `if(breaks)`

**Returns:** ``



### `dorow()`

**Returns:** ``



### `if(h > maxy)`

**Returns:** ``



### `dorow()`

**Returns:** ``



### `if(usedefaultspacing)`

**Returns:** ``



### `Reorganize()`

**Returns:** ``



### `InsertBreak(order)`

**Returns:** ``



### `InsertBreak(order + 1)`

**Returns:** ``



### `Reorganize()`

**Returns:** ``



### `if(fn == &std::endl<char, std::char_traits<char>>)`

**Returns:** ``



### `flow(Break)`

**Returns:** ``



### `Add(b)`

**Returns:** ``



### `Add(title)`

**Returns:** ``



### `SetSpacing(int value)`

**Returns:** `void`


Adds the given widget to the attached container. Adds the given text as a label to the attached container When supplied with std::endl, inserts a line break. Inserts a line break. Changes the alignment of the widgets if the line is not full Sets the size of the next widget in unit sizes Adds a button to the container Appends a modifier to the flow organizer Constructs a new flow organizer specifying spacing between widgets Constructs a new list organizer, spaces between widgets are obtained from the active parent Sets the spacing between the lines


### `reorganize()`

**Returns:** ``



### `UseDefaultSpacing()`

**Returns:** `void`


Starts using default spacing.


### `reorganize()`

**Returns:** ``



### `GetSpacing()`

**Returns:** `int`


Returns the spacing between the lines


### `SetTight(bool value)`

**Returns:** `void`


Sets tight arrangement, not working yet


### `reorganize()`

**Returns:** ``



### `SetAlignment(Graphics::TextAlignment value)`

**Returns:** `void`


Changes the default alignment of the widgets. Alignment of a specific line can be altered by streaming Flow::Left, Center and Right.


### `GetAlignment()`

**Returns:** `Graphics::TextAlignment`


Returns the default alignment of the widgets.


### `InsertBreak()`

**Returns:** `void`


Inserts a line break after the last widget. Reordering widgets do not automatically arrange breaks. Multiple breaks will leave unit width space between the lines.


### `InsertBreak(int index)`

**Returns:** `void`


Inserts a line break before the widget at the given index. Reordering widgets do not automatically arrange breaks. Multiple breaks will leave unit width space between the lines. -1 will add a space at the front.


### `InsertBreak(const Widget &widget)`

**Returns:** `void`


Inserts a line break after the given widget. This only works if the widget is currently in the container. Reordering widgets do not automatically arrange breaks. Multiple breaks will leave unit width space between the lines.


### `RemoveAllModifiers()`

**Returns:** `void`


Removes all modifiers such as breaks in the organizer


### `Reorganize()`

**Returns:** ``



### `HSpace(const UnitDimension &size)`

**Returns:** `Modifier`


This will create a modifier object that should be inserted into ui stream


### `VSpace(const UnitDimension &dist)`

**Returns:** `Modifier`


This will create a vertical space modifier object that should be inserted into ui stream


### `Indent(const UnitDimension &dist)`

**Returns:** `Modifier`


Adds to the indent amount, use ResetIndent to set it to zero. Insert this into the UI stream to use.


### `ResetIndent()`

**Returns:** `Modifier`


Removes the indent Insert this into the UI stream to use.


### `flow(Widget &widget)`

**Returns:** `void`


Adds the given widget to the attached container. Adds the given text as a label to the attached container When supplied with std::endl, inserts a line break. Inserts a line break. Inserts a line break. Changes the alignment of the widgets if the line is not full Sets the size of the next widget in unit sizes Adds a button to the container Creates an action, which when streamed to organizer will create a button Creates an action, which when streamed to organizer will create a button Creates an action, which when streamed to organizer will create a button


### `Add(widget)`

**Returns:** ``



### `flow(const std::string &title)`

**Returns:** `void`



### `flow(Modifier modifier)`

**Returns:** `void`



### `flow(BreakTag)`

**Returns:** `void`



### `flow(const UnitDimension &size)`

**Returns:** `void`



### `flow(Graphics::TextAlignment alignment)`

**Returns:** `void`


