__gql_tools__
minimal graphql examples

Runs a Monday query
from the command line.


1.
  Save your api_key
  in the 'box' folder.

2.
  Save your query in
  the 'gql' folder.
  e.g. 'gql/progress.graphql'

3.
  Go into query.py and
  make the this line
  point to your gql file:

  query1 = open("gql/progress.graphql", "r").read()

4.
  Run 'py query.py' from command line.
  Output appears in 'output.json'.