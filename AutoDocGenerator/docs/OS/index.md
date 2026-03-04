# OS

> Auto-generated documentation for the **OS** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Info`

**Namespace:** `User`

This structure represents the version of the operating system


### `Font`

**Namespace:** `User`

This class represents a single font.

#### Methods

##### `GetWeight(—)`

**Returns:** `FontWeight`

Returns the named weight of the font.

##### `if(Weight <= 150)`

**Returns:** ``

##### `if(Weight <= 250)`

**Returns:** `else`

##### `if(Weight <= 350)`

**Returns:** `else`

##### `if(Weight > 850)`

**Returns:** `else`

##### `if(Weight > 750)`

**Returns:** `else`

##### `if(Weight > 650)`

**Returns:** `else`

##### `if(Weight > 550)`

**Returns:** `else`

##### `if(Weight > 450)`

**Returns:** `else`

##### `GetCSSWeight(—)`

**Returns:** `std::string`

Returns CSS usable weight of the font.


### `FontFamily`

**Namespace:** `User`

This is the style name of the font. Apart form Regular, Bold, Italic it could have different names such as narrow, Extra-bold If this is a bold font Weight of the font. This is same as CSS3, 400 is regular Width of the font, 100 is regular, 75 is condensed and 125 is expanded. Whether the font is italic or not Whether the font is monospaced Name of the font family Filename of the font


---

## Enums

### `OSType`

**Namespace:** `User`


### `FontWeight`

**Namespace:** `User`


---

## Functions

### `DumpFontFamilies(std::ostream &file)`

**Returns:** `void`



### `for(auto &face : fam.Faces)`

**Returns:** ``



### `Initialize()`

**Returns:** `void`


Initializes operating system module.


### `GetUsername()`

**Returns:** `std::string`


Returns the current username


### `GetName()`

**Returns:** `std::string`


Returns the name of the current user


### `GetDocumentsPath()`

**Returns:** `std::string`


Returns the path where documents of the user should be saved


### `GetHomePath()`

**Returns:** `std::string`


Returns the home directory of the user


### `GetDataPath()`

**Returns:** `std::string`


Returns the path where applications can save data related to this user. This path could simply be user's home directory. Best practice would be creating a directory that starts with a "." such as .gorgon


### `IsAdmin()`

**Returns:** `bool`


Check if the currently logged in user is an administrator. If you are looking to perform an elevated operation, you best try to perform the operation without checking if the user is an admin first. It might be possible for a regular user to have extra permissions. Check this function afterwards before asking for elevation.


### `OpenTerminal()`

**Returns:** `void`


Opens a terminal window to display output from the stdout. This is not required for most operating systems and will not perform anything unless its necessary.


### `DisplayMessage(const std::string &message)`

**Returns:** `void`


This function shows a OS message box to display errors, for other messages its better to use in-game dialogs


### `GetAppDataPath()`

**Returns:** `std::string`


Returns the directory where the system wide application data is stored. Most probably it will be read only


### `GetAppSettingPath()`

**Returns:** `std::string`


Returns the directory where the system wide application settings is stored. Most probably it will be read only


### `GetEnvVar(const std::string &var)`

**Returns:** `std::string`


Returns the value of an environment variable.


### `GetName()`

**Returns:** `std::string`


Returns the name of the current operating system in human readable form. Might change from installation to installation.


### `GetInfo()`

**Returns:** `Info`


Identifier for the current operating system Name of the current operating system Major version Minor version Revision Build number Number of bits in the architecture, this number is independent of compiled platform of Gorgon Library The name  of the architecture, this information is independent of compiled platform of Gorgon Library Returns information related with the operating system, including version, name, and architecture.


### `Open(const std::string &file)`

**Returns:** `bool`


Starts the given application. This application is searched from the installed applications unless it includes a path. You may use `./appname` to start the appname from the current directory. The application is started in a separate process and the current process does not stop to wait its execution. @warning Depending on the operating system, executables in the current directory might take precedence even if no path is given. @return  true if the program is found and started. Does not check if the program continues working properly Opens the given file with the related application. This can also be a URI. @return true if the given file is somehow opened. This includes open with dialog if it can be displayed


### `processmessages()`

**Returns:** `void`


This method will notify the system should process any messages that coming from the operating system. Internally used. Should only be used when necessary.


### `GetFontFamilies()`

**Returns:** `std::vector<FontFamily>`


Name of the font family Individual fonts in the family


### `DumpFontFamilies(std::ostream &out)`

**Returns:** `void`


