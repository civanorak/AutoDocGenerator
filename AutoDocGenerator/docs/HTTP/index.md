# HTTP

&gt; Auto-generated documentation for the **HTTP** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Error`

**Namespace:** `HTTP`


### `Nonblocking`

**Namespace:** `HTTP`

No error occurs, you should not be getting this. Given URL is malformed Cannot find the specified host Cannot connect to the specified host Access denied System run out of memory Cannot login to the given host Page not found An unknown error has occurred Constructor Destructor Error message text Error code

#### Methods

##### `Nonblocking(—)`

**Returns:** ``

##### `GetText(const std::string &URL)`

**Returns:** `void`

Executed when GetText operation is completed. Fired when GetData operation is completed. The given vector is temporary, it will be destroyed after used. You may swap its data if you need it Fired when GetFile operation is completed. Fired if an error occurs Requests text data from the given URL

##### `GetData(const std::string &URL)`

**Returns:** `void`

Requests data from the given URL

##### `GetData(const std::string &URL, std::vector<Byte> &vec)`

**Returns:** `void`

Requests data from the given URL. Received data will be stored in the supplied vector

##### `GetFile(const std::string &URL, const std::string &filename)`

**Returns:** `void`

Downloads the given URL to the supplied filename

##### `GetStream(const std::string &URL, std::ostream &stream)`

**Returns:** `void`

Streams the data to the given output stream.

##### `IsRunning(—)`

**Returns:** `bool`

Check if the process is still running

##### `deletevec(std::vector<Byte> *vec)`

**Returns:** `void`

##### `if(currentoperation!=OwnedData)`

**Returns:** ``

##### `operation(—)`

**Returns:** `void`

##### `stream(const std::string &URL, std::ostream &stream)`

**Returns:** `void`

##### `getdata(const std::string &URL, std::vector<Byte> &vec)`

**Returns:** `void`


---

## Enums

### `Code`

**Namespace:** `HTTP`

Code of the error


---

## Functions

### `Initialize()`

**Returns:** `void`



### `curl_global_init(CURL_GLOBAL_ALL)`

**Returns:** ``



### `stringwriter(void *ptr, size_t size, size_t nmemb, void *stream)`

**Returns:** `static size_t`



### `streamwriter(void *ptr, size_t size, size_t nmemb, void *stream)`

**Returns:** `static size_t`



### `vectorwriter(void *ptr, size_t size, size_t nmemb, void *vec)`

**Returns:** `static size_t`



### `translateerror(CURLcode res)`

**Returns:** `static Error`



### `switch(res)`

**Returns:** ``



### `BlockingGetText(const std::string &URL)`

**Returns:** `std::string`



### `Initialize()`

**Returns:** ``



### `ASSERT(curl_handle, "Cannot create curl handle. Initialization failed?")`

**Returns:** ``



### `curl_easy_setopt(curl_handle, CURLOPT_NOPROGRESS, 1L)`

**Returns:** ``



### `curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, stringwriter)`

**Returns:** ``



### `curl_easy_setopt(curl_handle, CURLOPT_FOLLOWLOCATION, 1L)`

**Returns:** ``



### `curl_easy_setopt(curl_handle, CURLOPT_FAILONERROR, 1L)`

**Returns:** ``



### `curl_easy_cleanup(curl_handle)`

**Returns:** ``



### `guard(mtx)`

**Returns:** `std::lock_guard<std::mutex>`



### `curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 1L)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, stringwriter)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_FAILONERROR, 1L)`

**Returns:** ``



### `stream(URL, tempfile)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 1L)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, &streamwriter)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_FAILONERROR, 1L)`

**Returns:** ``



### `if(currentoperation==Data)`

**Returns:** ``



### `getdata(URL, *tempvec)`

**Returns:** ``



### `if(currentoperation==Data)`

**Returns:** ``



### `getdata(URL, vec)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 1L)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, vectorwriter)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L)`

**Returns:** ``



### `curl_easy_setopt(curl, CURLOPT_FAILONERROR, 1L)`

**Returns:** ``



### `Initialize()`

**Returns:** ``



### `ASSERT(curl, "Cannot create curl handle. Initialization failed?")`

**Returns:** ``



### `guard(mtx, std::adopt_lock)`

**Returns:** `std::lock_guard<std::mutex>`



### `if(currentoperation!=None && !isrunning)`

**Returns:** ``



### `if(err.error!=0)`

**Returns:** ``



### `TransferErrorEvent(err)`

**Returns:** ``



### `switch(currentoperation)`

**Returns:** ``



### `TextTransferCompletedEvent(tempstr)`

**Returns:** ``



### `DataTransferCompletedEvent(*tempvec)`

**Returns:** ``



### `if(!isrunning)`

**Returns:** ``



### `DataTransferCompletedEvent(*tempvec)`

**Returns:** ``



### `if(!isrunning)`

**Returns:** ``



### `FileTransferCompletedEvent()`

**Returns:** ``



### `FileTransferCompletedEvent()`

**Returns:** ``



### `Initialize()`

**Returns:** `void`


Initializes HTTP networking system. It is called automatically


### `BlockingGetText(const std::string &URL)`

**Returns:** `std::string`


Requests a text from the URL. This function blocks the current thread and should not be preferred for text transfers over the internet as the UI will freeze while this fuınction is running.

