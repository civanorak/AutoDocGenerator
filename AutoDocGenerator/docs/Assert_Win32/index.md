# Assert_Win32

> Auto-generated documentation for the **Assert_Win32** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `IMAGEHLP_MODULE64_V3`


### `IMAGEHLP_MODULE64_V2`


### `stackentry`

**Namespace:** `Utils`


### `Walker`

**Namespace:** `Utils`

#### Methods

##### `StackWalker(StackWalker::RetrieveVerbose | StackWalker::SymBuildPath)`

**Returns:** ``

##### `virtual` `OnOutput(LPCSTR text)`

**Returns:** `virtual void`

##### `virtual` `OnCallstackEntry(CallstackEntryType type, CallstackEntry &entry)`

**Returns:** `virtual void`


---

## Enums

### `CallstackEntryType`


---

## Functions

### `LoadModules()`

**Returns:** `BOOL`



### `OnSymInit(LPCSTR szSearchPath, DWORD symOptions, LPCSTR szUserName)`

**Returns:** `virtual void`



### `OnLoadModule(LPCSTR img, LPCSTR mod, DWORD64 baseAddr, DWORD size, DWORD result, LPCSTR symType, LPCSTR pdbName, ULONGLONG fileVersion)`

**Returns:** `virtual void`



### `OnCallstackEntry(CallstackEntryType eType, CallstackEntry &entry)`

**Returns:** `virtual void`



### `OnDbgHelpErr(LPCSTR szFuncName, DWORD gle, DWORD64 addr)`

**Returns:** `virtual void`



### `OnOutput(LPCSTR szText)`

**Returns:** `virtual void`



### `myReadProcMem(HANDLE hProcess, DWORD64 qwBaseAddress, PVOID lpBuffer, DWORD nSize, LPDWORD lpNumberOfBytesRead)`

**Returns:** `static BOOL __stdcall`



### `strcpy_s(szDest, nMaxDestSize, szSrc)`

**Returns:** ``



### `strncpy_s(szDest, nMaxDestSize, szSrc, nMaxDestSize)`

**Returns:** ``



### `pSC(m_hProcess)`

**Returns:** ``



### `FreeLibrary(m_hDbhHelp)`

**Returns:** ``



### `free(m_szSymPath)`

**Returns:** ``



### `FreeLibrary(m_hDbhHelp)`

**Returns:** ``



### `GetUserNameA(szUserName, &dwSize)`

**Returns:** ``



### `FreeLibrary(hToolhelp)`

**Returns:** ``



### `FreeLibrary(hToolhelp)`

**Returns:** ``



### `CloseHandle(hSnap)`

**Returns:** ``



### `FreeLibrary(hToolhelp)`

**Returns:** ``



### `FreeLibrary(hPsapi)`

**Returns:** ``



### `pGMI(hProcess, hMods[i], &mi, sizeof mi)`

**Returns:** ``



### `pGMFNE(hProcess, hMods[i], tt, TTBUFLEN)`

**Returns:** ``



### `pGMBN(hProcess, hMods[i], tt2, TTBUFLEN)`

**Returns:** ``



### `free(vData)`

**Returns:** ``



### `GetModuleListPSAPI(hProcess)`

**Returns:** `return`



### `SetLastError(ERROR_DLL_INIT_FAILED)`

**Returns:** ``



### `SetLastError(ERROR_NOT_ENOUGH_MEMORY)`

**Returns:** ``



### `free(pData)`

**Returns:** ``



### `free(pData)`

**Returns:** ``



### `free(pData)`

**Returns:** ``



### `SetLastError(ERROR_DLL_INIT_FAILED)`

**Returns:** ``



### `free(m_szSymPath)`

**Returns:** ``



### `SetLastError(ERROR_DLL_INIT_FAILED)`

**Returns:** ``



### `SetLastError(ERROR_NOT_ENOUGH_MEMORY)`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, this->m_szSymPath)`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, ";")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, ".;")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, szTemp)`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, ";")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, szTemp)`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, ";")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, szTemp)`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, ";")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, szTemp)`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, ";")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, szTemp)`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, ";")`

**Returns:** ``



### `strcat_s(szTemp, nTempLen, "\\system32")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, szTemp)`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, ";")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, "SRV*")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, szTemp)`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, "\\websymbols")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, "*http://msdl.microsoft.com/download/symbols;")`

**Returns:** ``



### `strcat_s(szSymPath, nSymPathLen, "SRV*c:\\websymbols*http://msdl.microsoft.com/download/symbols;")`

**Returns:** ``



### `SetLastError(ERROR_DLL_INIT_FAILED)`

**Returns:** ``



### `SetLastError(ERROR_DLL_INIT_FAILED)`

**Returns:** ``



### `GET_CURRENT_CONTEXT(c, USED_CONTEXT_FLAGS)`

**Returns:** ``



### `SuspendThread(hThread)`

**Returns:** ``



### `ResumeThread(hThread)`

**Returns:** ``



### `MyStrCpy(csEntry.name, STACKWALK_MAX_NAMELEN, pSym->Name)`

**Returns:** ``



### `MyStrCpy(csEntry.lineFileName, STACKWALK_MAX_NAMELEN, Line.FileName)`

**Returns:** ``



### `MyStrCpy(csEntry.moduleName, STACKWALK_MAX_NAMELEN, Module.ModuleName)`

**Returns:** ``



### `MyStrCpy(csEntry.loadedImageName, STACKWALK_MAX_NAMELEN, Module.LoadedImageName)`

**Returns:** ``



### `SetLastError(ERROR_SUCCESS)`

**Returns:** ``



### `ResumeThread(hThread)`

**Returns:** ``



### `s_readMemoryFunction(hProcess, qwBaseAddress, lpBuffer, nSize, lpNumberOfBytesRead, s_readMemoryFunction_UserData)`

**Returns:** `return`



### `MyStrCpy(entry.name, STACKWALK_MAX_NAMELEN, entry.undName)`

**Returns:** ``



### `MyStrCpy(entry.name, STACKWALK_MAX_NAMELEN, entry.undFullName)`

**Returns:** ``



### `OnOutput(buffer)`

**Returns:** ``



### `OnOutput(buffer)`

**Returns:** ``



### `OnOutput(buffer)`

**Returns:** ``



### `if(walker.Stack[i].function!="")`

**Returns:** ``



### `for(int i=2;i<skip+2;i++)`

**Returns:** ``



### `report(i)`

**Returns:** ``



### `report(i)`

**Returns:** ``


