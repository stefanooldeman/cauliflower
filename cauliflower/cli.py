import os
from cauliflower.service.cargo import CargoService

# here a dictionairy where the key matches the "subcommand name"
# containing for each item in the list of options
# tuple structure: (argument_name, corresponding_options)
commands = [
    ("cargo", {
        "description": "Cargo can get you a bunch \
                of data from point A to B",
        "help": "use this to import or export data"
    }),
    ("pattern", {
        "description": "",
        "help": "modify or add patterns in interactive mode"
    })]

options = {
    #note that eg. "choises": range(10) is not supported very well
    "cargo": [
        ('-action', {
            "metavar": "method",
            "help": "either `import` or `export`",
            "required": True
        }),
        ("--filename", {
            "metavar": "filename",
            "type": str,
            "help": "the location or destination for the cargo",
            "required": True
        })],
    "pattern": [
        ('-name', {
            "help": "the name of the pattern",
            "required": True,
            "type": str
        }),
        ("--add", {
            "help": "boolean flag, add a pattern in interaction session",
            "const": True,
            "default": False,
            "nargs": "?",
        })]}


def add_pattern(name):

    def multi_input(msg):
        print msg
        text = ""
        stopword = "Q"
        while True:
            line = raw_input()
            if line.strip() == stopword:
                break
            text += "%s\n" % line
        return text

    print "We are going to add the {} Pattern!".format(name)
    problem = multi_input("Add the problem description for {pattern_name} . \
            Type Q to end input.".format(pattern_name=name))
    solution = multi_input("Describe the solution {pattern_name} is solving. \
            Type Q to end input.".format(pattern_name=name))
    consequence = multi_input("""
    Describe the consequence of using {pattern_name}.
    Type Q to end input.
    """.format(pattern_name=name))


def pattern_handler(args):
    if args.add:
        add_pattern(args.name)


def cargo_handler(args):
    #TODO this should be moved to a config file
    dirlist = [os.path.dirname(__file__), os.pardir, 'var', 'data']
    varpath = os.path.abspath(os.sep.join(dirlist))

    c = CargoService(varpath)
    if args.action == 'export':
        c.do_export(args.filename)

    if args.action == 'import':
        c.do_import(args.filename)


def add_commands(parser):
    subparser_args = {
        "title": "The most commonly used cauliflower commands are:",
        "help": "see cauliflower <command> -h for more information",
        "description": None}

    subparser = parser.add_subparsers(**subparser_args)

    # define by which functions a cmd should be handled if aplicable
    hanlders = {
        "pattern": pattern_handler,
        "cargo": cargo_handler}

    subs_commands = dict()
    for (name, construct_args) in commands:
        cmd = subparser.add_parser(name, **construct_args)

        if name in hanlders:
            cmd.set_defaults(func=hanlders.get(name))

        # default to empty options
        for (cmd_option, option_args) in options.get(name, []):
            cmd.add_argument(cmd_option, **option_args)
        subs_commands[name] = cmd

    return parser
