# File

> Auto-generated documentation for the **File** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Loader`

**Namespace:** `Gorgon`

This class defines a resource loader. The set of predefined resource loaders exists within the resource system, however, it is possible to register custom loaders for custom objects.


### `File`

**Namespace:** `Gorgon`

This is Resource loader function prototype. Please note that, it is possible to use your own type derived from Base for the return type. First parameter is the stream object to read data from. The stream object would be opened in binary mode. Second parameter is the size of the data chunk. After reading the object, file pointer should be moved exactly the amount of data chunk. Last parameter is the file object that manages the current load operation. This function should return nullptr in case of an error, otherwise it should return the newly loaded object. The ownership of this object will be transferred to the parent of the object and it will be deleted with its parent unless detached from the tree. Filling constructor Empty constructor Gorgon ID of the resource that this loaded can load. Load handler function This class represents a logical resource file. A file class is necessary for loading a resource file from the disk. However, it is not required to create a resource tree in memory. Notice that Gorgon::Resource does not support saving, Gorgon::Resource::Editing has the support for saving resource files.

#### Methods

##### `File(—)`

**Returns:** ``

Default constructor

##### `Release(—)`

**Returns:** `std::unique_ptr<Folder>`

Destroys file object. If the root is not detached, it will destroy resource tree as well. Returns the root folder of the file Detaches the root of the File from the File object. The ownership of the root will be transferred to the caller.

##### `r(root)`

**Returns:** `std::unique_ptr<Folder>`

##### `Prepare(—)`

**Returns:** `void`

Prepares all resources in this file to be used. This function can be issued for individual objects and their children rather than whole file.

##### `Discard(—)`

**Returns:** `void`

Discards any data that is not required after preparation. The stored data might have significance in some applications, other than those, there is no reason to keep prepared data. Also discards guid mapping

##### `Destroy(—)`

**Returns:** `void`

Destroys the Gorgon resource tree that this file holds. This file object can still be used after destroy is issued

##### `LoadFile(const std::string &filename)`

**Returns:** `void`

Loads the given file. A prepare function call is necessary to be able to use some resources. The file could be left open if there are objects marked to be loaded when requested. If the filename not found and there is a filename.lzma file, this function extracts the compressed file and tries to load uncompressed version. @throws LoadError @throws std::runtime_error

##### `createfilereader(filename)`

**Returns:** ``

##### `load(false, false)`

**Returns:** ``

##### `LoadFirst(const std::string &filename)`

**Returns:** `void`

Loads only the first object of the given file. Useful to retrieve header information. If the filename not found and there is a filename.lzma file, this function extracts the compressed file and tries to load uncompressed version. @throws LoadError @throws std::runtime_error

##### `createfilereader(filename)`

**Returns:** ``

##### `load(true, false)`

**Returns:** ``

##### `LoadShallow(const std::string &filename)`

**Returns:** `void`

Loads only the first tier of objects. Only folders refrain from loading its children. Therefore, any other object will be loaded fully. This function should be use carefully in presence of links Any links that are reaching out to unloaded parts of the file will not be resolved. This may cause cast errors. Useful to selectively load a large file. Use Folder::Load function to load the contents of a specific folder. This function leaves the file open for further load attempts. If the filename not found and there is a filename.lzma file, this function extracts the compressed file and tries to load uncompressed version. @throws LoadError @throws runtime_error

##### `createfilereader(filename)`

**Returns:** ``

##### `load(false, true)`

**Returns:** ``

##### `Save(const std::string &filename)`

**Returns:** `void`

Saves this file to the disk using the given filename. This operation will over write if the file exists. May throw WriteError

##### `save(—)`

**Returns:** ``

##### `Self(—)`

**Returns:** `std::weak_ptr<File>`

Loads a resource object from the given file, GID and size. This function may return nullptr in cases that the object cannot be loaded or no loader exists for the given gid. Both cases will throw in debug mode. Also handles SGuid and name @warning This function is intended to be used while loading a resource. It can be used for any purpose, however, would not be very useful outside its prime use Loads a resource object from the given file, GID and size. This function may return nullptr in cases that the object cannot be loaded or no loader exists for the given gid. Both cases will throw in debug mode. @warning This function is intended to be used while loading a resource. It can be used for any purpose, however, would not be very useful outside its prime use Returns a weak reference to this file. This returned reference can then be used to test if this object is still in memory.

##### `load(bool first, bool shallow)`

**Returns:** `void`

Resource Loaders. You may add or remove any loaders that is necessary. Initially a file loads all internal resources. **INTERNAL**, allows guid to object mapping. This information is not kept fresh about changes in the tree. This information is used for link and object tracking and is consumed right after file is loaded. This information is kept until a discard is issued. @warning Stale information. This is the actual load function

##### `save(—)`

**Returns:** `void`

This function performs the save operation

##### `createfilereader(std::string filename)`

**Returns:** `void`

The root folder, root changes while loading a file Type of the loaded file Keeps the file open even after loading is completed. This guarantees that the file is readable at a later point to read more data. Version of the loaded file. Currently there is only a single version. This version does not relate to the versions of the resources in the resource file. The reader that would be used to read the file


---

## Functions

### `if(gid==GID::SGuid)`

**Returns:** ``



### `if(gid==GID::Name)`

**Returns:** `else`



### `ASSERT(reader, "Reader is not open")`

**Returns:** ``



### `for(auto &loader : Loaders)`

**Returns:** ``



### `if(loader.second.GID==gid)`

**Returns:** ``



### `ASSERT(reader, "Reader is not open")`

**Returns:** ``



### `for(auto &loader : Loaders)`

**Returns:** ``



### `if(loader.second.GID==gid)`

**Returns:** ``



### `LoadError(LoadError::FileCannotBeOpened)`

**Returns:** `throw`



### `LoadError(LoadError::Signature)`

**Returns:** `throw`



### `LoadError(LoadError::VersionMismatch)`

**Returns:** `throw`



### `LoadError(LoadError::Containment)`

**Returns:** `throw`



### `if(!root)`

**Returns:** ``



### `LoadError(LoadError::Containment)`

**Returns:** `throw`



### `catch(...)`

**Returns:** ``



### `ifile(filename+".lzma", std::ios::binary)`

**Returns:** `std::ifstream`



### `ofile(filename, std::ios::binary)`

**Returns:** `std::ofstream`



### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``


Writes the start of an object. Should have a matching WriteEnd with the returned marker.


### `WriteChunkSize(-1)`

**Returns:** ``



### `WriteGID(GID::SGuid)`

**Returns:** ``



### `WriteChunkSize(0x08)`

**Returns:** ``



### `WriteGID(GID::Name)`

**Returns:** ``



### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``


Writes the start of an object. Should have a matching WriteEnd with the returned marker. This variant allows a replacement GID.


### `WriteGID(type)`

**Returns:** ``



### `WriteChunkSize(-1)`

**Returns:** ``



### `WriteGID(GID::SGuid)`

**Returns:** ``



### `WriteChunkSize(0x08)`

**Returns:** ``



### `WriteGID(GID::Name)`

**Returns:** ``


