#
# priority order of operators
#  
''' infix : X+y
porfix : xy+
prefix : +xy
no need paranthesis
no need associativity rules
can be evaluated.
precedence and associativity
infix :    x+y*z     (x+y)*z
prefix :   +x*yz     *+xyz
post fix : xyz*+     xy+z*
 
steps for PostFix Conversion
x+y*z =(x+(y*z))

steps for postfix conversion
x+y*z ==(x+(y*z))
        (x+(yz*))

Why Prefix/Postfix Exist (Exam + Industry Logic)

Remove ambiguity

Simplify expression evaluation

Used internally by compilers

Faster parsing and execution
'''

    
    
    