Cauliflower
==========

Pattern selector project to find a pattern for your problem

cauliflower is concise, structured from the inside and maybe complex. But its
beautiful form the outside. The Cauliflower its design is a natural phenomenon
which can be recognized in trees, clouds, coastlines and even galaxy clusters.
Therefore it is an analogy and represents an typically or common structure much
like an design pattern which provides common solutions to recurring problems.

inspiration: https://sites.google.com/site/societyofpatternstext/analogies

Trello board: https://trello.com/b/Pa2QD4Fb

### Examples for cauliflower CLI command

Add a pattern in interactive session:
`bin/cauliflower pattern -name <pattern-name> --add`

Import data:
`bin/cauliflower pattern -action import --file patterns.xml`

### Troubleshooting

1. *I get this error*
    No module named cauliflower.cli

please make sure you are in the correct directory:
`ls` should show something similar to:

    Makefile                README.md               bin
    cauliflower             docs                    test-requirements.txt   var

if the problem remains, try:
    export PYTHONPATH=$(pwd)


2. *I see no output for my program*

There is alwasy the help for the CLI:

    bin/cauliflower --help

In case of imports, ensure there is data in var/data, you could copy the test
data from here or build your own:
    cp cauliflower/tests/mocks/uploads/dummy_import.xml var/data/patterns.xml
The end result goes into var/pckldb/ for local usage

