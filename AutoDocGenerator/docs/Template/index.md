# Template

> Auto-generated documentation for the **Template** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Template`

**Namespace:** `UI`

#### Methods

##### `Template(—)`

**Returns:** ``

This template can be freely resized Size of the template is fixed and should not be modified Size of the template should be incremented at the multiples of the size and addition size should be added to it.

##### `Template(Template &&other)`

**Returns:** ``

##### `Remove(int index)`

**Returns:** `void`

Destructor This will create a new placeholder and return it. The ownership will stay with the template. Index is the component index not the order in the template. This will create a new placeholder and return it. The ownership will stay with the template. Index is the component index not the order in the template. This will create a new textholder and return it. The ownership will stay with the template. Index is the component index not the order in the template. This will create a new ignored template. Ignored templates are used to erase templates that are set to Always This will create a new textholder and return it. The ownership will stay with the template. Index is the component index not the order in the template. This will create a new drawable and return it. The ownership will stay with the template. Index is the component index not the order in the template. This will create a new drawable and return it. The ownership will stay with the template. Index is the component index not the order in the template. This will create a new drawable and return it. The ownership will stay with the template. Index is the component index not the order in the template. This will create a new drawable and return it. The ownership will stay with the template. Index is the component index not the order in the template. This will create a new ignored template. Ignored templates are used to erase templates that are set to Always Removes the component at the given index.

##### `ChangedEvent(—)`

**Returns:** ``

##### `Assume(ComponentTemplate &component)`

**Returns:** `void`

Releases the component and its ownership Adds a previously created component to the template, the ownership of the object is transferred to the template object.

##### `GetCount(—)`

**Returns:** `int`

Returns the number of components in the template

##### `SetSizing(SizeMode x, SizeMode y)`

**Returns:** `void`

Returns the component at the given index. This index is not component index, but rather the location of the component in the template. Returns the component at the given index. This index is not component index, but rather the location of the component in the template. Changes the size mode of the template

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetXSizing(—)`

**Returns:** `SizeMode`

Returns the sizing mode

##### `GetYSizing(—)`

**Returns:** `SizeMode`

Returns the sizing mode

##### `SetSize(const UnitDimension &w, const UnitDimension &h)`

**Returns:** `void`

Changes the size of the template

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetSize(const UnitSize &value)`

**Returns:** `void`

Changes the size of the template

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetSize(—)`

**Returns:** `UnitSize`

Returns the size of the template

##### `GetSize(const Geometry::Size &parentsize)`

**Returns:** `Geometry::Size`

Returns the size of the template in Pixels

##### `GetWidth(—)`

**Returns:** `UnitDimension`

Returns the size of the template

##### `GetHeight(—)`

**Returns:** `UnitDimension`

Returns the size of the template

##### `SetAdditionalSize(int w, int h)`

**Returns:** `void`

Changes the additional size of the template. This value should only be set and used if the size mode is multiple. This value is in pixels

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetAdditionalSize(Geometry::Size value)`

**Returns:** `void`

Changes the additional size of the template. This value should only be set and used if the size mode is multiple

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetAdditionalSize(—)`

**Returns:** `Geometry::Size`

Returns the additional size. This value should only be set and used if the size mode is multiple

##### `SetConditionDuration(ComponentCondition from, ComponentCondition to, int duration)`

**Returns:** `void`

Changes the duration of a component condition. Durations on final conditions are ignored, only transition condition durations are used. Duration is in milliseconds

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetConditionDuration(ComponentCondition from, ComponentCondition to)`

**Returns:** `int`

Returns the duration of the component condition

##### `SetSpacing(int value)`

**Returns:** `void`

Sets the spacing required for this template. Organizer widgets uses this spacing in order to layout the widgets.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetSpacing(—)`

**Returns:** `int`

Returns the spacing required for this template. Organizer widgets uses this spacing in order to layout the widgets.

##### `SetUnitSize(int value)`

**Returns:** `void`

Sets the unit size for a widget. This size should be enough to have a bordered icon.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetUnitSize(—)`

**Returns:** `int`

Returns the unit width for a widget. This size is enough to have a bordered icon. Widgets should be sized according to unit width and spacing. A single unit width would be too small for most widgets. Multiple units can be calculated by following formula: W(n) = n * W(1) + (n-1) * Spacing

##### `SetResizeHandleSize(int value)`

**Returns:** `void`

Sets the size for resize handles. -1 sets it automatic which will return unit width. Default is -1.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetResizeHandleSize(—)`

**Returns:** `int`

Returns the size for resize handles. Default is unitwidth.

##### `begin(—)`

**Returns:** `auto`

for iteration

##### `end(—)`

**Returns:** `auto`

for iteration

##### `begin(—)`

**Returns:** `auto`

for iteration

##### `end(—)`

**Returns:** `auto`

for iteration

##### `SetDirection(Direction value)`

**Returns:** `void`

In some widgets there is a direction which controls where the subcomponents are placed. Direction controls this.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetDirection(—)`

**Returns:** `Direction`

In some widgets there is a direction which controls where the subcomponents are placed. Direction controls this.


### `ComponentTemplate`

**Namespace:** `UI`

This event is fired whenever template or its components are changed. This is mainly for debugging Defines an object according to the Box Model.

#### Methods

##### `SetPosition(int x, int y, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Returns the type of the component. Changes the coordinates of the component to the given position.

##### `SetPosition(Geometry::Point pos, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the coordinates of the component to the given position.

##### `SetPosition(Dimension x, Dimension y)`

**Returns:** `void`

Changes the coordinates of the component to the given position.

##### `SetPosition(Point value)`

**Returns:** `void`

Changes the coordinates of the component to the given position.

##### `SetPositioning(PositionType value)`

**Returns:** `void`

Changes the positioning method of the component.

##### `GetPosition(—)`

**Returns:** `Point`

Returns the current position of the component. This value is *not* absolute final position as it cannot be determined before the component is rendered in a widget.

##### `GetPositioning(—)`

**Returns:** `PositionType`

Returns the positioning method of the component

##### `SetCenter(int x, int y, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the center coordinate that will be used in rotation

##### `SetCenter(Geometry::Point pos, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the center coordinate that will be used in rotation

##### `SetCenter(Dimension x, Dimension y)`

**Returns:** `void`

Changes the center coordinate that will be used in rotation

##### `SetCenter(Point value)`

**Returns:** `void`

Changes the center coordinate that will be used in rotation

##### `GetCenter(—)`

**Returns:** `Point`

Returns the center point that would be used for rotation

##### `SetSize(int w, int h, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the size of the component. The given values are ignored if the sizing mode is Automatic.

##### `SetSize(Geometry::Size size, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the size of the component. The given values are ignored if the sizing mode is Automatic.

##### `SetSize(Dimension w, Dimension h)`

**Returns:** `void`

Changes the size of the component. If sizing mode is automatic, it will be set to fixed.

##### `SetSize(Size size)`

**Returns:** `void`

Changes the size of the component. If sizing mode is automatic, it will be set to fixed.

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetSizing(SizingMode value)`

**Returns:** `void`

Changes the sizing mode of the component.

##### `SetSizing(SizingMode hor, SizingMode vert)`

**Returns:** `void`

Changes the sizing mode of the component.

##### `GetSize(—)`

**Returns:** `Size`

Returns the size of the component. This value is *not* absolute final size as it cannot be determined before the component is rendered in a widget.

##### `GetHorizontalSizing(—)`

**Returns:** `SizingMode`

Returns the horizontal sizing mode of the component.

##### `GetVerticalSizing(—)`

**Returns:** `SizingMode`

Returns the horizontal sizing mode of the component.

##### `SetMargin(int value, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the margin of the component. Margin is the minimum spacing around the component. Negative margin is possible and will always be subtracted from the other component's margin.

##### `SetMargin(int hor, int ver, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the margin of the component. Margin is the minimum spacing around the component. Negative margin is possible and will always be subtracted from the other component's margin.

##### `SetMargin(int left, int top, int right, int bottom, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the margin of the component. Margin is the minimum spacing around the component. Negative margin is possible and will always be subtracted from the other component's margin.

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetMargin(Geometry::Margin value, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the margin of the component. Margin is the minimum spacing around the component. Negative margin is possible and will always be subtracted from the other component's margin.

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetMargin(Dimension value)`

**Returns:** `void`

Changes the margin of the component. Margin is the minimum spacing around the component. Negative margin is possible and will always be subtracted from the other component's margin.

##### `SetMargin(Dimension hor, Dimension ver)`

**Returns:** `void`

Changes the margin of the component. Margin is the minimum spacing around the component. Negative margin is possible and will always be subtracted from the other component's margin.

##### `SetMargin(Dimension left, Dimension top, Dimension right, Dimension bottom)`

**Returns:** `void`

Changes the margin of the component. Margin is the minimum spacing around the component. Negative margin is possible and will always be subtracted from the other component's margin.

##### `SetMargin(Margin value)`

**Returns:** `void`

Changes the margin of the component. Margin is the minimum spacing around the component. Negative margin is possible and will always be subtracted from the other component's margin.

##### `GetMargin(—)`

**Returns:** `Margin`

Returns the margin.

##### `SetIndent(int value, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the indent of the component. Indent is added to the margin if the component is at the edge of the container.

##### `SetIndent(int hor, int ver, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the indent of the component. Indent is added to the margin if the component is at the edge of the container.

##### `SetIndent(int left, int top, int right, int bottom, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the indent of the component. Indent is added to the margin if the component is at the edge of the container.

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetIndent(Geometry::Margin value, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the indent of the component. Indent is added to the margin if the component is at the edge of the container.

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetIndent(Dimension value)`

**Returns:** `void`

Changes the indent of the component. Indent is added to the margin if the component is at the edge of the container.

##### `SetIndent(Dimension hor, Dimension ver)`

**Returns:** `void`

Changes the indent of the component. Indent is added to the margin if the component is at the edge of the container.

##### `SetIndent(Dimension left, Dimension top, Dimension right, Dimension bottom)`

**Returns:** `void`

Changes the indent of the component. Indent is added to the margin if the component is at the edge of the container.

##### `SetIndent(Margin value)`

**Returns:** `void`

Changes the indent of the component. Indent is added to the margin if the component is at the edge of the container.

##### `GetIndent(—)`

**Returns:** `Margin`

Returns the current indent.

##### `SetDataEffect(DataEffect effect)`

**Returns:** `void`

Sets the data effect for this component. Default is None.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetDataEffect(—)`

**Returns:** `DataEffect`

Returns how the data will affect this component

##### `SetValueOrdering(int first, int second, int third, int fourth)`

**Returns:** `void`

Changes the ordering of the values. This allows swaps like X-Y. You should specify which channel will receive which value.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetValueOrdering(—)`

**Returns:** `std::array<int, 4>`

Returns the ordering of value channels.

##### `SetValueModification(ValueModification mod, ValueSource source = UseFirst, std::array<float, 4> min = {{0, 0, 0, 0}}, std::array<float, 4> max = {{1, 1, 1, 1}})`

**Returns:** `void`

Sets the property that will be affected by the value of the widget. Default is NoModification. If min and max is specified incoming value will be scaled accordingly.

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetValueRange(std::array<float, 4> min, std::array<float, 4> max)`

**Returns:** `void`

Changes the data range, which scales the data effect on the component. Not all effects are affected by the range.

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetValueRange(int channel, float min, float max)`

**Returns:** `void`

Changes the data range, which scales the data effect on the component. Not all effects are affected by the range.

##### `ASSERT(channel>=0 && channel<4, "Channel index out of bounds")`

**Returns:** ``

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetValueModification(—)`

**Returns:** `ValueModification`

Returns which property of this component will be modified by the value

##### `SetValueSource(ValueSource value)`

**Returns:** `void`

Returns the value source that will be used

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetValueSource(—)`

**Returns:** `ValueSource`

Returns the value source that will be used

##### `SetTag(Tag value)`

**Returns:** `void`

Changes the tag of this component

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetTag(—)`

**Returns:** `Tag`

Returns the tag of the component

##### `SetRepeatMode(RepeatMode value)`

**Returns:** `void`

Changes the repeat mode of this component. If the consumer of the component does not know about this repeat mode, this component will be ignored

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetRepeatMode(—)`

**Returns:** `RepeatMode`

Returns the repeat mode of this component.

##### `GetValueMin(—)`

**Returns:** `std::array<float, 4>`

Returns the value scale minimum.

##### `GetValueRange(—)`

**Returns:** `std::array<float, 4>`

Returns the range of the value scale.

##### `GetValueMax(—)`

**Returns:** `std::array<float, 4>`

Returns the value scale maximum.

##### `GetValueMin(int channel)`

**Returns:** `float`

Returns the value scale minimum.

##### `ASSERT(channel>=0 && channel<4, "Channel index out of bounds")`

**Returns:** ``

##### `GetValueRange(int channel)`

**Returns:** `float`

Returns the range of the value scale.

##### `ASSERT(channel>=0 && channel<4, "Channel index out of bounds")`

**Returns:** ``

##### `GetValueMax(int channel)`

**Returns:** `float`

Returns the value scale maximum.

##### `ASSERT(channel>=0 && channel<4, "Channel index out of bounds")`

**Returns:** ``

##### `SetAnchor(Anchor previous, Anchor container, Anchor my)`

**Returns:** `void`

Changes the anchor of the component to the given values.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetPreviousAnchor(—)`

**Returns:** `Anchor`

Returns the anchor point of the previous component that this component will attach to. This value will be used if this component attaches to another of its siblings.

##### `GetContainerAnchor(—)`

**Returns:** `Anchor`

Returns the anchor point of the container that this component will attach to. This value will be used if this component attaches to its container.

##### `GetMyAnchor(—)`

**Returns:** `Anchor`

Returns the anchor point of this component.

##### `SetBaseline(int value)`

**Returns:** `void`

Changes the baseline of the current component. If set to 0, it will be determined automatically.

##### `GetBaseline(—)`

**Returns:** `int`

Returns the baseline. If set to 0, it will be detected automatically

##### `SetIndex(int value)`

**Returns:** `void`

Changes the index of the current component. Only one component can be rendered at an index which is determined by the component condition. See component indexing for more information.

##### `GetIndex(—)`

**Returns:** `int`

Returns the component index.

##### `SetCondition(ComponentCondition value)`

**Returns:** `void`

Sets the condition when this component will be visible. The visibility also depens on whether there are other visible components at the same component index. If that is the case, most specific condition will be rendered.

##### `SetCondition(ComponentCondition from, ComponentCondition to)`

**Returns:** `void`

Sets the condition when this component will be visible. This variant will create a transition condition.

##### `GetCondition(—)`

**Returns:** `ComponentCondition`

Returns the current component condition

##### `GetTargetCondition(—)`

**Returns:** `ComponentCondition`

Returns the target component condition

##### `IsTransition(—)`

**Returns:** `bool`

Returns whether this component is a transition component

##### `SetReversible(bool value)`

**Returns:** `void`

Sets whether the component transition can be reversed. Can be used to simplify from - to - from animations.

##### `IsReversible(—)`

**Returns:** `bool`

Returns whether this component transition can be reversed.

##### `SetClip(bool value)`

**Returns:** `void`

Whether to clip the contents of this container, default value is false. Due to shadows, it is advicable not to set clipping on the outer most container. Activating clipping creates a new layer for the component, requiring additional memory. If clipping is on, a component cannot be drawn more than once in different containers.

##### `GetClip(—)`

**Returns:** `bool`

Returns whether currently clipping the contents


### `PlaceholderTemplate`

**Namespace:** `UI`

This event will be fired whenever any property is changed. Can be used to update widget automatically. If set to true, will clip the contents of the component to the bounds. Condition when this component will be visible Condition when this component will be visible, setting condition_to will create a transition component. The effect that the data will have on this component The property of the component that will be affected by the value The value that will be used for this component Changes the ordering of the value source If required, can be used to scale incoming data Tag identifies a component for various modifications depending on the widget. Whether the component will be repeated along an axis. If an item will  Positioning mode Position of the component Sizing mode Size of the object. Margin around the object, will be collapsed with other object margins and padding Indent is added to the margin and padding on the edge of the container Center point for rotation Anchor point of the previous component that this component will be attached to. If the component positioning is absolute or this is the first component, it will be anchored to the container and parent anchor point will be used. Anchor point of the container that this component will be attached to, if it is attaching to its parent. Anchor point of the current component. This point will be matched to the previous component's anchor point Manually set baseline for this component. When 0, it will not be effective. Component index. Only one component can exist for a specific index position. The ordering and visibility of the components will be determined from the condition. Components will be laid out according to this index. Z-ordering is performed using the order of components in container. Defines a placeholder according to the Box Model. Placeholder is replaced with a visual component. Default sizing mode for a placeholder is Automatic.

#### Methods

##### `PlaceholderTemplate(—)`

**Returns:** ``

##### `SetTemplate(const Template &value)`

**Returns:** `void`

Returns the type of the component. Sets the sub template for this placeholder.

##### `ChangedEvent(—)`

**Returns:** ``

##### `OwnTemplate(const Template &value)`

**Returns:** `void`

Sets the sub template for this placeholder.

##### `ChangedEvent(—)`

**Returns:** ``

##### `HasTemplate(—)`

**Returns:** `bool`

Returns if this placeholder has a sub template

##### `ASSERT(temp, "Template is empty.")`

**Returns:** ``

Returns the sub template of this placeholder. If the template does not exists, assertation violation will be fired, thus it is advisable to check if the template exists using HasTemplate function.


### `IgnoredTemplate`

**Namespace:** `UI`

This component type will be ignored by ComponentStack, effectively erasing Always when necessary.


### `TextholderTemplate`

**Namespace:** `UI`

Returns the type of the component.

#### Methods

##### `TextholderTemplate(—)`

**Returns:** ``

##### `SetSizing(Automatic)`

**Returns:** ``

##### `IsReady(—)`

**Returns:** `bool`

Returns the type of the component. Returns if this text holder can perform rendering

##### `SetRenderer(const Graphics::TextPrinter &value)`

**Returns:** `void`

Changes the renderer

##### `ASSERT(renderer, "Renderer is not set.")`

**Returns:** ``

Returns the renderer for this textholder

##### `SetColor(Graphics::RGBAf value)`

**Returns:** `void`

Changes the color that will override default color of the text drawn.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetColor(—)`

**Returns:** `Graphics::RGBAf`

Returns current color.

##### `SetTargetColor(Graphics::RGBAf value)`

**Returns:** `void`

Sets the target color for BlendColor value modification.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetTargetColor(—)`

**Returns:** `Graphics::RGBAf`

Returns the target color that will be used for BlendColor value modification.

##### `SetText(const std::string &value)`

**Returns:** `void`

Sets the default text for the textholder. This text can be overriden by DataEffect

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetText(—)`

**Returns:** `std::string`

Returns the default text for the textholder.


### `VisualProvider`

**Namespace:** `UI`

#### Methods

##### `HasContent(—)`

**Returns:** `bool`

If this drawable has any content

##### `IsAnimation(—)`

**Returns:** `bool`

Of this drawable template has animation content

##### `IsDrawable(—)`

**Returns:** `bool`

Of this drawable template has drawable content

##### `if(provider == nullptr)`

**Returns:** ``

Returns the content as animation provider

##### `if(drawable == nullptr)`

**Returns:** ``

Returns the content as a drawable

##### `if(provider)`

**Returns:** `else`

##### `SetDrawable(const Graphics::Drawable &value)`

**Returns:** `void`

Sets the content from a drawable

##### `SetAnimation(const Graphics::AnimationProvider &value)`

**Returns:** `void`

Sets the content from an animation provider


### `GraphicsTemplate`

**Namespace:** `UI`

Defines a visual component. RelativeToContents sizing mode is selected if no drawable is supplied, the relative size will be taken as 0x0. If the drawable has no size information, object will be treated as RelativeToContainer and size will be taken as 100%. This component can either work with animation providers, which are meant to be instantiated or drawable which will directly be used.

#### Methods

##### `GraphicsTemplate(—)`

**Returns:** ``

Default constructor.

##### `SetFillArea(bool value)`

**Returns:** `void`

Filling constructor, might cause ambiguous call due to most drawables being AnimationProviders as well. You might typecast or use Content.SetDrawable function Filling constructor, might cause ambiguous call due to most drawables being AnimationProviders as well. You might typecast or use Content.SetDrawable function Returns the type of the component. TODO: add size controller Set to true if you want to fill the region with the given graphics. This will only work if the given animation/drawable is rectangular

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetFillArea(—)`

**Returns:** `bool`

Returns whether this graphics will fill the component area

##### `SetColor(Graphics::RGBAf value)`

**Returns:** `void`

Changes the color that will set tint of the drawn graphics.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetColor(—)`

**Returns:** `Graphics::RGBAf`

Returns current tint color.

##### `SetTargetColor(Graphics::RGBAf value)`

**Returns:** `void`

Sets the target tint color for BlendColor value modification.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetTargetColor(—)`

**Returns:** `Graphics::RGBAf`

Returns the target tint color that will be used for BlendColor value modification.


### `ContainerTemplate`

**Namespace:** `UI`

Graphical representation of the template Container class that defines an area according to the Box Model. It can contain other objects.

#### Methods

##### `SetPadding(int value, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the padding of the component. Padding is the minimum spacing inside the component.

##### `SetPadding(int hor, int ver, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the padding of the component. Padding is the minimum spacing inside the component.

##### `SetPadding(int left, int top, int right, int bottom, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the padding of the component. Padding is the minimum spacing inside the component.

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetPadding(Geometry::Margin value, Dimension::Unit unit = Dimension::Pixel)`

**Returns:** `void`

Changes the padding of the component. Padding is the minimum spacing inside the component.

##### `ChangedEvent(—)`

**Returns:** ``

##### `SetPadding(Dimension value)`

**Returns:** `void`

Changes the padding of the component. Padding is the minimum spacing inside the component.

##### `SetPadding(Dimension hor, Dimension ver)`

**Returns:** `void`

Changes the padding of the component. Padding is the minimum spacing inside the component.

##### `SetPadding(Dimension left, Dimension top, Dimension right, Dimension bottom)`

**Returns:** `void`

Changes the padding of the component. Padding is the minimum spacing inside the component.

##### `SetPadding(Margin value)`

**Returns:** `void`

Changes the padding of the component. Padding is the minimum spacing inside the component.

##### `GetPadding(—)`

**Returns:** `Margin`

Returns the padding.

##### `SetBorderSize(int value)`

**Returns:** `void`

Changes the border size of the component. Border size stays within the object area, but excluded from the interior area.

##### `SetBorderSize(int hor, int ver)`

**Returns:** `void`

Changes the border size of the component. Border size stays within the object area, but excluded from the interior area.

##### `SetBorderSize(int left, int top, int right, int bottom)`

**Returns:** `void`

Changes the border size of the component. Border size stays within the object area, but excluded from the interior area.

##### `SetBorderSize(Geometry::Margin value)`

**Returns:** `void`

Changes the border size of the component. Border size stays within the object area, but excluded from the interior area.

##### `GetBorderSize(—)`

**Returns:** `Geometry::Margin`

Returns the border size

##### `SetShadowExtent(int value)`

**Returns:** `void`

Changes the shadow extent of the component. Shadow extent stays within the object area, but excluded from the interior area.

##### `SetShadowExtent(int hor, int ver)`

**Returns:** `void`

Changes the shadow extent of the component. Shadow extent stays within the object area, but excluded from the interior area.

##### `SetShadowExtent(int left, int top, int right, int bottom)`

**Returns:** `void`

Changes the shadow extent of the component. Shadow extent stays within the object area, but excluded from the interior area.

##### `SetShadowExtent(Geometry::Margin value)`

**Returns:** `void`

Changes the shadow extent of the component. Shadow extent stays within the object area, but excluded from the interior area.

##### `GetShadowExtent(—)`

**Returns:** `Geometry::Margin`

Returns the shadow extent

##### `SetOverlayExtent(int value)`

**Returns:** `void`

Changes the overlay extent of the component. Overlay extent stays within the object area, but excluded from the interior area.

##### `SetOverlayExtent(int hor, int ver)`

**Returns:** `void`

Changes the overlay extent of the component. Overlay extent stays within the object area, but excluded from the interior area.

##### `SetOverlayExtent(int left, int top, int right, int bottom)`

**Returns:** `void`

Changes the overlay extent of the component. Overlay extent stays within the object area, but excluded from the interior area.

##### `SetOverlayExtent(Geometry::Margin value)`

**Returns:** `void`

Changes the overlay extent of the component. Overlay extent stays within the object area, but excluded from the interior area.

##### `GetOverlayExtent(—)`

**Returns:** `Geometry::Margin`

Returns the overlay extent

##### `SetOrientation(Graphics::Orientation value)`

**Returns:** `void`

Changes the orientation of the template

##### `GetOrientation(—)`

**Returns:** `Graphics::Orientation`

Returns the current orientation of the container

##### `ChangedEvent(—)`

**Returns:** ``

Adds an index to the container. The components will be drawn in order. Thus the components that are added later will be drawn on top. Multiple indexes will not cause any crashes, however, same component might be drawn multiple times on top of itself.

##### `InsertIndex(int before, int componentindex)`

**Returns:** `void`

Insert an index to the specified location in the container. The components will be drawn in order. Thus the components that are added later will be drawn on top. Multiple indexes will not cause any crashes, however, same component might be drawn multiple times on top of itself.

##### `ChangedEvent(—)`

**Returns:** ``

##### `RemoveIndexAt(int index)`

**Returns:** `void`

Removes the index at the given position.

##### `ChangedEvent(—)`

**Returns:** ``

##### `GetCount(—)`

**Returns:** `int`

Returns the number of component indices stored in this container

##### `SetReportMouse(bool value)`

**Returns:** `void`

Returns the component index at the given location Returns the component index at the given location Returns the type of the component. Mouse reporting allows component stack to report mouse events over this container to be reported separately. Setting a tag with this property will help distinguishing between multiple regions.

##### `GetReportMouse(—)`

**Returns:** `bool`


---

## Enums

### `SizeMode`

**Namespace:** `UI`

Size mode of the template, will be applied separately to X and Y dimensions


### `PositionType`

**Namespace:** `UI`

Destructor Controls where the component will be placed.


### `SizingMode`

**Namespace:** `UI`

Component will be placed relative to the previous component Absolute positioning, coordinates will start from the container, percent based movement will move to stay within the container. If the component is filling the container, it cannot be moved. Absolute positioning, coordinates will start from the container. Percent based movement is relative to the size of the component. The given coordinates are polar coordinates, The radius is given in pixels and angle is specified in degrees. Parent's center point is used as pole. X component is used as radius and Y component is used as angle. Controls how the size is affected from the contents of the object


### `DataEffect`

**Namespace:** `UI`

The given size is absolute, it is not affected by the contents Given size is not used, object is sized to its contents Given size is the minimum, if the contents are bigger, the object be resized to fit Given size is the maximum, if the contents are smaller, the object be resized Which property will the data of the widget affect.


### `ValueModification`

**Namespace:** `UI`

Nothing will be affected Works only for TextholderTemplate, data will affect the text that is displayed. Data will effect the displayed graphics Which property will the value of the widget affect. It will be scaled between valuemin and valuemax.


### `ValueSource`

**Namespace:** `UI`

Nothing will be modified Position of this component will be affected by the data. Data will be given as a percent and will modify Position property. Useful for sliders, scrollbars and progress bars. The direction of the container is used to determine which axis will get affected if only one channel is used. Modifies the X coordinate of the component regardless of the container direction. Modifies the Y coordinate of the component regardless of the container direction. Value modifies the opacity of the component. If used on a container, it will effect all components in that container Value modifies the color of the component. If used on a container, it will tint all components in that container In text and graphics templates, this setting will blend the color to target color. If there is only one value source, all channels will be blended using the given factor. Two value sources will have separate blending factor RGB and A. Three sources will cause R, G, and B to have separate blender factors. A of the original color will be used. Four channels will have four separate blending factors. Data affects the rotation of the component. Rotation angle will start from 0 degrees for 0, 360 degrees for 1. You may use min and max to modify this. For instance, if max is set to 0.5, the degrees will go up to 180. For now, this effect is not in use. Data will affect the progress of the animation. Will only work for Objects with animations. Size of this component will be affected. Data will be given as a percent and will modify Size property. Useful for sliders and progress bars. The direction of the container is used to determine which axis will get affected. Width of this component will be affected. Data will be given as a percent and will modify Size property. Useful for sliders and progress bars. The direction of the container is used to determine which axis will get affected. Height of this component will be affected. Data will be given as a percent and will modify Size property. Useful for sliders and progress bars. The direction of the container is used to determine which axis will get affected. This is a combined modification of position and size. Single channel will control the position along the orientation. Two channels will control position and size along the orientation. Three channels will control xy position and size along the orientation. Finally four channels will control every aspect of the component. Modifies X position and width Modifies X position and height Modifies Y position and width Modifies Y position and height Which data channels should be used as the value, common combinations are listed, however, all combinations are valid except when they are used for mouse mapping. Only the values listed here that use two channels will work fully with mouse mapping. LCh is for circular La*b* color system. Color can also be mapped to coordinate system. Particularly, CH can be mapped to polar coordinates to create a color map. LCh color system is not yet working


### `Tag`

**Namespace:** `UI`

Red or radius for polar coordinates Theta for polar coordinates Grayscale value of color Lightness Hue Chromacity This channel will give the progress of a transition. It will be set to 1 for non-transitional components. Use this channel alone, do not combine it with others. Maximum power of two Tags mark a component to be modified in a way meaningful to specific widgets. Components can be queried for their size and positions from the component stack using their tag.


### `RepeatMode`

**Namespace:** `UI`

Do not use this tag for regular components, it is used to identify substacks without a tag Some components are repeated along some axis, this property controls how they will be repeated. Use X direction if there is no direction. Y is the angular direction on polar systems. Repeated components will have their values set to the values specified by their position.


---

## Functions

### `for(auto &c : components)`

**Returns:** ``



### `for(auto &c : components)`

**Returns:** ``



### `ChangedEvent()`

**Returns:** ``



### `ChangedEvent()`

**Returns:** ``



### `ChangedEvent()`

**Returns:** ``



### `ChangedEvent()`

**Returns:** ``



### `ChangedEvent()`

**Returns:** ``



### `ChangedEvent()`

**Returns:** ``



### `ChangedEvent()`

**Returns:** ``



### `IsLeft(Anchor a)`

**Returns:** `inline bool`


Anchor position This anchor position should is only used to denote object will not be anchored to a previous object, only to its parent. If used as parent anchor it will be ignored and default anchor will be used instead. This should be paired with absolute positioning. Top left Top center Top right Middle left Middle center, using this position ensures that the components will be inside each other. Middle right Bottom left Bottom center Bottom right Baseline left, for text, this aligns to the baseline of the first line Baseline right, for text, this aligns to the baseline of the first line Baseline left, for text, this aligns to the baseline of the last line. This mode only works properly if Sizing is set to automatic. Baseline right, for text, this aligns to the baseline of the last line. This mode only works properly if Sizing is set to automatic. Returns if an anchor is on the left


### `switch(a)`

**Returns:** ``



### `IsRight(Anchor a)`

**Returns:** `inline bool`


Returns if an anchor is on the right


### `switch(a)`

**Returns:** ``



### `IsCenter(Anchor a)`

**Returns:** `inline bool`


Returns if an anchor is centered horizontally


### `switch(a)`

**Returns:** ``



### `IsTop(Anchor a)`

**Returns:** `inline bool`


Returns if the given anchor is at top


### `switch(a)`

**Returns:** ``



### `IsBottom(Anchor a)`

**Returns:** `inline bool`


Returns if the given anchor is at bottom


### `switch(a)`

**Returns:** ``



### `IsMiddle(Anchor a)`

**Returns:** `inline bool`


Returns if the given anchor is at middle vertically


### `switch(a)`

**Returns:** ``



### `IsMouseRelated(ComponentCondition condition)`

**Returns:** `inline bool`


Types of components, see respective classes for details. Controls the condition when the components are visible. Components with the same ID will replace a previous one. If there is a condition that is satisfied, the component at the specific index will be replaced with that one, otherwise, if a component with condition always exists, it will be used. Component is always active Component is always disabled Component is visible when the widget is disabled. Component is visible when the widget is readonly. Widget has the focus Mouse is over the widget, or over a particular repeat This is activated when the mouse is pressed on the component stack. However, it can be activated in cases when activation key is pressed. Second state of the widget, first state is Always Third state of the widget, first state is Always Fourth state of the widget, first state is Always This condition is triggered when the widget is opened like a combobox showing its list part. For widgets which are "opened" by default like window, this condition will never be satisfied. Instead of this condition, use Always for the base state. This condition is triggered when the widget is closed like a tree view item that is folded, or a window that is rolled. For widgets which are "closed" by default, like combobox, this condition will never be satisfied. Instead of this condition, use Always for the base state. For widgets that can have reversed state. When dropdown will open above, this will be set. In lists denotes the item is in odd position In lists denotes the item is in even position In a list this denotes the item is at the first place In a list this denotes the item is somewhere in the middle In a list this denotes the item is at the last place In a list this denotes the item alone This is for widgets that can be activated, like a count down timer There is space horizontally to be scrolled There is space vertically to be scrolled. There is space both horizontally and vertically to be scrolled. Channel 1 value is 0, the value will be rounded to 4 decimal points before comparison Channel 1 value is 0.5, the value will be rounded to 4 decimal points before comparison Channel 1 value is 1, the value will be rounded to 4 decimal points before comparison Channel 2 value is 0, the value will be rounded to 4 decimal points before comparison Channel 2 value is 0.5, the value will be rounded to 4 decimal points before comparison Channel 2 value is 1, the value will be rounded to 4 decimal points before comparison Channel 3 value is 0, the value will be rounded to 4 decimal points before comparison Channel 3 value is 0.5, the value will be rounded to 4 decimal points before comparison Channel 3 value is 1, the value will be rounded to 4 decimal points before comparison Channel 4 value is 0, the value will be rounded to 4 decimal points before comparison Channel 4 value is 0.5, the value will be rounded to 4 decimal points before comparison Channel 4 value is 1, the value will be rounded to 4 decimal points before comparison This widget is the default widget of its container This widget is the cancel widget of its container This widget is hidden Do not use this value Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Data effect of the component is set Do not use this condition, this is to size the arrays. Returns if the given condition is related to mouse events


### `switch(condition)`

**Returns:** ``


