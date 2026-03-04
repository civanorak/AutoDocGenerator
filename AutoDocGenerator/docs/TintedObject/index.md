# TintedObject

> Auto-generated documentation for the **TintedObject** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `ITintedObjectProvider`

**Namespace:** `Gorgon`

For ease of use in resource system

#### Methods

##### `virtual` `GetColor(—)`

**Returns:** `virtual RGBAf`

##### `virtual` `SetColor(const RGBAf &value)`

**Returns:** `virtual void`


### `basic_TintedObject`

**Namespace:** `Gorgon`

#### Methods

##### `basic_TintedObject(const basic_TintedObjectProvider<A_> &parent, bool create = true)`

**Returns:** ``

##### `basic_TintedObject(const basic_TintedObjectProvider<A_> &parent, Gorgon::Animation::ControllerBase &timer)`

**Returns:** ``

##### `SetColor(RGBAf value)`

**Returns:** `void`

Creates a scalable object from two animations, these animations should not have controllers attached to them. Any attached controllers will be replaced or removed. A non-const version cannot work as this object needs to control the controllers of these animations. Creates a scalable object from two animations, these animations should not have controllers attached to them Any attached controllers will be replaced or removed. A non-const version cannot work as this object needs to control the controllers of these animations. Changes the size controller used in this scalable object

##### `GetColor(—)`

**Returns:** `RGBAf`

Returns the size controller used in this scalable object


### `basic_TintedObjectProvider`

**Namespace:** `Gorgon`

#### Methods

##### `if(own)`

**Returns:** ``

Empty constructor Filling constructor

##### `if(base)`

**Returns:** ``

Creates a base animation without controller.

##### `SetBase(A_ *value)`

**Returns:** `void`

Returns the base component. Could return nullptr Returns the tint color Sets the tint color of the object Sets the base provider, ownership semantics will not be changed

##### `OwnProvider(—)`

**Returns:** `void`

Assumes the ownership of the providers

##### `Prepare(—)`

**Returns:** `void`

Prepares the providers. Provider type should support this operation, otherwise this function will cause a compile time error.


### `TintedObject`

**Namespace:** `Resource`

#### Methods

##### `TintedObject(Graphics::TintedBitmapProvider &prov)`

**Returns:** `explicit`

Creates a new tinted object using another tinted object provider.

##### `TintedObject(Graphics::TintedBitmapAnimationProvider &prov)`

**Returns:** `explicit`

Creates a new tinted object using another tinted object provider.

##### `TintedObject(Graphics::TintedObjectProvider &prov)`

**Returns:** `explicit`

Creates a new tinted object using another tinted object provider.

##### `TintedObject(—)`

**Returns:** ``

Creates a new tinted object using another tinted object provider. Creates a new tinted object using another tinted object provider. Creates a new tinted object using another tinted object provider. Creates a new empty tinted object

##### `SetProvider(Graphics::TintedBitmapProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::TintedBitmapAnimationProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::TintedObjectProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::TintedBitmapProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::TintedBitmapAnimationProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::TintedObjectProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `RemoveProvider(—)`

**Returns:** `void`

Removes the provider, if it is own by this resource it will be deleted.

##### `static` `SaveThis(Writer &writer, const Graphics::ITintedObjectProvider &provider)`

**Returns:** `static void`

This function loads a tinted object resource from the file


---

## Functions

### `while(!target)`

**Returns:** ``



### `if(gid == GID::TintedObject_Props)`

**Returns:** ``



### `if(resource)`

**Returns:** ``



### `if(++c > 1)`

**Returns:** ``



### `if(type == anim)`

**Returns:** ``



### `if(type == img)`

**Returns:** `else`



### `if(type == mixed)`

**Returns:** `else`



### `savethis(Writer &writer, const Graphics::basic_TintedObjectProvider<T_> &provider)`

**Returns:** `static void`



### `if(b)`

**Returns:** ``



### `SaveAnimation(writer, b)`

**Returns:** ``



### `if(prov != nullptr)`

**Returns:** `else`



### `setthis(F_, Graphics::basic_TintedObjectProvider<T_> *, T_ *)`

**Returns:** `static void`



### `setthis(F_ f, Graphics::TintedBitmapProvider *provider, Graphics::Bitmap *o)`

**Returns:** `static void`



### `CallBitmapAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::TintedBitmapAnimationProvider *provider, Graphics::BitmapAnimationProvider *o)`

**Returns:** `static void`



### `CallBitmapAnimationAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::TintedObjectProvider *provider, Graphics::RectangularAnimationProvider *o)`

**Returns:** `static void`



### `CallGenericAnimationSetter(f, provider, o)`

**Returns:** ``



### `moveout(Graphics::basic_TintedObjectProvider<T_> *provider, Graphics::ITintedObjectProvider *&p)`

**Returns:** `static void`



### `setthis(&Graphics::basic_TintedObjectProvider<T_>::SetBase, bp, b)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `for(auto &child : children)`

**Returns:** ``


