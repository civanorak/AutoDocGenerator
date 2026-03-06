# PD

&gt; Auto-generated documentation for the **PD** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Token`

**Namespace:** `Compilers`

#### Methods

##### `GetLiteralValue(—)`

**Returns:** `const Data`

##### `switch(type)`

**Returns:** ``

##### `isliteral(—)`

**Returns:** `bool`

##### `switch(type)`

**Returns:** ``


### `opnode`

**Namespace:** `Compilers`


### `parenthesis`

**Namespace:** `Compilers`


---

## Enums

### `Type`

**Namespace:** `Compilers`


---

## Functions

### `isbreaker(char c)`

**Returns:** `bool`



### `switch(c)`

**Returns:** ``



### `isoperator(char c)`

**Returns:** `bool`



### `switch(c)`

**Returns:** ``



### `consumenexttoken(const std::string &input, int &index, bool expectop=false)`

**Returns:** `Token`



### `switch(c)`

**Returns:** ``



### `if(literalmarker=="" || literalmarker=="s")`

**Returns:** ``



### `if(literalmarker=="c")`

**Returns:** `else`



### `ParseError(ExceptionType::InvalidLiteral, "Literal 'c' is only valid for single character", index)`

**Returns:** `throw`



### `ParseError(ExceptionType::InvalidLiteral, "Unknown string literal: "+literalmarker, index)`

**Returns:** `throw`



### `if(specialident)`

**Returns:** ``



### `if(c == '-' && !expectop)`

**Returns:** `else`



### `if(c== '=')`

**Returns:** `else`



### `if(specialident)`

**Returns:** ``



### `if(numeric)`

**Returns:** `else`



### `if(literal=="i")`

**Returns:** ``



### `if(literal=="u")`

**Returns:** `else`



### `if(literal=="f")`

**Returns:** `else`



### `if(literal=="d")`

**Returns:** `else`



### `if(literal=="c")`

**Returns:** `else`



### `if(literal=="n")`

**Returns:** `else`



### `if(literal=="b")`

**Returns:** `else`



### `if(literal=="s")`

**Returns:** `else`



### `ParseError(ExceptionType::InvalidLiteral, "Unknown numeric literal: "+literal, index)`

**Returns:** `throw`



### `if(c == '.')`

**Returns:** `else`



### `if(flt)`

**Returns:** ``



### `if(opornumber)`

**Returns:** ``



### `if(oporequals)`

**Returns:** `else`



### `if(op || opornumber || oporequals)`

**Returns:** `else`



### `if(oporequals)`

**Returns:** `else`



### `if(acc == "true" || acc == "false")`

**Returns:** ``



### `if(t!=Token::Operator)`

**Returns:** ``



### `if(acc != "operator")`

**Returns:** ``



### `peeknexttoken(const std::string &input, int index)`

**Returns:** `Token`



### `consumenexttoken(input, index)`

**Returns:** `return`



### `testlexer(const std::string &input, std::ostream *cases)`

**Returns:** `void`



### `if(cases)`

**Returns:** ``



### `if(cases)`

**Returns:** ``



### `for(int j = 0; j < index; j++)`

**Returns:** ``



### `if(cases)`

**Returns:** ``



### `parseexpressions(const std::string &input, int &index)`

**Returns:** `Containers::Collection<ASTNode>`



### `if(token==Token::RightP || token==Token::RightCrlyP || token==Token::RightSqrP)`

**Returns:** ``



### `while(true)`

**Returns:** ``



### `if(token!=Token::Seperator)`

**Returns:** ``



### `if(token.type == Token::Identifier)`

**Returns:** ``



### `if(token==Token::LeftCrlyP)`

**Returns:** `else`



### `if(token!=Token::RightCrlyP)`

**Returns:** ``



### `while(1)`

**Returns:** ``



### `if(token==Token::Membership)`

**Returns:** ``



### `if(token!=Token::Identifier)`

**Returns:** ``



### `if(token==Token::LeftCrlyP)`

**Returns:** `else`



### `if(token!=Token::RightCrlyP)`

**Returns:** ``



### `if(token==Token::LeftSqrP)`

**Returns:** `else`



### `if(token!=Token::RightSqrP)`

**Returns:** ``



### `if(token==Token::LeftP)`

**Returns:** `else`



### `if(token!=Token::RightP)`

**Returns:** ``



### `for(auto &t : outputstack)`

**Returns:** ``



### `PrintAST(t)`

**Returns:** ``



### `for(auto &op : opstack)`

**Returns:** ``



### `while(true)`

**Returns:** ``



### `if(nextisop)`

**Returns:** ``



### `if(token==Token::Operator || token==Token::Identifier)`

**Returns:** ``



### `if(token==Token::Identifier)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `popoff()`

**Returns:** ``



### `if(token==Token::RightP && parcount)`

**Returns:** `else`



### `popoff()`

**Returns:** ``



### `if(token==Token::Identifier || token==Token::LeftCrlyP)`

**Returns:** `else`



### `if(token==Token::LeftP)`

**Returns:** `else`



### `if(token==Token::RightP)`

**Returns:** `else`



### `popoff()`

**Returns:** ``



### `fixconstructors(ASTNode *tree, ASTNode *parent=nullptr)`

**Returns:** `void`



### `if(tree->Type==ASTNode::Construct)`

**Returns:** ``



### `if(tree->Leaves[0].Type==ASTNode::Empty)`

**Returns:** ``



### `if(!parent || parent->Type!=ASTNode::Index)`

**Returns:** ``



### `for(auto &ASTNode : tree->Leaves)`

**Returns:** ``



### `fixconstructors(&ASTNode, tree)`

**Returns:** ``



### `checkvar(const std::string &text)`

**Returns:** `bool`



### `for(auto c : text)`

**Returns:** ``



### `checknewident(const std::string &text)`

**Returns:** `bool`



### `for(auto c : text)`

**Returns:** ``



### `if(!term)`

**Returns:** ``



### `ParseError(ExceptionType::UnexpectedToken, term->Text+" is not a valid identifier for "+keyword)`

**Returns:** `throw`



### `if(token!=Token::EqualSign)`

**Returns:** ``



### `ParseError(ExceptionType::UnexpectedToken, term->Text+" is not a valid variable name")`

**Returns:** `throw`



### `if(token!=Token::Identifier)`

**Returns:** ``



### `if(token.repr=="for")`

**Returns:** ``



### `if(tokenvar!=Token::Identifier)`

**Returns:** ``



### `if(token.repr=="call")`

**Returns:** `else`



### `if(root->Type!=ASTNode::FunctionCall)`

**Returns:** ``



### `if(token.repr=="function" || token.repr=="method")`

**Returns:** `else`



### `if(token==Token::LeftP)`

**Returns:** ``



### `consumenexttoken(input, index)`

**Returns:** ``



### `if(token!=Token::Identifier)`

**Returns:** ``



### `if(token!=Token::Identifier)`

**Returns:** ``



### `if(token!=Token::Identifier)`

**Returns:** ``



### `if(p.reference)`

**Returns:** ``



### `ParseError(ExceptionType::UnexpectedToken, "oneof statement cannot be used for references")`

**Returns:** `throw`



### `consumenexttoken(input, index)`

**Returns:** ``



### `if(token!=Token::LeftP)`

**Returns:** ``



### `if(token!=Token::RightP)`

**Returns:** ``



### `if(token==Token::EqualSign)`

**Returns:** ``



### `consumenexttoken(input, index)`

**Returns:** ``



### `if(token!=Token::RightP && token!=Token::Seperator)`

**Returns:** ``



### `if(token==Token::Seperator)`

**Returns:** ``



### `consumenexttoken(input, index)`

**Returns:** ``



### `if(token==Token::EoS)`

**Returns:** ``



### `if(ismethod)`

**Returns:** ``



### `if(ismethod)`

**Returns:** `else`



### `if(token!=Token::Identifier)`

**Returns:** ``



### `if(token!=Token::Identifier)`

**Returns:** ``



### `if(token!=Token::Identifier)`

**Returns:** ``



### `if(token.repr=="const" || token.repr=="static" || token.repr=="ref")`

**Returns:** `else`



### `assignment(nullptr, name)`

**Returns:** ``



### `if(token.repr=="using")`

**Returns:** `else`



### `if(astk==Token::EoS)`

**Returns:** ``



### `ParseError(ExceptionType::UnexpectedToken, "Expecting identifier for new name, found: "+astk.repr)`

**Returns:** `throw`



### `ParseError(ExceptionType::UnexpectedToken, "Expecting `as` or end of line, found: "+astk.repr)`

**Returns:** `throw`



### `if(token.repr=="source")`

**Returns:** `else`



### `if(token!=Token::String)`

**Returns:** ``



### `file(token.repr)`

**Returns:** `std::ifstream`



### `FileNotFoundException(token.repr)`

**Returns:** `throw`



### `Compile(line, linenr++)`

**Returns:** ``



### `catch(Exception &err)`

**Returns:** ``



### `while(token!=Token::EoS)`

**Returns:** ``



### `if(token==Token::Seperator)`

**Returns:** ``



### `consumenexttoken(input, index)`

**Returns:** ``



### `if(token==Token::EqualSign)`

**Returns:** ``



### `assignment(term, "")`

**Returns:** ``



### `if(term->Type==ASTNode::FunctionCall)`

**Returns:** `else`



### `fixconstructors(root)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `if(it->pos<ch)`

**Returns:** ``



### `for(unsigned i=0;i<len;i++)`

**Returns:** ``



### `if(inquotes)`

**Returns:** ``



### `if(escape==1)`

**Returns:** ``



### `if(escape==2)`

**Returns:** `else`



### `if(c=='\\')`

**Returns:** `else`



### `if(inquotes==1 && c=='\'')`

**Returns:** `else`



### `if(inquotes==2 && c=='"')`

**Returns:** `else`



### `if(c=='\'')`

**Returns:** `else`



### `if(c=='"')`

**Returns:** `else`



### `if(c=='#')`

**Returns:** `else`



### `if(c==';')`

**Returns:** `else`



### `transformpos(i, cline, cchar)`

**Returns:** ``



### `if(cline!=pline)`

**Returns:** ``



### `if(c=='(' || c=='[' || c=='{')`

**Returns:** `else`



### `if(error)`

**Returns:** ``



### `transformpos(i, cline, cchar)`

**Returns:** ``



### `if(cutfrom==-1)`

**Returns:** ``



### `if(clearafter!=-1)`

**Returns:** ``



### `swap(prepared, input)`

**Returns:** ``



### `extractline(left, process)`

**Returns:** ``



### `catch(ParseError &ex)`

**Returns:** ``



### `transformpos(ex.Char, cline, cchar)`

**Returns:** ``



### `if(ret)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `if(showsvg__)`

**Returns:** ``



### `ASTToSVG(input, *ret, {}, true)`

**Returns:** ``



### `while(true)`

**Returns:** ``



### `if(it->pos==p)`

**Returns:** ``



### `for(auto &m : linemarkers)`

**Returns:** ``



### `if(showsvg__)`

**Returns:** ``



### `ASTToSVG(input, *ret, strlines, true)`

**Returns:** ``



### `Compile("", -1)`

**Returns:** ``


