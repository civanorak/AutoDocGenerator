# ScalableObject

> Auto-generated documentation for the **ScalableObject** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `IScalableObjectProvider`

**Namespace:** `Gorgon`

For ease of use in resource system

#### Methods

##### `virtual` `GetController(—)`

**Returns:** `virtual SizeController`

##### `virtual` `SetController(const SizeController &value)`

**Returns:** `virtual void`


### `basic_ScalableObject`

**Namespace:** `Gorgon`

#### Methods

##### `basic_ScalableObject(const basic_ScalableObjectProvider<A_> &parent, bool create = true)`

**Returns:** ``

##### `basic_ScalableObject(const basic_ScalableObjectProvider<A_> &parent, Gorgon::Animation::ControllerBase &timer)`

**Returns:** ``

##### `SetSizeController(SizeController value)`

**Returns:** `void`

Creates a scalable object from two animations, these animations should not have controllers attached to them. Any attached controllers will be replaced or removed. A non-const version cannot work as this object needs to control the controllers of these animations. Creates a scalable object from two animations, these animations should not have controllers attached to them Any attached controllers will be replaced or removed. A non-const version cannot work as this object needs to control the controllers of these animations. Changes the size controller used in this scalable object

##### `GetSizeController(—)`

**Returns:** `SizeController`

Returns the size controller used in this scalable object


### `basic_ScalableObjectProvider`

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

Returns the base component. Could return nullptr Returns the size controller Sets the controller Sets the base provider, ownership semantics will not be changed

##### `OwnProvider(—)`

**Returns:** `void`

Assumes the ownership of the providers

##### `Prepare(—)`

**Returns:** `void`

Prepares the providers. Provider type should support this operation, otherwise this function will cause a compile time error.


### `ScalableObject`

**Namespace:** `Resource`

#### Methods

##### `ScalableObject(Graphics::ScalableBitmapProvider &prov)`

**Returns:** `explicit`

Creates a new tinted object using another tinted object provider.

##### `ScalableObject(Graphics::ScalableBitmapAnimationProvider &prov)`

**Returns:** `explicit`

Creates a new tinted object using another tinted object provider.

##### `ScalableObject(Graphics::ScalableObjectProvider &prov)`

**Returns:** `explicit`

Creates a new tinted object using another tinted object provider.

##### `ScalableObject(—)`

**Returns:** ``

Creates a new tinted object using another tinted object provider. Creates a new tinted object using another tinted object provider. Creates a new tinted object using another tinted object provider. Creates a new empty tinted object

##### `SetProvider(Graphics::ScalableBitmapProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::ScalableBitmapAnimationProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::ScalableObjectProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::ScalableBitmapProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::ScalableBitmapAnimationProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::ScalableObjectProvider &value)`

**Returns:** `void`

Changes the provider stored in this tinted object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `RemoveProvider(—)`

**Returns:** `void`

Removes the provider, if it is own by this resource it will be deleted.

##### `static` `SaveThis(Writer &writer, const Graphics::IScalableObjectProvider &provider)`

**Returns:** `static void`

This function loads a tinted object resource from the file


---

## Functions

### `while(!target)`

**Returns:** ``



### `if(gid == GID::ScalableObject_Props)`

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



### `savethis(Writer &writer, const Graphics::basic_ScalableObjectProvider<T_> &provider)`

**Returns:** `static void`



### `if(b)`

**Returns:** ``



### `SaveAnimation(writer, b)`

**Returns:** ``



### `if(prov != nullptr)`

**Returns:** `else`



### `setthis(F_, Graphics::basic_ScalableObjectProvider<T_> *, T_ *)`

**Returns:** `static void`



### `setthis(F_ f, Graphics::ScalableBitmapProvider *provider, Graphics::Bitmap *o)`

**Returns:** `static void`



### `CallBitmapAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::ScalableBitmapAnimationProvider *provider, Graphics::BitmapAnimationProvider *o)`

**Returns:** `static void`



### `CallBitmapAnimationAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::ScalableObjectProvider *provider, Graphics::RectangularAnimationProvider *o)`

**Returns:** `static void`



### `CallGenericAnimationSetter(f, provider, o)`

**Returns:** ``



### `moveout(Graphics::basic_ScalableObjectProvider<T_> *provider, Graphics::IScalableObjectProvider *&p)`

**Returns:** `static void`



### `setthis(&Graphics::basic_ScalableObjectProvider<T_>::SetBase, bp, b)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `for(auto &child : children)`

**Returns:** ``


