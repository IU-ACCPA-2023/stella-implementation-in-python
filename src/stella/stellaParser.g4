parser grammar stellaParser;

options {
    tokenVocab = stellaLexer;
}

start_Program: x = program EOF;
start_Expr: x = expr EOF;
start_Type: x = stellatype EOF;

program:
    languageDecl (extensions += extension)* (decls += decl)*;

languageDecl: 'language' 'core' ';' # LanguageCore;

extension:
    'extend' 'with' extensionNames += ExtensionName (
        ',' extensionNames += ExtensionName
    )* ';' # AnExtension;

decl: (annotations += annotation)* 'fn' name = StellaIdent '(' (
        paramDecls += paramDecl (',' paramDecls += paramDecl)*
    )? ')' ('->' returnType = stellatype)? (
        'throws' throwType = stellatype
    )? '{' (localDecls += decl)* 'return' returnExpr = expr ';' '}' # DeclFun
    | 'type' name = StellaIdent '=' atype = stellatype ';'          # DeclTypeAlias;

annotation: 'inline' # InlineAnnotation;
paramDecl: name = StellaIdent ':' paramType = stellatype;

expr:
    // expr6
    expr_ = expr '.' label = StellaIdent # DotRecord
    | expr_ = expr '.' index = INTEGER   # DotTuple
    | 'true'                             # ConstTrue
    | 'false'                            # ConstFalse
    | n = INTEGER                        # ConstInt
    | name = StellaIdent                 # Var
    // expr
    | 'cons' '(' head = expr ',' tail = expr ')'                     # ConsList
    | 'List::head' '(' list = expr ')'                               # Head
    | 'List::isempty' '(' list = expr ')'                            # IsEmpty
    | 'List::tail' '(' list = expr ')'                               # Tail
    | 'succ' '(' n = expr ')'                                        # Succ
    | 'not' '(' expr_ = expr ')'                                     # LogicNot
    | 'Nat::pred' '(' n = expr ')'                                   # Pred
    | 'Nat::iszero' '(' n = expr ')'                                 # IsZero
    | 'fix' '(' expr_ = expr ')'                                     # Fix
    | 'Nat::rec' '(' n = expr ',' initial = expr ',' step = expr ')' # NatRec
    | 'fold' '[' type_ = stellatype ']' expr_ = expr                 # Fold
    | 'unfold' '[' type_ = stellatype ']' expr_ = expr               # Unfold
    // expr
    | fun = expr '(' (args += expr (',' args += expr)*)? ')' # Application
    // expr
    | expr '*' expr   # Multiply
    | expr 'and' expr # LogicAnd
    // expr
    | expr '+' expr                        # Add
    | expr 'or' expr                       # LogicOr
    | expr_ = expr 'as' type_ = stellatype # TypeAsc
    | 'fn' '(' (
        paramDecls += paramDecl (',' paramDecls += paramDecl)*
    )? ')' '{' 'return' returnExpr = expr ';' '}'       # Abstraction
    | '{' (exprs += expr (',' exprs += expr)*)? '}' # Tuple
    | 'record' '{' (
        bindings += binding (',' bindings += binding)*
    )? '}'                                            # Record
    | '<|' label = StellaIdent ('=' rhs = expr)? '|>' # Variant
    | 'match' expr '{' (
        cases += match_case (';' cases += match_case)*
    )? '}'                                         # match
    | '[' (exprs += expr (',' exprs += expr))? ']' # List
    // expr
    | left = expr '<' right = expr  # LessThan
    | left = expr '<=' right = expr # LessThanOrEqual
    | left = expr '>' right = expr  # GreaterThan
    | left = expr '>=' right = expr # GreaterThanOrEqual
    | left = expr '==' right = expr # Equal
    | left = expr '!=' right = expr # NotEqual
    // expr
    | 'if' condition = expr 'then' thenExpr = expr 'else' elseExpr = expr # If
    | 'let' var = StellaIdent '=' value = expr 'in' body = expr           # Let
    | '(' expr ')'                                                        # ParenthesisedExpr;

binding: name = StellaIdent '=' rhs = expr;

match_case: pattern '=>' expr;

pattern:
    '<|' label = StellaIdent ('=' pattern)? '|>'                # PatternVariant
    | '{' (patterns += pattern (',' patterns += pattern)*)? '}' # PatternTuple
    | 'record' '{' (
        patterns += labelledPattern (
            ',' patterns += labelledPattern
        )*
    )? '}'                                                      # PatternRecord
    | '[' (patterns += pattern (',' patterns += pattern)*)? ']' # PatternList
    | 'cons' '(' head = pattern ',' tail = pattern ')'          # PatternCons
    | 'false'                                                   # PatternFalse
    | 'true'                                                    # PatternTrue
    | n = INTEGER                                               # PatternInt
    | 'succ' '(' n = pattern ')'                                # PatternSucc
    | name = StellaIdent                                        # PatternVar
    | '(' pattern ')'                                           # ParenthesisedPattern;

labelledPattern: label = StellaIdent '=' pattern;

stellatype:
    'Bool'  # TypeBool
    | 'Nat' # TypeNat
    | 'fn' '(' (
        paramTypes += stellatype (',' paramTypes += stellatype)*
    )? ')' '->' returnType = stellatype                        # TypeFun
    | 'µ' var = StellaIdent '.' type_ = stellatype             # TypeRec
    | left = stellatype '+' right = stellatype                 # TypeSum
    | '{' (types += stellatype (',' types += stellatype))? '}' # TypeTuple
    | 'record' '{' (
        fieldTypes += recordFieldType (
            ',' fieldTypes += recordFieldType
        )*
    )? '}' # TypeRecord
    | 'variant' '{' (
        fieldTypes += variantFieldType (
            ',' fieldTypes += variantFieldType
        )*
    )? '}'                                                      # TypeVariant
    | '[' (types += stellatype (',' types += stellatype)*)? ']' # TypeList
    | 'Unit'                                                    # TypeUnit
    | name = StellaIdent                                        # TypeVar
    | '(' stellatype ')' # TypeParens;

recordFieldType: label = StellaIdent ':' type_ = stellatype;
variantFieldType: label = StellaIdent (':' type_ = stellatype)?;