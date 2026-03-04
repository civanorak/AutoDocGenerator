# IOption

> Auto-generated documentation for the **IOption** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `IOption`

**Namespace:** `gge`

#### Methods

##### `Check(—)`

**Returns:** `void`

##### `bool(—)`

**Returns:** `operator`

##### `T_(—)`

**Returns:** `operator`

##### `virtual` `Uncheck(—)`

**Returns:** `virtual void`

##### `setgroup(IOptionGroup<T_> *grp)`

**Returns:** `void`

##### `virtual` `setState(const bool &state)`

**Returns:** `virtual void`

##### `virtual` `getState(—)`

**Returns:** `virtual bool`

##### `virtual` `setText(const std::string &text)`

**Returns:** `virtual void`

##### `virtual` `getText(—)`

**Returns:** `virtual std::string`


### `IOptionGroup`

**Namespace:** `gge`

#### Methods

##### `virtual` `Remove(IOption<T_> *)`

**Returns:** `virtual void`

##### `virtual` `SetToNext(—)`

**Returns:** `virtual void`

##### `virtual` `SetToPrev(—)`

**Returns:** `virtual void`


### `OptionGroup`

**Namespace:** `gge`

#### Methods

##### `virtual` `Add(O_ &option)`

**Returns:** `virtual void`

##### `Add(O_ *option)`

**Returns:** `void`

##### `Add(*option)`

**Returns:** ``

##### `Add(option)`

**Returns:** ``

##### `virtual` `Remove(O_ &option)`

**Returns:** `virtual void`

##### `Remove(O_ *option)`

**Returns:** `void`

##### `Remove(*option)`

**Returns:** ``

##### `Remove(IOption<T_> *option)`

**Returns:** `void`

##### `Remove(*option)`

**Returns:** ``

##### `Remove(const T_ &value)`

**Returns:** `void`

##### `Remove(*option)`

**Returns:** ``

##### `T_(—)`

**Returns:** `operator`

##### `virtual` `Set(O_ *option)`

**Returns:** `virtual void`

##### `for(auto i=Options.First()`

**Returns:** ``

##### `ChangeEvent(option->Value)`

**Returns:** ``

##### `Set(O_ &option)`

**Returns:** `void`

##### `Set(&option)`

**Returns:** ``

##### `Set(const T_ &value)`

**Returns:** `void`

##### `virtual` `SetToNext(—)`

**Returns:** `virtual void`

##### `if(currentoption==NULL)`

**Returns:** ``

##### `Set(*it)`

**Returns:** ``

##### `virtual` `SetToPrev(—)`

**Returns:** `virtual void`

##### `if(currentoption==NULL)`

**Returns:** ``

##### `Set(*it)`

**Returns:** ``

##### `virtual` `HasSelected(—)`

**Returns:** `virtual bool`

##### `virtual` `Get(—)`

**Returns:** `virtual T_`

##### `for(auto i=Options.First()`

**Returns:** ``

##### `for(auto i=Options.First()`

**Returns:** ``

##### `First(—)`

**Returns:** `typename utils::Collection<O_>::Iterator`

##### `Last(—)`

**Returns:** `typename utils::Collection<O_>::Iterator`

##### `begin(—)`

**Returns:** `typename utils::Collection<O_>::Iterator`

##### `end(—)`

**Returns:** `typename utils::Collection<O_>::Iterator`

##### `First(—)`

**Returns:** `typename utils::Collection<O_>::ConstIterator`

##### `Last(—)`

**Returns:** `typename utils::Collection<O_>::ConstIterator`

##### `begin(—)`

**Returns:** `typename utils::Collection<O_>::ConstIterator`

##### `end(—)`

**Returns:** `typename utils::Collection<O_>::ConstIterator`

##### `clearall(—)`

**Returns:** `void`

##### `for(auto i=Options.First()`

**Returns:** ``

##### `option_changed(O_ &option)`

**Returns:** `void`

##### `Set(option)`

**Returns:** ``

