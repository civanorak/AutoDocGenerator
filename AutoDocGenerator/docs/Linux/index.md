# Linux

&gt; Auto-generated documentation for the **Linux** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `iterator_data`

**Namespace:** `internal`


---

## Functions

### `CreateDirectory(const std::string &path)`

**Returns:** `bool`



### `IsDirectory(path)`

**Returns:** `return`



### `IsDirectory(const std::string &path)`

**Returns:** `bool`



### `IsFile(const std::string &path)`

**Returns:** `bool`



### `IsExists(const std::string &path)`

**Returns:** `bool`



### `IsWritable(const std::string &path)`

**Returns:** `bool`



### `IsHidden(const std::string &f)`

**Returns:** `bool`



### `Canonical(const std::string &path)`

**Returns:** `std::string`



### `if(newpath==nullptr)`

**Returns:** ``



### `PathNotFoundError("Cannot canonicalize the given path: "+path)`

**Returns:** `throw`



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



### `getcwd(path, 1024)`

**Returns:** ``



### `copyfile(const std::string &source, const std::string &destination)`

**Returns:** `static bool`



### `close(src)`

**Returns:** ``



### `if(dest==0)`

**Returns:** ``



### `close(src)`

**Returns:** ``



### `close(src)`

**Returns:** ``



### `close(dest)`

**Returns:** ``



### `Copy(const std::string &source, const std::string &target)`

**Returns:** `bool`



### `copyfile(source, target+"/"+source)`

**Returns:** `return`



### `copyfile(source, target)`

**Returns:** `return`



### `dir(s)`

**Returns:** `Iterator`



### `for(;dir.IsValid()`

**Returns:** ``



### `Move(const std::string &source, const std::string &target)`

**Returns:** `bool`



### `ExeDirectory()`

**Returns:** `std::string`



### `GetDirectory(path)`

**Returns:** `return`



### `ExePath()`

**Returns:** `std::string`



### `EntryPoints()`

**Returns:** `std::vector<EntryPoint>`



### `it("/dev/disk/by-label/")`

**Returns:** `Iterator`



### `for(;it.IsValid()`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `for(unsigned i=0;i<e.Name.length()`

**Returns:** ``



### `if(escape)`

**Returns:** ``



### `switch(e.Name[i])`

**Returns:** ``



### `if(e.Name[i]=='\\')`

**Returns:** `else`



### `endmntent(fp)`

**Returns:** ``



### `WildMatch(const char *pat, const char *str)`

**Returns:** `static int`



### `if(*pat == '*')`

**Returns:** ``



### `for(i = 0; pat[i] && (pat[i] != '*')`

**Returns:** ``



### `if(str[i] != pat[i])`

**Returns:** ``



### `if(pat[i] == '*')`

**Returns:** ``



### `if(!data->dir)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `PathNotFoundError("Cannot open directory for reading")`

**Returns:** `throw`



### `Next()`

**Returns:** ``



### `if(!other.data)`

**Returns:** ``



### `if(!data->dir)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `PathNotFoundError("Cannot open directory for reading")`

**Returns:** `throw`



### `if(!data || !data->dir)`

**Returns:** ``



### `if(!ret)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `Next()`

**Returns:** `return`



### `Next()`

**Returns:** `return`



### `GetEnvVar(const std::string &var)`

**Returns:** `std::string`



### `GetUsername()`

**Returns:** `std::string`



### `GetName()`

**Returns:** `std::string`



### `GetDocumentsPath()`

**Returns:** `std::string`



### `GetHomePath()`

**Returns:** `std::string`



### `GetEnvVar("HOME")`

**Returns:** `return`



### `GetDataPath()`

**Returns:** `std::string`



### `GetEnvVar("HOME")`

**Returns:** `return`



### `IsAdmin()`

**Returns:** `bool`



### `Initialize()`

**Returns:** `void`



### `GetName()`

**Returns:** `std::string`



### `if(p!=nullptr)`

**Returns:** ``



### `if(line!="")`

**Returns:** ``



### `issuefile("/etc/os-release")`

**Returns:** `std::ifstream`



### `OpenTerminal()`

**Returns:** `void`



### `DisplayMessage(const std::string &message)`

**Returns:** `void`



### `GetAppDataPath()`

**Returns:** `std::string`



### `GetAppSettingPath()`

**Returns:** `std::string`



### `Start(const std::string &name, const std::vector<std::string> &args)`

**Returns:** `bool`



### `close(execpipe[0])`

**Returns:** ``



### `close(execpipe[1])`

**Returns:** ``



### `if(f==-1)`

**Returns:** ``



### `close(execpipe[0])`

**Returns:** ``



### `close(execpipe[1])`

**Returns:** ``



### `if(f==0)`

**Returns:** ``



### `close(execpipe[0])`

**Returns:** ``



### `for(auto &s : args)`

**Returns:** ``



### `close(execpipe[1])`

**Returns:** ``



### `exit(-1)`

**Returns:** ``



### `close(execpipe[1])`

**Returns:** ``



### `close(execpipe[0])`

**Returns:** ``



### `close(execpipe[0])`

**Returns:** ``



### `Start(const std::string &name, std::streambuf *&buf, const std::vector<std::string> &args)`

**Returns:** `bool`


This variant of start enables reading output of the application, buf is returned, ownership lies with the caller of the function


### `close(execpipe[0])`

**Returns:** ``



### `close(execpipe[1])`

**Returns:** ``



### `if(f==-1)`

**Returns:** ``



### `close(execpipe[0])`

**Returns:** ``



### `close(execpipe[1])`

**Returns:** ``



### `close(outpipe[0])`

**Returns:** ``



### `close(outpipe[1])`

**Returns:** ``



### `if(f==0)`

**Returns:** ``



### `close(execpipe[0])`

**Returns:** ``



### `close(outpipe[0])`

**Returns:** ``



### `dup2(outpipe[1], 1)`

**Returns:** ``



### `for(auto &s : args)`

**Returns:** ``



### `close(execpipe[1])`

**Returns:** ``



### `exit(-1)`

**Returns:** ``



### `close(execpipe[1])`

**Returns:** ``



### `close(outpipe[1])`

**Returns:** ``



### `close(execpipe[0])`

**Returns:** ``



### `close(outpipe[0])`

**Returns:** ``



### `close(execpipe[0])`

**Returns:** ``



### `Open(const std::string &file)`

**Returns:** `bool`



### `Start("kde-open", {file})`

**Returns:** `return`



### `Start("gnome-open", {file})`

**Returns:** `return`



### `processmessages()`

**Returns:** `void`



### `for(auto &w : Window::Windows)`

**Returns:** ``



### `fctocss(int weight)`

**Returns:** `int`



### `for(i=0; i<mapping.size()`

**Returns:** ``



### `if(mapping[i].first >= weight)`

**Returns:** ``



### `GetFontFamilies()`

**Returns:** `std::vector<FontFamily>`



### `if(lang)`

**Returns:** ``



### `FcPatternAddLangSet(pat, FC_LANG, lang)`

**Returns:** ``



### `FcConfigSetRescanInterval(config, GORGON_FONTCONFIG_INTERVAL)`

**Returns:** ``



### `if(!fs)`

**Returns:** ``



### `FcObjectSetDestroy(os)`

**Returns:** ``



### `FcPatternDestroy(pat)`

**Returns:** ``



### `FcLangSetDestroy(lang)`

**Returns:** ``



### `for(int i=0; i<fs->nfont; i++)`

**Returns:** ``



### `FcPatternGetString(font, FC_FILE, 0, &file)`

**Returns:** ``



### `FcPatternGetString(font, FC_FAMILY, 0, &family)`

**Returns:** ``



### `FcPatternGetString(font, FC_STYLE, 0, &style)`

**Returns:** ``



### `FcPatternGetInteger(font, FC_WEIGHT, 0, &weight)`

**Returns:** ``



### `FcPatternGetInteger(font, FC_SLANT, 0, &slant)`

**Returns:** ``



### `FcPatternGetInteger(font, FC_SPACING, 0, &spacing)`

**Returns:** ``



### `FcPatternGetInteger(font, FC_WIDTH, 0, &width)`

**Returns:** ``



### `FcObjectSetDestroy(os)`

**Returns:** ``



### `FcPatternDestroy(pat)`

**Returns:** ``



### `FcLangSetDestroy(lang)`

**Returns:** ``



### `GetDate()`

**Returns:** `Date`



### `time(&rawtime)`

**Returns:** ``



### `gettimeofday(&tv, NULL)`

**Returns:** ``



### `GetTime()`

**Returns:** `unsigned long`



### `gettimeofday(&tv, 0)`

**Returns:** ``


