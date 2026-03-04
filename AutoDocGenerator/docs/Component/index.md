# Component

> Auto-generated documentation for the **Component** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `Component`

**Namespace:** `Gorgon`


### `ComponentStorage`

**Namespace:** `Gorgon`

Returns the template, component should have a template at all times This class stores component related data. It will be instantiated whenever a new template is instantiated and will be preserved even after the component is destroyed. This prevents constant construction and destruction of objects.

