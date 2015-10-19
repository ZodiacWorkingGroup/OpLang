# UniLang
A believable, imperative, non-C-family language.
## Introduction
UniLang, a badly-named esoteric programming language, is a programming language designed to believable (that is, it seems like something that the world could've seriously created given a slightly alien mindset, unlike esolangs such as Befunge or Malbolge) language outside of the C family. Whether or not I successfully made it believable is yet to be determined.

## Syntax
UniLang's syntax consists of a series of operation lines; lines consisting of 0-2 variables and one operator. Variables are of the form `/[a-zA-Z0-9_]+/ and operators are anything that isn't a variable (or a semicolon) The operation lines can be:
* Prefix: `+v`
* Postfix: `v+`
* Infix: `u+v`
* Padfix: `+v+`
* Nofix: `+`
(Note that in padfix, the two operations must be the same, making this language context-sensitive)

The effect of a line is determined by the variables at play (not their names, their values of course), the operator used, and the line's fixity.

Operation lines are separated by semicolons.

## Operators
What each operator does is a Work-in-progress. Operators are any unicode character that is not a variable. Every operator has a meaning in every fixity.

## Adapting for other (human) languages
To adapt UniLang to another human language, simply change the variable VARCHARS in the python script to be representative of the inside of a `[]` in a regex that should match the characters in your desired language. The script uses this to generate both the variable name regexes and the operator regexes. Adaptation: Complete!
