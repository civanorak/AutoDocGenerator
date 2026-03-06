# StackedObject

&gt; Auto-generated documentation for the **StackedObject** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `IStackedObjectProvider`

**Namespace:** `Gorgon`

For ease of use in resource system

#### Methods

##### `virtual` `GetOffset(—)`

**Returns:** `virtual Geometry::Point`

##### `virtual` `SetOffset(const Geometry::Point&)`

**Returns:** `virtual void`


### `basic_StackedObject`

**Namespace:** `Gorgon`

#### Methods

##### `basic_StackedObject(const basic_StackedObjectProvider<A_> &parent, bool create = true)`

**Returns:** ``

##### `basic_StackedObject(const basic_StackedObjectProvider<A_> &parent, Gorgon::Animation::ControllerBase &timer)`

**Returns:** ``


### `basic_StackedObjectProvider`

**Namespace:** `Gorgon`

Creates a stacked object from two animations, these animations should not have controllers attached to them. Any attached controllers will be replaced or removed. A non-const version cannot work as this object needs to control the controllers of these animations. Creates a bottomed object from two animations, these animations should not have controllers attached to them Any attached controllers will be replaced or removed. A non-const version cannot work as this object needs to control the controllers of these animations.

#### Methods

##### `if(own)`

**Returns:** ``

Empty constructor Filling constructor Filling constructor, nullptr is allowed but not recommended Filling constructor Filling constructor, nullptr is allowed but not recommended

##### `if(own)`

**Returns:** ``

##### `if(top)`

**Returns:** ``

Creates a top animation without controller.

##### `if(bottom)`

**Returns:** ``

Creates a bottom animation without controller.

##### `SetTop(A_ *value)`

**Returns:** `void`

Returns the top component. Could return nullptr Returns the bottom component. Could return nullptr Sets the top provider, ownership semantics will not be changed

##### `SetBottom(A_ *value)`

**Returns:** `void`

Sets the bottom provider, ownership semantics will not be changed

##### `SetProviders(A_ &top, A_ &bottom)`

**Returns:** `void`

Returns the offset of the top image Sets the offset of the top image Sets the providers in this object

##### `if(own)`

**Returns:** ``

##### `OwnProviders(—)`

**Returns:** `void`

Assumes the ownership of the providers

##### `Prepare(—)`

**Returns:** `void`

Prepares the providers. Provider type should support this operation, otherwise this function will cause a compile time error.


### `StackedObject`

**Namespace:** `Gorgon`

#### Methods

##### `StackedObject(Graphics::StackedBitmapProvider &prov)`

**Returns:** `explicit`

Creates a new stacked object using another stacked object provider.

##### `StackedObject(Graphics::StackedBitmapAnimationProvider &prov)`

**Returns:** `explicit`

Creates a new stacked object using another stacked object provider.

##### `StackedObject(Graphics::StackedObjectProvider &prov)`

**Returns:** `explicit`

Creates a new stacked object using another stacked object provider.

##### `StackedObject(—)`

**Returns:** ``

Creates a new stacked object using another stacked object provider. Creates a new stacked object using another stacked object provider. Creates a new stacked object using another stacked object provider. Creates a new empty stacked object

##### `SetProvider(Graphics::StackedBitmapProvider &value)`

**Returns:** `void`

Changes the provider stored in this stacked object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::StackedBitmapAnimationProvider &value)`

**Returns:** `void`

Changes the provider stored in this stacked object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::StackedObjectProvider &value)`

**Returns:** `void`

Changes the provider stored in this stacked object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::StackedBitmapProvider &value)`

**Returns:** `void`

Changes the provider stored in this stacked object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::StackedBitmapAnimationProvider &value)`

**Returns:** `void`

Changes the provider stored in this stacked object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::StackedObjectProvider &value)`

**Returns:** `void`

Changes the provider stored in this stacked object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `RemoveProvider(—)`

**Returns:** `void`

Removes the provider, if it is own by this resource it will be deleted.

##### `static` `SaveThis(Writer &writer, const Graphics::IStackedObjectProvider &provider)`

**Returns:** `static void`

This function loads a stacked object resource from the file


---

## Functions

### `while(!target)`

**Returns:** ``



### `if(gid == GID::StackedObject_Props)`

**Returns:** ``



### `if(resource)`

**Returns:** ``



### `if(++c > 2)`

**Returns:** ``



### `if(type == anim)`

**Returns:** ``



### `if(type == img)`

**Returns:** `else`



### `if(type == mixed)`

**Returns:** `else`



### `savethis(Writer &writer, const Graphics::basic_StackedObjectProvider<T_> &provider)`

**Returns:** `static void`



### `if(!t)`

**Returns:** ``



### `SaveAnimation(writer, t)`

**Returns:** ``



### `SaveAnimation(writer, t)`

**Returns:** ``



### `SaveAnimation(writer, b)`

**Returns:** ``



### `if(prov != nullptr)`

**Returns:** `else`



### `setthis(F_ f, Graphics::basic_StackedObjectProvider<T_> *provider, T_ *o)`

**Returns:** `static void`



### `setthis(F_ f, Graphics::StackedBitmapProvider *provider, Graphics::Bitmap *o)`

**Returns:** `static void`



### `CallBitmapAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::StackedBitmapAnimationProvider *provider, Graphics::BitmapAnimationProvider *o)`

**Returns:** `static void`



### `CallBitmapAnimationAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::StackedObjectProvider *provider, Graphics::RectangularAnimationProvider *o)`

**Returns:** `static void`



### `CallGenericAnimationSetter(f, provider, o)`

**Returns:** ``



### `moveout(Graphics::basic_StackedObjectProvider<T_> *provider, Graphics::IStackedObjectProvider *&p)`

**Returns:** `static void`



### `setthis(&Graphics::basic_StackedObjectProvider<T_>::SetTop, bp, t)`

**Returns:** ``



### `setthis(&Graphics::basic_StackedObjectProvider<T_>::SetBottom, bp, b)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `for(auto &child : children)`

**Returns:** ``


