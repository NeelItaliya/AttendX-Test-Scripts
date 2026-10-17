
def login(username, password):
    if username == "":
        return "Username Required"
    elif username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Login Failed"


# Test Case 1: Valid login
assert login("admin", "1234") == "Login Successful"
print("Test 1 Passed: Valid Login")

# Test Case 2: Invalid password
assert login("admin", "wrong") == "Login Failed"
print("Test 2 Passed: Invalid Password")

# Test Case 3: Empty username
assert login("", "1234") == "Username Required"
print("Test 3 Passed: Empty Username")

print("All Login Tests Passed!")
