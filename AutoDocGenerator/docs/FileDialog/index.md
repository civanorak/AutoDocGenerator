# FileDialog

&gt; Auto-generated documentation for the **FileDialog** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `File`

**Namespace:** `gge`

#### Methods

##### `init(—)`

**Returns:** ``

##### `RefreshPaths(—)`

**Returns:** `void`

##### `for(auto it=paths.begin()`

**Returns:** ``

##### `if(it->Name=="")`

**Returns:** ``

##### `RefreshFiles(—)`

**Returns:** `void`

##### `for(auto it=os::filesystem::DirectoryIterator(curdir)`

**Returns:** ``

##### `for(auto it=os::filesystem::DirectoryIterator(curdir, mask)`

**Returns:** ``

##### `Show(bool focus=true)`

**Returns:** `void`

##### `init(—)`

**Returns:** `void`

##### `SetContainer(activevp)`

**Returns:** ``

##### `SetContainer(TopLevel)`

**Returns:** ``

##### `SetBlueprint(WR.Panels.DialogWindow)`

**Returns:** ``

##### `RefreshFiles(—)`

**Returns:** ``

##### `placedialogbutton(Cancel)`

**Returns:** ``

##### `placedialogbutton(Ok)`

**Returns:** ``

##### `RefreshPaths(—)`

**Returns:** ``

##### `RefreshFiles(—)`

**Returns:** ``

##### `relocate(—)`

**Returns:** ``

##### `relocate(—)`

**Returns:** `void`

##### `MoveToCenter(—)`

**Returns:** ``

##### `Accept(—)`

**Returns:** `void`

##### `if(multiselect)`

**Returns:** ``

##### `MultiSelectRepliedEvent(files)`

**Returns:** ``

##### `ShowMessage("Please select a directory.", Title)`

**Returns:** ``

##### `ShowMessage("Please select a file.", Title)`

**Returns:** ``

##### `if(onlyexisting)`

**Returns:** ``

##### `if(directoriesonly)`

**Returns:** ``

##### `ShowMessage("Directory not found: "+Filename.Text, Title)`

**Returns:** ``

##### `ShowMessage("File not found: "+Filename.Text, Title)`

**Returns:** ``

##### `if(askoverwrite)`

**Returns:** ``

##### `if(reply)`

**Returns:** ``

##### `Close(—)`

**Returns:** ``

##### `if(reply)`

**Returns:** ``

##### `Close(—)`

**Returns:** ``

##### `RepliedEvent(f)`

**Returns:** ``

##### `Close(—)`

**Returns:** ``

##### `path_click(Listbox<utils::CaptionValue<std::string> >::ItemType &item)`

**Returns:** `void`

##### `RefreshFiles(—)`

**Returns:** ``

##### `file_click(Listbox<utils::CaptionValue<std::string> >::ItemType &item)`

**Returns:** `void`

##### `if(v==selectedfile)`

**Returns:** ``

##### `if(v[0]=='/')`

**Returns:** ``

##### `ShowMessage("The directory "+v+" is vanished.", "Folder not found!")`

**Returns:** ``

##### `RefreshFiles(—)`

**Returns:** ``

##### `RefreshFiles(—)`

**Returns:** ``

##### `if(!directoriesonly)`

**Returns:** ``

##### `RepliedEvent(selectedfile)`

**Returns:** ``

##### `Close(—)`

**Returns:** ``

##### `if(selectedfile[0]!='/' || directoriesonly)`

**Returns:** ``

##### `setAskOverwrite(const bool &value)`

**Returns:** `void`

##### `getAskOverwrite(—)`

**Returns:** `bool`

##### `setOnlyExisting(const bool &value)`

**Returns:** `void`

##### `getOnlyExisting(—)`

**Returns:** `bool`

##### `setDirectoriesOnly(const bool &value)`

**Returns:** `void`

##### `if(directoriesonly!=value)`

**Returns:** ``

##### `if(!directoriesonly && Filename.Text=="")`

**Returns:** ``

##### `RefreshFiles(—)`

**Returns:** ``

##### `getDirectoriesOnly(—)`

**Returns:** `bool`

##### `setMultiSelect(const bool &value)`

**Returns:** `void`

##### `if(multiselect!=value)`

**Returns:** ``

##### `getMultiSelect(—)`

**Returns:** `bool`

##### `setCurrentDirectory(const std::string &value)`

**Returns:** `void`

##### `if(curdir!=d)`

**Returns:** ``

##### `RefreshFiles(—)`

**Returns:** ``

##### `getCurrentDirectory(—)`

**Returns:** `std::string`

##### `setMask(const std::string &value)`

**Returns:** `void`

##### `if(mask!=value)`

**Returns:** ``

##### `RefreshFiles(—)`

**Returns:** ``

##### `getMask(—)`

**Returns:** `std::string`

##### `setColumns(const int &value)`

**Returns:** `void`

##### `if(columns!=value)`

**Returns:** ``

##### `relocate(—)`

**Returns:** ``

##### `getColumns(—)`

**Returns:** `int`

