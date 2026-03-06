# Dialog

&gt; Auto-generated documentation for the **Dialog** module of the Gorgon C++ Game Engine.


## Contents

- [Enums](#enums)
- [Functions](#functions)

---

## Enums

### `CloseOption`

**Namespace:** `internal`

@endcond Allows specifying how the dialog can be closed without supplying a response.


---

## Functions

### `ShouldBeCollected(Widgets::DialogWindow &wind)`

**Returns:** `bool`



### `init()`

**Returns:** `void`



### `handledialogcopy(Input::Key key, float state, const std::string &message)`

**Returns:** `bool`



### `if(state == 1 && key == Input::Keyboard::Keycodes::C && Input::Keyboard::CurrentModifier == Input::Keyboard::Modifier::Ctrl)`

**Returns:** ``



### `attachdialogcopy(Widgets::DialogWindow *diag, const std::string &title, std::string message)`

**Returns:** `void`



### `if(markdown)`

**Returns:** ``



### `closethis(Widgets::DialogWindow *diag)`

**Returns:** `void`



### `negotiatesize(Widgets::DialogWindow *diag, Widget *text, bool allowshrink)`

**Returns:** `Geometry::Size`



### `for(int i=0; i<5; i++)`

**Returns:** ``



### `if(sz.Width >= maxw)`

**Returns:** ``



### `if(compact)`

**Returns:** ``



### `place(Widgets::DialogWindow *diag)`

**Returns:** `void`



### `closethis(diag)`

**Returns:** ``



### `attachdialogcopy(diag, title, message)`

**Returns:** ``



### `place(diag)`

**Returns:** ``



### `for(auto opt : options)`

**Returns:** ``



### `closethis(diag)`

**Returns:** ``



### `onselect(index)`

**Returns:** ``



### `if(close != CloseOption::None)`

**Returns:** ``



### `closethis(diag)`

**Returns:** ``



### `onselect(-1)`

**Returns:** ``



### `attachdialogcopy(diag, title, message)`

**Returns:** ``



### `for(auto &w : btnsarea)`

**Returns:** ``



### `place(diag)`

**Returns:** ``



### `MultipleChoiceIndex(title, message, {notext, yestext}, [onyes, onno, onclose](int ind)`

**Returns:** ``


Asks user to respond with yes or no, optionally with cancel


### `switch(ind)`

**Returns:** ``



### `onclose()`

**Returns:** ``



### `onno()`

**Returns:** ``



### `onyes()`

**Returns:** ``



### `MultipleChoiceIndex(title, message, {cancel== "" ? canceltext : cancel, confirm== "" ? oktext : confirm}, [onconfirm](int ind)`

**Returns:** ``



### `switch(ind)`

**Returns:** ``



### `onconfirm()`

**Returns:** ``



### `init()`

**Returns:** ``



### `if(close != CloseOption::None)`

**Returns:** ``



### `closethis(diag)`

**Returns:** ``



### `onselect(-1)`

**Returns:** ``



### `closethis(diag)`

**Returns:** ``



### `if(requireselection)`

**Returns:** ``



### `if(def == -1)`

**Returns:** ``



### `if(l)`

**Returns:** ``



### `place(diag)`

**Returns:** ``



### `SetCloseText(const std::string &value)`

**Returns:** `void`



### `SetOkText(const std::string &value)`

**Returns:** `void`



### `SetCancelText(const std::string &value)`

**Returns:** `void`



### `SetYesNoText(const std::string &yes, const std::string &no)`

**Returns:** `void`



### `GetOkText()`

**Returns:** `std::string`



### `GetCancelText()`

**Returns:** `std::string`



### `GetCloseText()`

**Returns:** `std::string`



### `init()`

**Returns:** `void`



### `handledialogcopy(Input::Key key, float state, const std::string &message)`

**Returns:** `bool`



### `closethis(Widgets::DialogWindow *diag)`

**Returns:** `void`



### `place(Widgets::DialogWindow *diag)`

**Returns:** `void`



### `ShowMessage(title, message, {}, buttontext)`

**Returns:** ``


Displays the given message in a message window, calls the given function when the window is closed Displays the given message in a message window, calls the given function when the window is closed


### `ShowMessage("", message, onclose)`

**Returns:** ``


Displays the given message in a message window, calls the given function when the window is closed


### `MultipleChoiceIndex("", message, options, onselect, close)`

**Returns:** ``


Asks a multiple choice question to the user with an optional close/cancel button. Useful for a few options Asks a multiple choice question to the user with an optional close/cancel button. Useful for a few options. Selection option index is passed to the onselect function. If close/cancel option is selected, -1 is passed to onselect. options are not needed after the function call and can be destroyed.


### `for(auto o : options)`

**Returns:** ``


Asks a multiple choice question to the user with an optional close/cancel button Useful for a few options. Option value is passed to onselect function. options must outlive the dialog. Use MultipleChoiceIndex if this is not practical.


### `MultipleChoiceIndex(title, message, options, [options, onselect, onclose](int ind)`

**Returns:** ``



### `if(ind == -1)`

**Returns:** ``



### `onclose()`

**Returns:** ``



### `onselect(options[ind])`

**Returns:** ``



### `MultipleChoiceIndex(title, message, options, [onselect, onclose](int ind)`

**Returns:** ``


Asks a multiple choice question to the user with an optional close/cancel button Useful for a few options. Option value is passed to onselect function. options must outlive the dialog. Use MultipleChoiceIndex if this is not practical. disallow passing temporary vectors. The vectors should outlive the dialog. Asks a multiple choice question to the user with an optional close/cancel button using the values from enumeration. Useful for a few options.


### `if(ind == -1)`

**Returns:** ``



### `onclose()`

**Returns:** ``



### `AskYesNo("", message, onyes, onno, close, onclose)`

**Returns:** ``


Asks a multiple choice question to the user with an optional close/cancel button Useful for few options Asks user to respond with yes or no, optionally with cancel Asks user to respond with yes or no, optionally with cancel


### `Confirm("", message, onconfirm, confirmtext, canceltext)`

**Returns:** ``


Asks user to confirm an action. There will be a cancel button to continue without confirming this dialog. Asks user to confirm an action. There will be a cancel button to continue without confirming this dialog.


### `SetCloseText(const std::string &value)`

**Returns:** `void`


Changes the text of the close button. This change will effect only future dialogs.


### `GetCloseText()`

**Returns:** `std::string`


Returns the text of the close button.


### `SetYesNoText(const std::string &yes, const std::string &no)`

**Returns:** `void`


Changes the text of the yes and no buttons. This change will effect only future dialogs.


### `SetOkText(const std::string &value)`

**Returns:** `void`


Changes the text of the ok button. This change will effect only future dialogs.


### `GetOkText()`

**Returns:** `std::string`


Returns the text of the ok button.


### `SetCancelText(const std::string &value)`

**Returns:** `void`


Changes the text of the cancel button. This change will effect only future dialogs.


### `GetCancelText()`

**Returns:** `std::string`


Returns the text of the cancel button.


### `init()`

**Returns:** ``


Requests an input from the user


### `if(close != CloseOption::None)`

**Returns:** ``



### `closethis(diag)`

**Returns:** ``



### `onclose()`

**Returns:** ``



### `closethis(diag)`

**Returns:** ``



### `onconfirm(*inp)`

**Returns:** ``



### `if(validate)`

**Returns:** ``



### `if(l)`

**Returns:** ``



### `place(diag)`

**Returns:** ``



### `Input(title, message, label, onconfirm, T_{}, validate, close, onclose, confirmtext, closetext)`

**Returns:** ``


Requests an input from the user


### `Input(title, message, "", onconfirm, def, validate, close, onclose, confirmtext, closetext)`

**Returns:** ``


Requests an input from the user


### `Input(title, message, "", onconfirm, T_{}, validate, close, onclose, confirmtext, closetext)`

**Returns:** ``


Requests an input from the user


### `Input("", message, "", onconfirm, def, validate, close, onclose, confirmtext, closetext)`

**Returns:** ``


Requests an input from the user


### `Input("", message, "", onconfirm, T_{}, validate, close, onclose, confirmtext, closetext)`

**Returns:** ``


Requests an input from the user


### `init()`

**Returns:** ``


Asks a select question to the user with a confirm button and  optional close/cancel button. MultipleChoiceIndex is a better fit if there are a few choices. Asks a select question to the user with a confirm button and  optional close/cancel button. MultipleChoiceIndex is a better fit if there are a few choices. Asks a select question to the user with a confirm button and  optional close/cancel button. MultipleChoiceIndex is a better fit if there are a few choices. Asks a select question to the user with a confirm button and  optional close/cancel button. MultipleChoiceIndex is a better fit if there are a few choices. If requireselection is false and user clicks on confirm, onclose will be called instead of onselect. Options vector is not needed and could be destroyed once the dialog is created.


### `if(close != CloseOption::None)`

**Returns:** ``



### `closethis(diag)`

**Returns:** ``



### `onclose()`

**Returns:** ``



### `closethis(diag)`

**Returns:** ``



### `onselect(*inp)`

**Returns:** ``



### `onclose()`

**Returns:** ``



### `if(requireselection)`

**Returns:** ``



### `if(def == -1)`

**Returns:** ``



### `if(l)`

**Returns:** ``



### `place(diag)`

**Returns:** ``


