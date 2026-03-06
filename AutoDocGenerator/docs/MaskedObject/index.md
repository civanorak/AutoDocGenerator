# MaskedObject

&gt; Auto-generated documentation for the **MaskedObject** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `IMaskedObjectProvider`

**Namespace:** `Gorgon`

For ease of use in resource system


### `basic_MaskedObject`

**Namespace:** `Gorgon`

#### Methods

##### `basic_MaskedObject(const basic_MaskedObjectProvider<A_> &parent, bool create = true)`

**Returns:** ``

##### `basic_MaskedObject(const basic_MaskedObjectProvider<A_> &parent, Gorgon::Animation::ControllerBase &timer)`

**Returns:** ``


### `basic_MaskedObjectProvider`

**Namespace:** `Gorgon`

Creates a masked object from two animations, these animations should not have controllers attached to them. Any attached controllers will be replaced or removed. A non-const version cannot work as this object needs to control the controllers of these animations. Creates a masked object from two animations, these animations should not have controllers attached to them Any attached controllers will be replaced or removed. A non-const version cannot work as this object needs to control the controllers of these animations.

#### Methods

##### `if(own)`

**Returns:** ``

Empty constructor Filling constructor Filling constructor, nullptr is allowed but not recommended

##### `if(base)`

**Returns:** ``

Creates a base animation without controller.

##### `if(mask)`

**Returns:** ``

Creates a mask animation without controller.

##### `SetBase(A_ *value)`

**Returns:** `void`

Returns the base component. Could return nullptr Returns the mask component. Could return nullptr Sets the base provider, ownership semantics will not be changed

##### `SetMask(A_ *value)`

**Returns:** `void`

Sets the mask provider, ownership semantics will not be changed

##### `SetProviders(A_ &base, A_ &mask)`

**Returns:** `void`

Sets the providers in this object

##### `if(own)`

**Returns:** ``

##### `OwnProviders(—)`

**Returns:** `void`

Assumes the ownership of the providers

##### `Prepare(—)`

**Returns:** `void`

Prepares the providers. Provider type should support this operation, otherwise this function will cause a compile time error.


### `MaskedObject`

**Namespace:** `Gorgon`

#### Methods

##### `MaskedObject(Graphics::MaskedBitmapProvider &prov)`

**Returns:** `explicit`

Creates a new masked object using another masked object provider.

##### `MaskedObject(Graphics::MaskedBitmapAnimationProvider &prov)`

**Returns:** `explicit`

Creates a new masked object using another masked object provider.

##### `MaskedObject(Graphics::MaskedObjectProvider &prov)`

**Returns:** `explicit`

Creates a new masked object using another masked object provider.

##### `MaskedObject(—)`

**Returns:** ``

Creates a new masked object using another masked object provider. Creates a new masked object using another masked object provider. Creates a new masked object using another masked object provider. Creates a new empty masked object

##### `SetProvider(Graphics::MaskedBitmapProvider &value)`

**Returns:** `void`

Changes the provider stored in this masked object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::MaskedBitmapAnimationProvider &value)`

**Returns:** `void`

Changes the provider stored in this masked object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::MaskedObjectProvider &value)`

**Returns:** `void`

Changes the provider stored in this masked object, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::MaskedBitmapProvider &value)`

**Returns:** `void`

Changes the provider stored in this masked object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::MaskedBitmapAnimationProvider &value)`

**Returns:** `void`

Changes the provider stored in this masked object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::MaskedObjectProvider &value)`

**Returns:** `void`

Changes the provider stored in this masked object, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `RemoveProvider(—)`

**Returns:** `void`

Removes the provider, if it is own by this resource it will be deleted.

##### `static` `SaveThis(Writer &writer, const Graphics::IMaskedObjectProvider &provider)`

**Returns:** `static void`

This function loads a masked object resource from the file


---

## Functions

### `while(!target)`

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



### `savethis(Writer &writer, const Graphics::basic_MaskedObjectProvider<T_> &provider)`

**Returns:** `static void`



### `if(!m)`

**Returns:** ``



### `SaveAnimation(writer, m)`

**Returns:** ``



### `SaveAnimation(writer, b)`

**Returns:** ``



### `SaveAnimation(writer, m)`

**Returns:** ``



### `if(prov != nullptr)`

**Returns:** `else`



### `setthis(F_, Graphics::basic_MaskedObjectProvider<T_> *, T_ *)`

**Returns:** `static void`



### `setthis(F_ f, Graphics::MaskedBitmapProvider *provider, Graphics::Bitmap *o)`

**Returns:** `static void`



### `CallBitmapAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::MaskedBitmapAnimationProvider *provider, Graphics::BitmapAnimationProvider *o)`

**Returns:** `static void`



### `CallBitmapAnimationAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::MaskedObjectProvider *provider, Graphics::RectangularAnimationProvider *o)`

**Returns:** `static void`



### `CallGenericAnimationSetter(f, provider, o)`

**Returns:** ``



### `moveout(Graphics::basic_MaskedObjectProvider<T_> *provider, Graphics::IMaskedObjectProvider *&p)`

**Returns:** `static void`



### `setthis(&Graphics::basic_MaskedObjectProvider<T_>::SetBase, bp, b)`

**Returns:** ``



### `setthis(&Graphics::basic_MaskedObjectProvider<T_>::SetMask, bp, m)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `for(auto &child : children)`

**Returns:** ``


