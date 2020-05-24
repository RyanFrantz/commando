package main

# The app should be running as a non-privileged user.
# Test for a missing USER statement.
# Inspired by https://charlieegan3.com/posts/2019-12-05-rego-fun/
deny[msg] {
  count({command |
    command := input[i].Cmd
    command == "user"
  }) == 0

  msg = sprintf("Missing %s statement", ["USER"])
}

# Test that the defined user is 'commando'.
deny[msg] {
  input[i].Cmd == "user"
  val := input[i].Value
  not val == ["commando"]

  msg = sprintf("Expected USER value to be '%s'", ["commando"])
}
