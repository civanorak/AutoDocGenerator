# Windows

> Auto-generated documentation for the **Windows** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `iterator_data`

**Namespace:** `internal`

#### Methods

##### `FindClose(search_handle)`

**Returns:** ``


---

## Functions

### `CreateDirectory(const std::string &name)`

**Returns:** `bool`



### `if(pos!=std::string::npos)`

**Returns:** ``



### `IsDirectory(name)`

**Returns:** `return`



### `IsDirectory(const std::string &path)`

**Returns:** `bool`



### `IsDirectory(const std::wstring &wpath)`

**Returns:** `bool`



### `IsFile(const std::string &path)`

**Returns:** `bool`



### `IsExists(const std::string &path)`

**Returns:** `bool`



### `IsWritable(const std::string &path)`

**Returns:** `bool`



### `IsHidden(const std::string &path)`

**Returns:** `bool`



### `fixwinslashes(std::string &s)`

**Returns:** `void`



### `Canonical(const std::string &path)`

**Returns:** `std::string`



### `PathNotFoundError("Cannot canonicalize the given path: "+path)`

**Returns:** `throw`



### `PathNotFoundError("Cannot canonicalize the given path: "+path)`

**Returns:** `throw`



### `fixwinslashes(ret)`

**Returns:** ``



### `Delete(const std::string &path)`

**Returns:** `bool`



### `it(path)`

**Returns:** `Iterator`



### `for(;it.IsValid()`

**Returns:** ``



### `if(*it!="." && *it!="..")`

**Returns:** ``



### `ChangeDirectory(const std::string &path)`

**Returns:** `bool`



### `CurrentDirectory()`

**Returns:** `std::string`



### `GetCurrentDirectory(MAX_PATH, path)`

**Returns:** ``



### `fixwinslashes(ret)`

**Returns:** ``



### `Copy(const std::string &source, const std::string &target)`

**Returns:** `bool`



### `Move(const std::string &source, const std::string &target)`

**Returns:** `bool`



### `ExeDirectory()`

**Returns:** `std::string`



### `GetModuleFileName(hModule, path, MAX_PATH)`

**Returns:** ``



### `fixwinslashes(dir)`

**Returns:** ``



### `GetDirectory(dir)`

**Returns:** `return`



### `ExePath()`

**Returns:** `std::string`



### `GetModuleFileName(hModule, path, MAX_PATH)`

**Returns:** ``



### `fixwinslashes(dir)`

**Returns:** ``



### `EntryPoints()`

**Returns:** `std::vector<EntryPoint>`



### `SHGetFolderPath(NULL, CSIDL_PROFILE, NULL, SHGFP_TYPE_CURRENT, my_documents)`

**Returns:** ``



### `fixwinslashes(e.Path)`

**Returns:** ``



### `while(*drives)`

**Returns:** ``



### `fixwinslashes(e.Path)`

**Returns:** ``



### `if(data->search_handle==INVALID_HANDLE_VALUE)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `PathNotFoundError("Cannot open directory for reading")`

**Returns:** `throw`



### `if(!other.data)`

**Returns:** ``



### `if(data->search_handle==INVALID_HANDLE_VALUE)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `PathNotFoundError("Cannot open directory for reading")`

**Returns:** `throw`



### `Destroy()`

**Returns:** ``



### `if(!data || !data->data || data->search_handle==INVALID_HANDLE_VALUE)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `GetTime()`

**Returns:** `unsigned long`



### `timeGetTime()`

**Returns:** `return`



### `GetDate()`

**Returns:** `Date`



### `GetLocalTime(&timeinfo)`

**Returns:** ``


