# Win32

&gt; Auto-generated documentation for the **Win32** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `MByteToUnicode(const std::string &multiByteStr)`

**Returns:** `std::string`



### `UnicodeToMByte(LPCWSTR unicodeStr)`

**Returns:** `std::string`



### `WideCharToMultiByte(CP_UTF8, NULL, unicodeStr, -1, &ret[0], minSize, NULL, FALSE)`

**Returns:** ``



### `GetEnvVar(const std::string &var)`

**Returns:** `std::string`



### `Initialize()`

**Returns:** `void`



### `GetUsername()`

**Returns:** `std::string`



### `GetUserName(username, &s)`

**Returns:** ``



### `GetName()`

**Returns:** `std::string`



### `GetUserNameEx(NameDisplay, name, &s)`

**Returns:** ``



### `GetDocumentsPath()`

**Returns:** `std::string`



### `SHGetFolderPath(NULL, CSIDL_PERSONAL, NULL, SHGFP_TYPE_CURRENT, my_documents)`

**Returns:** ``



### `GetHomePath()`

**Returns:** `std::string`



### `SHGetFolderPath(NULL, CSIDL_PROFILE, NULL, SHGFP_TYPE_CURRENT, profile)`

**Returns:** ``



### `GetDataPath()`

**Returns:** `std::string`



### `SHGetFolderPath(NULL, CSIDL_APPDATA, NULL, SHGFP_TYPE_CURRENT, path)`

**Returns:** ``



### `IsAdmin()`

**Returns:** `bool`



### `GetUserNameW(user_name, &size)`

**Returns:** ``



### `NetApiBufferFree(info)`

**Returns:** ``



### `OpenTerminal()`

**Returns:** `void`



### `AllocConsole()`

**Returns:** ``



### `setvbuf(stdout, NULL, _IONBF, 0)`

**Returns:** ``



### `setvbuf(stdin, NULL, _IONBF, 0)`

**Returns:** ``



### `setvbuf(stderr, NULL, _IONBF, 0)`

**Returns:** ``



### `GetName()`

**Returns:** `std::string`



### `GetVersionEx(&os)`

**Returns:** ``



### `if(os.dwMajorVersion == 5)`

**Returns:** ``



### `switch(os.dwMinorVersion)`

**Returns:** ``



### `if(os.dwMajorVersion == 6)`

**Returns:** `else`



### `switch(os.dwMinorVersion)`

**Returns:** ``



### `if(os.dwMajorVersion == 10)`

**Returns:** `else`



### `DisplayMessage(const std::string &message)`

**Returns:** `void`



### `GetAppDataPath()`

**Returns:** `std::string`



### `SHGetFolderPath(NULL, CSIDL_COMMON_APPDATA, NULL, SHGFP_TYPE_CURRENT, path)`

**Returns:** ``



### `GetAppSettingPath()`

**Returns:** `std::string`



### `GetAppDataPath()`

**Returns:** `return`



### `processmessages()`

**Returns:** `void`



### `for(auto &w : Window::Windows)`

**Returns:** ``



### `GetMessage(&msg, NULL, 0, 0)`

**Returns:** ``



### `DispatchMessage(&msg)`

**Returns:** ``



### `TranslateMessage(&msg)`

**Returns:** ``



### `Start(const std::string &name, const std::vector<std::string> &args)`

**Returns:** `bool`



### `for(auto &arg : args)`

**Returns:** ``



### `if(usepath)`

**Returns:** ``



### `for(auto arg : args)`

**Returns:** ``



### `if(usepath)`

**Returns:** ``



### `if(ret)`

**Returns:** ``



### `CloseHandle(pi.hProcess)`

**Returns:** ``



### `CloseHandle(pi.hThread)`

**Returns:** ``



### `Open(const std::string &file)`

**Returns:** `bool`



### `normalslashtowin(std::string &s)`

**Returns:** `void`



### `winslashtonormal(std::string &s)`

**Returns:** `void`



### `GetFontFamilies()`

**Returns:** `std::vector<FontFamily>`



### `FT_Init_FreeType(&library)`

**Returns:** ``



### `for(auto filename : filenames)`

**Returns:** ``



### `if(face)`

**Returns:** ``



### `FT_Done_Face(face)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `if(tbl != nullptr)`

**Returns:** ``



### `FT_Done_FreeType(library)`

**Returns:** ``


