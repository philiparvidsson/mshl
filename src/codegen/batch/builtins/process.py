#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

var = None

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def emit_code(parser):
    global var
    if not var:
        var = parser.tempvar('string')
        code = (
'''
set {0}={0}

set {0}[exit]={0}[exit]
goto {0}[exit]_
:{0}[exit]
goto :eof
:{0}[exit]_

set {0}[exitCode]=0
'''.format(var.name))
        parser.emit(code, 'decl')

    parser.scope.declare_variable('process', 'variable').name = var.name
