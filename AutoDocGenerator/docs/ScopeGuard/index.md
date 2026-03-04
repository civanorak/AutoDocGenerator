# ScopeGuard

> Auto-generated documentation for the **ScopeGuard** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `ScopeGuard`

**Namespace:** `Gorgon`

#### Methods

##### `Disarm(—)`

**Returns:** `void`

Construct a scope guard with the given function Construct an empty scope guard Move constructor No copying Move assignment No copy assignment Disarm this scope guard, after this function it will not fire

##### `Arm(F_ &&value)`

**Returns:** `void`

Arms the scope guard with the given function.

##### `fn(—)`

**Returns:** ``

Destructor

