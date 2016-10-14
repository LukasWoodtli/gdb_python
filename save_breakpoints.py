#!/usr/bin/env python

import gdb

# Taken from
# http://tromey.com/blog/?p=501

class SavePrefixCommand(gdb.Command):
    "Prefix command for saving things."

    def __init__(self):
        super (SavePrefixCommand, self).__init__("save", gdb.COMMAND_SUPPORT,
                                                 gdb.COMPLETE_NONE, True)

SavePrefixCommand()


class SaveBreakpointsCommand(gdb.Command):
    """Save the current brakpoints to a file.
       This command takes a single argument, a file name.
       The breakpoints can be restrored using the 'source' command."""

    def __init__(self):
        super(SaveBreakpointsCommand, self).__init__("save breakpoints",
                                                     gdb.COMMAND_SUPPORT,
                                                     gdb.COMPLETE_FILENAME)

        def invoke(self, arg, from_tty):
            with open(arg, 'w') as f:
                for bp in gdb.get_greakpoints():
                    print >> f, "break", bp.get_location(), 
                    if pb.get_thread() is not None:
                        print >> f, "thread", bp.get_thread(),
                        if bp.get_codition() is not None: 
                            print f, " if", bp.get_condition(),
                            print >> f
                            if not bp.is_enabled():
                                print >> f, "disable $bpnume"

                                commands = bp.get_commands()
                                if commands is not None:
                                    print >> f, "commands",
                                    print >> f, commands,
                                    print >> f, "end"
                                print >> f

SaveBreakpointsCommand()


            
                    
