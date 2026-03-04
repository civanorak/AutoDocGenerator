# Pointer

> Auto-generated documentation for the **Pointer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Pointer`

**Namespace:** `Gorgon`

No pointer is selected or using default. Do not use this value Arrow / Pointer Wait / Hourglass Processing, pointer and wait combined No / Not allowed Text / Beam pointer A pointer for links Cursor icon that offers to move an item Drag / Closed hand pointer Scaling from left side Scaling from the right side Scaling from top side Scaling from bottom side Scaling from top left corner Scaling from top right corner Scaling from bottom left corner Scaling from bottom right corner Cross hair to select a point A cursor denotes a help text Straight upward pointing arrow, can be used for alternative objects Do not use this value

#### Methods

##### `GetType(—)`

**Returns:** `PointerType`

Returns the type of the pointer

##### `SetType(PointerType value)`

**Returns:** `void`

Sets the type of the pointer. Pointer type can be used to determine the type while adding to the stack. If operating system pointers are used, this value is used determine which pointer to show.


### `DrawablePointer`

**Namespace:** `Gorgon`

This class turns a drawable into a pointer

#### Methods

##### `SetType(type)`

**Returns:** ``

Initializes a pointer. Ownership of the drawable is not transferred. Use Assume function after invoking default constructor to transfer ownership.

##### `SetType(type)`

**Returns:** ``

Initializes a pointer. Ownership of the drawable is not transferred. Use Assume function after invoking default constructor to transfer ownership.

##### `SetType(type)`

**Returns:** ``

Initializes a pointer. Ownership of the drawable is not transferred. Use Assume function after invoking default constructor to transfer ownership.

##### `SetType(type)`

**Returns:** ``

Initializes a pointer. Ownership of the drawable is not transferred. Use Assume function after invoking default constructor to transfer ownership.

##### `RemoveImage(—)`

**Returns:** ``

##### `RemoveImage(—)`

**Returns:** ``

##### `HasImage(—)`

**Returns:** `bool`

Returns if the pointer has an image

##### `ASSERT(image, "Pointer image is not set")`

**Returns:** ``

Returns the image contained in this pointer. You should check HasImage before accessing to the image

##### `SetImage(const Drawable &value)`

**Returns:** `void`

Changes the image of this pointer

##### `RemoveImage(—)`

**Returns:** ``

##### `Assume(const Drawable &value)`

**Returns:** `void`

Changes the image of the pointer by assuming the ownership of the given image

##### `RemoveImage(—)`

**Returns:** ``

##### `Assume(const Drawable &value, Geometry::Point hotspot)`

**Returns:** `void`

Changes the image of the pointer by assuming the ownership of the given image

##### `RemoveImage(—)`

**Returns:** ``

##### `Assume(const Drawable &value, int x, int y)`

**Returns:** `void`

Changes the image of the pointer by assuming the ownership of the given image

##### `RemoveImage(—)`

**Returns:** ``

##### `RemoveImage(—)`

**Returns:** `void`

Removes the image from the pointer

##### `if(owner)`

**Returns:** ``


### `basic_AnimatedPointer`

**Namespace:** `Gorgon`

Releases the ownership of the drawable and removes it from the pointer Represents animated pointer.

#### Methods

##### `ASSERT(anim, "Trying to use a moved out pointer")`

**Returns:** ``

##### `ASSERT(anim, "Trying to use a moved out pointer")`

**Returns:** ``

##### `ASSERT(anim, "Trying to use a moved out pointer")`

**Returns:** ``

##### `ASSERT(anim, "Trying to use a moved out pointer")`

**Returns:** ``


### `basic_PointerProvider`

**Namespace:** `Gorgon`

This class stores information that allows an animated pointer to be created.

#### Methods

##### `hotspot(hotspot)`

**Returns:** ``

##### `CreatePointer(Gorgon::Animation::Timer &timer)`

**Returns:** `AnimationType`

Move constructor Creates a pointer from this provider

##### `CreatePointer(bool create = true)`

**Returns:** `AnimationType`

Creates a pointer from this provider, just a rename for CreateAnimation

##### `GetHotspot(—)`

**Returns:** `Geometry::Point`

Creates a pointer from this provider Creates a pointer from this provider Returns the hotspot of the provider

##### `SetHotspot(Geometry::Point value)`

**Returns:** `void`

Sets the hotspot of the pointer

##### `GetType(—)`

**Returns:** `PointerType`

Returns the type of the pointer

##### `SetType(PointerType value)`

**Returns:** `void`

Sets the type of the pointer. Pointer type can be used to determine the type while adding to the stack. If operating system pointers are used, this value is used determine which pointer to show.


### `PointerStack`

**Namespace:** `Gorgon`

Hotspot will be transferred to newly created pointers Whether the animation is owned by this object


### `Token`

**Namespace:** `Gorgon`

Token type, automatically pops pointer stack when goes out of scope

#### Methods

##### `Token(—)`

**Returns:** ``

##### `Token(Token &&other)`

**Returns:** ``

##### `Revert(—)`

**Returns:** ``

##### `Revert(—)`

**Returns:** ``

##### `Revert(—)`

**Returns:** `void`

##### `IsNull(—)`

**Returns:** `bool`

Checks if the token is null

##### `bool(—)`

**Returns:** `explicit operator`

Checks if the token is valid


### `Wrapper`

**Namespace:** `Gorgon`

This event is fired if the pointer at the top is changed.


### `Pointer`

**Namespace:** `Gorgon`

#### Methods

##### `Add(bmp)`

**Returns:** ``

##### `SetType(type)`

**Returns:** ``

##### `SetType(type)`

**Returns:** ``

##### `Pointer(Graphics::PointerType type = Graphics::PointerType::None)`

**Returns:** `explicit`

##### `SetType(type)`

**Returns:** ``

##### `MoveOut(—)`

**Returns:** `Graphics::BitmapPointerProvider`

Moves the pointer provider out of resource system. Use Prepare and Discard before calling this function to avoid data duplication

##### `static` `LoadResource(std::weak_ptr< Gorgon::Resource::File > file, std::shared_ptr< Gorgon::Resource::Reader > reader, long unsigned int size)`

**Returns:** `static Resource::Pointer*`

This function loads a bitmap font resource from the given file


---

## Enums

### `PointerType`

**Namespace:** `Gorgon`

Pointer types


---

## Functions

### `Add(type, pointer)`

**Returns:** ``



### `Add(type, *ptr)`

**Returns:** ``



### `PointerChanged()`

**Returns:** ``



### `Token(this, lastind++)`

**Returns:** `return`



### `PointerChanged()`

**Returns:** ``



### `Token(this, lastind++)`

**Returns:** `return`



### `PointerChanged()`

**Returns:** ``



### `PointerStack(PointerStack &&other)`

**Returns:** ``


Checks if the token is invalid


### `Swap(other)`

**Returns:** ``



### `Swap(PointerStack &other)`

**Returns:** `void`



### `swap(lastind, other.lastind)`

**Returns:** ``



### `swap(stack, other.stack)`

**Returns:** ``



### `swap(pointers, other.pointers)`

**Returns:** ``



### `for(auto &w : pointers)`

**Returns:** ``



### `Add(PointerType type, const Pointer &pointer)`

**Returns:** `void`


Adds the given pointer to the stack. Ownership of the pointer will not be transferred. If the given pointer type exists old one will be overridden. If the old pointer is managed by this stack then it will be deleted.


### `Add(const Pointer &pointer)`

**Returns:** `void`


Adds the given pointer to the stack. Ownership of the pointer will not be transferred. If the given pointer type exists old one will be overridden. If the old pointer is managed by this stack then it will be deleted. Type that is set in the pointer is used to refer to this pointer.


### `Assume(PointerType type, const Pointer &pointer)`

**Returns:** `void`


Adds the given pointer to the stack. Ownership of the pointer will be transferred. If the given pointer type exists old one will be overridden. If the old pointer is managed by this stack then it will be deleted.


### `Add(PointerType type, const Drawable &image, Geometry::Point hotspot)`

**Returns:** `void`


Creates and adds a new pointer. Life time of this new pointer will be bound to the life time of the stack. If the given pointer type exists old one will be overridden. If the old pointer is managed by this stack then it will be deleted.


### `Exists(PointerType type)`

**Returns:** `bool`


Checks if the given pointer exists


### `GetCurrentType()`

**Returns:** `PointerType`



### `Set(PointerType type)`

**Returns:** `Token`


Set the current pointer to the given type. This would return a token to be used to reset this operation. The token should be stored in a variable otherwise the pointer would be reset immediately.


### `Set(const Pointer &pointer)`

**Returns:** `Token`


Sets the current pointer in the stack to the given pointer. This pointer will not be added to the list. The token should be stored in a variable otherwise the pointer would be reset immediately.


### `Reset(Token &token)`

**Returns:** `void`


Removes a pointer shape from the stack. If the given token is null or does not belong to this stack, nothing is done.


### `IsValid()`

**Returns:** `bool`


Returns the pointer on top of the stack, if no pointer is on the stack, first pointer in the order of PointerType enums will be returned. If no pointers are registered, this function will throw runtime_error Returns if the stack is valid to be used. A valid stack requires at least one registered or pushed pointer


### `ASSERT(anim, "Try to use a moved out pointer")`

**Returns:** ``



### `while(!target)`

**Returns:** ``



### `if(gid==GID::Pointer_Props)`

**Returns:** ``



### `if(gid == GID::Animation)`

**Returns:** `else`



### `if(obj)`

**Returns:** ``



### `for(auto frame : frames)`

**Returns:** ``


