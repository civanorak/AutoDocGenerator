# DWM

&gt; Auto-generated documentation for the **DWM** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `GGEDropTarget`

**Namespace:** `WindowManager`

#### Methods

##### `QueryInterface(REFIID iid, void **ppvObject)`

**Returns:** `HRESULT __stdcall`

##### `AddRef(void)`

**Returns:** `ULONG   __stdcall`

##### `Release(void)`

**Returns:** `ULONG   __stdcall`

##### `DragEnter(IDataObject *pDataObject, DWORD grfKeyState, POINTL pt, DWORD *pdwEffect)`

**Returns:** `HRESULT __stdcall`

##### `DragOver(DWORD grfKeyState, POINTL pt, DWORD *pdwEffect)`

**Returns:** `HRESULT __stdcall`

##### `DragLeave(void)`

**Returns:** `HRESULT __stdcall`

##### `Drop(IDataObject *pDataObject, DWORD grfKeyState, POINTL pt, DWORD *pdwEffect)`

**Returns:** `HRESULT __stdcall`

##### `dragfinished(—)`

**Returns:** `void`


### `clipboardentry`

**Namespace:** `WindowManager`


### `monitordata`

**Namespace:** `internal`


### `icondata`

**Namespace:** `internal`


### `windowdata`

**Namespace:** `internal`

#### Methods

##### `Proc(UINT message, WPARAM wParam, LPARAM lParam)`

**Returns:** `LRESULT`


---

## Functions

### `GetMousePosition(Gorgon::internal::windowdata *wind)`

**Returns:** `Geometry::Point`


@cond INTERNAL


### `GetCursorPos(&pnt)`

**Returns:** ``



### `switchcontext(Gorgon::internal::windowdata &data)`

**Returns:** `void`



### `wglMakeCurrent(data.device_context, data.context)`

**Returns:** ``



### `finalizerender(Gorgon::internal::windowdata &data)`

**Returns:** `void`



### `SwapBuffers(data.device_context)`

**Returns:** ``



### `init()`

**Returns:** `void`


@endcond


### `FromImage(image)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `DeleteObject(hBitmap)`

**Returns:** ``



### `DeleteObject(hMonoBitmap)`

**Returns:** ``



### `if(data->icon)`

**Returns:** ``



### `DeleteObject(data->icon)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `MByteToUnicode(const std::string &multiByteStr)`

**Returns:** `std::string`



### `UnicodeToMByte(LPCWSTR unicodeStr)`

**Returns:** `std::string`



### `winslashtonormal(std::string &)`

**Returns:** `void`



### `normalslashtowin(std::string &s)`

**Returns:** `void`



### `osgetkeyname(Input::Keyboard::Key key)`

**Returns:** `std::string`



### `maposkey(WPARAM wParam, LPARAM lParam)`

**Returns:** `Input::Keyboard::Key`



### `GetMousePosition(Gorgon::internal::windowdata *wind)`

**Returns:** `Geometry::Point`



### `renderformat(unsigned type)`

**Returns:** `void`



### `clearkeys(Gorgon::internal::windowdata *data)`

**Returns:** `void`



### `handleinputevent(Gorgon::internal::windowdata *data, UINT message, WPARAM wParam, LPARAM lParam)`

**Returns:** `void`



### `make_clipboarddata(T_ data)`

**Returns:** `std::shared_ptr<CopyFreeAny>`



### `ishandled(HWND hwnd, Input::Key key)`

**Returns:** `bool`


