import lldb 


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f jprint.jprint jprint')


def jprint(debugger, command, result, internal_dict):
    set_expression = "po print(String(data: try! JSONSerialization.data(withJSONObject: %s, option: .prettyPrinted), encoding: .utf8)!)" % command
    debugger.HandleCommand(set_expression)
    return