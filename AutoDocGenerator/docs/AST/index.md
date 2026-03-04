# AST

> Auto-generated documentation for the **AST** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `ASTNode`

**Namespace:** `Gorgon`


### `ASTCompiler`

**Namespace:** `Gorgon`

This node represents a literal. Literal member of ASTNode should be set. This node represents a function call. First element of the tree is the function to be called. Rest of the elements are used as parameter. If this is a member function call then the first child of this node should be a member node. Same as function call, this just calls method variant if it exists, if not it will print out return value of the function call. This node represents a membership. Membership should be parsed as left associative. This node is an identifier. This node represents a variable identifier This node represents an operator. All operators in GorgonScript are left associative and binary This node represents an indexing operation. Indexing operation can construct a new array if the first child is a type, otherwise it will return or assign to that index This node is a constructor node. The type of the object to be constructed can be set as Empty if the constructor is inside an Index node This node is a keyword call This node is an assignment. This node should be top level This node is empty, possibly a placeholder for an identifier List of expressions to be compiled Constructor requires the node type Duplicates this node Destroying a node destroys its children Type of the node Starting character of the node. Used for error locating Starting line of this ASTNode Textual data held by this node If node type is literal, this value will be used Leaves of this node

#### Methods

##### `Compile(ASTNode *tree)`

**Returns:** `unsigned`

AST compiler requires a vector of instructions. The compiler appends elements to the end of the list. However, it is important not to modify the list while IsReady function returns false. This function compiles given abstract syntax tree, returns the number of instructions generated. You should check IsReady function before using instructions. @param tree is the AST to be compiled

##### `IsReady(—)`

**Returns:** `bool`

If this function returns true, it is ok to use instructions from the list. A return value of false means not all instructions are fully completed. In these cases, more ASTs should be supplied to the compiler

##### `Finalize(—)`

**Returns:** `void`

##### `compilekeyword(ASTNode *tree, Byte &tempind)`

**Returns:** `bool`

##### `release(int start, int except=-1)`

**Returns:** `void`

##### `release(int start, Value except)`

**Returns:** `void`


### `scope`

**Namespace:** `Gorgon`


---

## Enums

### `NodeType`

**Namespace:** `Gorgon`

Node type


### `scopetype`

**Namespace:** `Gorgon`


---

## Functions

### `instructionlisttype("#instructionlist", "")`

**Returns:** `MappedReferenceType<std::vector<Instruction>, &ToEmptyString>`



### `dottree(ASTNode &tree, int &ind)`

**Returns:** `std::string`



### `switch(tree.Type)`

**Returns:** ``



### `for(auto &chld : tree.Leaves)`

**Returns:** ``



### `ASTToSVG(const std::string &line, ASTNode &tree, const std::vector<std::string> &last, bool show)`

**Returns:** `void`



### `for(auto &str : last)`

**Returns:** ``



### `if(i++)`

**Returns:** ``



### `temp("temp.dot")`

**Returns:** `std::ofstream`



### `PrintAST(ASTNode &tree)`

**Returns:** `void`



### `if(tree.Type==ASTNode::FunctionCall)`

**Returns:** ``



### `if(tree.Type==ASTNode::Construct)`

**Returns:** ``



### `if(tree.Type==ASTNode::Index)`

**Returns:** ``



### `for(auto &n : tree.Leaves)`

**Returns:** ``



### `PrintAST(n)`

**Returns:** ``



### `if(tree.Type==ASTNode::FunctionCall)`

**Returns:** ``



### `if(tree.Type==ASTNode::Construct)`

**Returns:** `else`



### `if(tree.Type==ASTNode::Index)`

**Returns:** `else`



### `compilevalue(ASTNode &tree, std::vector<Instruction> *list, Byte &tempind, bool generateoutput=true)`

**Returns:** `Value`



### `if(tree.Type==ASTNode::Operator)`

**Returns:** ``



### `if(tree.Type==ASTNode::Literal)`

**Returns:** ``



### `if(tree.Type==ASTNode::Identifier)`

**Returns:** ``



### `if(tree.Type==ASTNode::Variable)`

**Returns:** ``



### `if(tree.Type==ASTNode::FunctionCall || tree.Type==ASTNode::MethodCall)`

**Returns:** ``



### `if(tree.Leaves[0].Type==ASTNode::Identifier)`

**Returns:** ``



### `if(tree.Leaves[0].Type==ASTNode::Member)`

**Returns:** `else`



### `for(int i=1;i<tree.Leaves.GetCount()`

**Returns:** ``



### `if(tree.Type==ASTNode::Construct)`

**Returns:** ``



### `for(int i=0;i<tree.Leaves.GetCount()`

**Returns:** ``



### `if(tree.Type==ASTNode::Index)`

**Returns:** ``



### `for(int i=0;i<tree.Leaves.GetCount()`

**Returns:** ``



### `if(tree.Type==ASTNode::Member)`

**Returns:** ``



### `for(int i=start;i>=indstart;i--)`

**Returns:** ``



### `if(i!=except)`

**Returns:** ``



### `if(except.Type==ValueType::Temp)`

**Returns:** ``



### `release(start, except.Result)`

**Returns:** ``



### `release(start)`

**Returns:** ``



### `if(tree->Type==ASTNode::Assignment)`

**Returns:** ``



### `if(tree->Leaves[0].Type==ASTNode::Identifier || tree->Leaves[0].Type==ASTNode::Variable)`

**Returns:** ``



### `if(tree->Leaves[1].Type==ASTNode::Member)`

**Returns:** ``



### `if(tree->Leaves[0].Type==ASTNode::Member)`

**Returns:** `else`



### `if(tree->Leaves[0].Type==ASTNode::Index)`

**Returns:** `else`



### `for(int i=1; i<tree->Leaves[0].Leaves.GetSize()`

**Returns:** ``



### `ASSERT(false, "Assignment can only be performed to variable, membership and indexing nodes")`

**Returns:** ``



### `if(tree->Type==ASTNode::FunctionCall || tree->Type==ASTNode::MethodCall)`

**Returns:** `else`



### `if(tree->Type==ASTNode::Keyword)`

**Returns:** `else`



### `for(auto &p : tree->Leaves)`

**Returns:** ``



### `ASSERT(false, "Unknown top level AST Node")`

**Returns:** ``



### `release(tempind-1)`

**Returns:** ``



### `if(tree->Text=="if")`

**Returns:** ``



### `MissingParameterException("condition", 0, "Bool", "Condition for If keyword is not specified")`

**Returns:** `throw`



### `release(tempind-1, jf.RHS)`

**Returns:** ``



### `if(tree->Text=="else")`

**Returns:** `else`



### `FlowException("Else without If")`

**Returns:** `throw`



### `FlowException("Multiple Else for a single If")`

**Returns:** `throw`



### `if(tree->Text=="elseif")`

**Returns:** `else`



### `FlowException("ElseIf without If")`

**Returns:** `throw`



### `FlowException("ElseIf statements must be before Else statement")`

**Returns:** `throw`



### `MissingParameterException("condition", 0, "Bool", "Condition for ElseIf keyword is not specified")`

**Returns:** `throw`



### `release(tempind-1, jf.RHS)`

**Returns:** ``



### `if(tree->Text=="while")`

**Returns:** `else`



### `MissingParameterException("condition", 0, "Bool", "Condition for While keyword is not specified")`

**Returns:** `throw`



### `release(tempind-1, jf.RHS)`

**Returns:** ``



### `if(jf.RHS.Type==ValueType::Temp)`

**Returns:** ``



### `if(tree->Text=="for")`

**Returns:** `else`



### `ASSERT(tempind==indstart, "Some is wrong here")`

**Returns:** ``



### `if(val.Type!=ValueType::Temp)`

**Returns:** ``



### `for(int i=tempind-1;i>=indstart;i--)`

**Returns:** ``



### `release(tempind-2)`

**Returns:** ``



### `if(tree->Text=="break")`

**Returns:** `else`



### `for(auto it=scopes.rbegin()`

**Returns:** ``



### `if(it->type==scope::whilekeyword)`

**Returns:** ``



### `if(it->type==scope::forkeyword)`

**Returns:** `else`



### `if(supported==nullptr)`

**Returns:** ``



### `FlowException("Break without a breakable keyword scope")`

**Returns:** `throw`



### `if(tree->Text=="continue")`

**Returns:** `else`



### `for(auto it=scopes.rbegin()`

**Returns:** ``



### `if(it->type==scope::whilekeyword)`

**Returns:** ``



### `if(it->type==scope::forkeyword)`

**Returns:** `else`



### `if(supported==nullptr)`

**Returns:** ``



### `FlowException("Continue without a supported keyword scope")`

**Returns:** `throw`



### `if(tree->Text=="const")`

**Returns:** `else`



### `Compile(&tree->Leaves[0])`

**Returns:** ``



### `if(tree->Text=="static")`

**Returns:** `else`



### `if(tree->Text=="ref")`

**Returns:** `else`



### `if(tree->Text=="function" || tree->Text=="method")`

**Returns:** `else`



### `ASSERT(tree->Leaves[0].Type==ASTNode::Identifier, "Function names should be represented as identfiers")`

**Returns:** ``



### `if(tree->Leaves[1].Type==ASTNode::Identifier)`

**Returns:** ``



### `for(int i=2; i<tree->Leaves.GetSize()`

**Returns:** ``



### `if(p.defvaldata)`

**Returns:** ``



### `if(p.optdata)`

**Returns:** ``



### `for(auto &n : opts->Leaves)`

**Returns:** ``



### `if(scopes[i].type==scope::functionkeyword)`

**Returns:** ``



### `if(scopes[i].state>0)`

**Returns:** ``



### `if(tree->Text=="end")`

**Returns:** `else`



### `FlowException("`End` without a keyword scope")`

**Returns:** `throw`



### `for(unsigned i=1; i<elm; i++)`

**Returns:** ``



### `for(unsigned i=1; i<elm; i++)`

**Returns:** ``



### `ASTToSVG(const std::string &line, ASTNode &tree, const std::vector<std::string> &compiled={}, bool show=false)`

**Returns:** `void`


Converts given AST to an SVG file. This function requires GraphViz dot to be in path. The SVG will be saved as temp.dot.svg in the current directory. @param line the source code line @param tree to be converted @param compiled parameter can be used to add disassembly to the tree @param show if set, the generated SVG will be opened


### `PrintAST(ASTNode &tree)`

**Returns:** `void`


Recursively prints an AST

