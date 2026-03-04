# WindowManager

> Auto-generated documentation for the **WindowManager** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Icon`

**Namespace:** `internal`

@endcond Represents an icon object that can be used as window icon.

#### Methods

##### `Icon(const Containers::Image &image)`

**Returns:** `explicit`

##### `Icon(Icon &&icon)`

**Returns:** ``

##### `Icon(—)`

**Returns:** ``

##### `Destroy(—)`

**Returns:** `void`

##### `FromImage(const Containers::Image &image)`

**Returns:** `void`


### `Pointer`

**Namespace:** `internal`

Represents a hardware/OS pointer graphic. Hardware pointers do not have the power of Gorgon internal pointers, however, they are mostly delay free and works even when the system is busy.

#### Methods

##### `Pointer(—)`

**Returns:** ``


### `Monitor`

**Namespace:** `internal`

#### Methods

##### `addpadding(const Monitor*, int, int, int, int)`

**Returns:** `friend void`

##### `GetSize(—)`

**Returns:** `Geometry::Size`

Returns the size of this monitor in pixels.

##### `GetLocation(—)`

**Returns:** `Geometry::Point`

Returns the location of this monitor relative to the other monitors in pixels. This function is expected to return (0, 0) if there are no other monitors in the system.

##### `GetArea(—)`

**Returns:** `Geometry::Rectangle`

Returns the area of the entire monitor including shift for multihead displays.

##### `GetUsable(—)`

**Returns:** `Geometry::Bounds`

Returns the area usable rectangle of the monitor. This region excludes any panels on the screen.

##### `GetScaleFactor(—)`

**Returns:** `float`

##### `IsPrimary(—)`

**Returns:** `bool`

Whether this display is primary.

##### `GetName(—)`

**Returns:** `std::string`

Returns the name of the monitor

##### `ASSERT(primary, "WindowManager module is not initialized or there are no connected monitors.")`

**Returns:** ``

Returns the default monitor

##### `for(auto &monitor : monitors)`

**Returns:** ``

Returns all monitors connected to this device Returns the monitor from the given location. If none found, will return nullptr.

##### `static` `Refresh(bool force=false)`

**Returns:** `static void`

Asks WindowManager to refresh the list of monitors. This may deallocate monitors and cause problems. Calling this method raises DisplayChanged to mitigate this problem partially. This function will not re-create monitor list if window manager determines that there are no changes in the monitors. You may set force parameter to true to ensure monitors list is re-created.

##### `static` `IsChangeEventSupported(—)`

**Returns:** `static bool`

In some cases, Changed event is not supported. This function might be used to query if it works or not. Even this event is not supported, RefreshMonitors function causes it to be raised after gathering information.

##### `Monitor(—)`

**Returns:** ``

Fires when window manager raises an event about a change in the monitor or screen layout. Additionally, this event will be fired when RefreshMonitors causes monitor list to be re-created. If monitor pointers are stored, this event should be listened as a call to RefreshMonitors may invalidate these pointers.


---

## Functions

### `for(auto &w : Windows)`

**Returns:** ``



### `CurrentContext()`

**Returns:** `intptr_t`


@cond INTERNAL @endcond


### `init()`

**Returns:** `void`



### `Initialize()`

**Returns:** `void`



### `init()`

**Returns:** ``



### `switchcontext(Gorgon::internal::windowdata &data)`

**Returns:** `void`



### `finalizerender(Gorgon::internal::windowdata &data)`

**Returns:** `void`



### `Initialize()`

**Returns:** `void`


Initializes window manager system


### `CurrentContext()`

**Returns:** `intptr_t`


Returns an identifier for the current context


### `GetClipboardFormats()`

**Returns:** `std::vector<Resource::GID::Type>`


Returns the list of formats that is in the clipboard supported by the Gorgon Library. Use GetAllClipboardFormats to get OS dependent clipboard format list. The following list is the currently supported formats: * Image_Data: This is a Graphics::Bitmap object, this can be constructed from PNG, JPG, BMP, OS Bitmap formats (BMP, DIB), [Gorgon]Bitmap format which is copied from Graphics::Bitmap. Use GetClipboardBitmap * Text: Text data. Use GetClipboardText * HTML: HTML data. Use GetClipboardText This function might hang the program if the owner of the clipboard does not respond. In the future, there might be an asynchronous version of this function.


### `GetClipboardText(Resource::GID::Type type = Resource::GID::Text)`

**Returns:** `std::string`


Returns the clipboard text. If there is no data or its incompatible with text, empty string is returned. May require an existing window. This function will prioritize Unicode text if it exists. type refers to the clipboard type. Currently Text and HTML are supported. This function might hang the program if the owner of the clipboard does not respond. In the future, there might be an asynchronous version of this function.


### `GetClipboardList(Resource::GID::Type type = Resource::GID::FileList)`

**Returns:** `std::vector<std::string>`


Sets the clipboard text to given string. May require an existing window. Currently Text and HTML are supported. If append is set, instead of clearing the clipboard, it will add the given text to the list of clipboard data. This function will copy the text, thus is not suitable if the data is too large. If unicode is true, both unicode and regular text would be set to the given data. If you wish to advertise non-unicode text, you should do it after setting unicode text by setting unicode to false and append to true. Returns a list of strings from the clipboard. If FileList is supplied, it will specifically be files copied from clipboard. If your application can handle remote resources, it would be better to use URIList, as URIList can contain list of any resources, including internet sources like HTTP/FTP/SFTP.


### `SetClipboardList(std::vector<std::string> list, Resource::GID::Type type = Resource::GID::FileList, bool append = false)`

**Returns:** `void`


Sets a list of strings to the clipboard. URIList can work in some operating systems to copy files from internet resources to other applications. But it is not available in all systems thus it is best to use FileList to copy files.


### `GetClipboardBitmap()`

**Returns:** `Containers::Image`


Returns a bitmap from the clipboard. This function chooses the best fitting image from the clipboard. However, in Windows it is not always possible to get a transparent image from browsers. If necessary, it is possible to get HTML code, then fetch the image from the internet using Network module.


### `SetClipboardBitmap(Containers::Image img, bool append = false)`

**Returns:** `void`


Changes the clipboard to the given image. Depending on size of the image, this operation might not work on X11 for now.


### `SetPointer(Window &wind, Graphics::PointerType type)`

**Returns:** `void`


Changes the OS pointer to the requested type. If target OS does not supported the requested type, a similar pointer will be displayed.

