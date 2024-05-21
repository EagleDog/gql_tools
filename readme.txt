__gql_tools__
minimal graphql examples

1.
  Save your api_key
  in the /box folder.

2.
  Go into query.py and
  make the following line
  point to your gql file:

  query1 = open("gql/status.graphql", "r").read()

3.
  Run 'py query.py' from command line.
  Output appears in 'output.json'.