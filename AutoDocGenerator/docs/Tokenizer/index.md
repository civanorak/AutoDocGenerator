# Tokenizer

> Auto-generated documentation for the **Tokenizer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `Tokenizer`

**Namespace:** `Gorgon`

Tokenizer is a forward iterator that tokenizes a given string. This class only supports single character delimeters, however, its possible to specify more than one delimeter.

#### Methods

##### `Next(—)`

**Returns:** ``

Creates an empty tokenizer. Effectively creates an end iterator. Creates a new tokenizer. @param  str string to be tokenized @param  delimeters is the delimeters to use while tokenizing

##### `Next(—)`

**Returns:** ``

Move to the next token

##### `Next(—)`

**Returns:** `void`

Move to the next token

##### `if(ind==text.npos)`

**Returns:** ``

##### `Current(—)`

**Returns:** `std::string`

Return the current token

##### `IsValid(—)`

**Returns:** `bool`

Return the current token Return the current token Return the current token Whether the iterator is valid (i.e. dereferencable)

##### `end(—)`

**Returns:** `const Tokenizer`

Compare two iterators, does not check if two iterators are identical. Compares only current positions and tokens Compare two iterators, does not check if two iterators are identical. Compares only current positions and tokens

