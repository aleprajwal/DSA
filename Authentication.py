import string


class Authentication():
    """
    authenticate user with their username and password

    creating a sample authentication workflow: mapping username and password with a user list dictonary  
    """

    def __init__(self, username: string, password: string) -> None:
        self.username = username
        self.password = password

        self.user_list = {
            "admin" : "admin123",
            "zoe" : "mario2007",
            "evan" : "$superball"
        }

    def authentication(self) -> bool:
        if self.username in self.user_list and self.user_list[self.username] == self.password:
                return True
        return False


if __name__ == "__main__":
    username, password = ["admin", "admin123"]
    authentication = Authentication(username, password)          
    if authentication.authentication():
        print("logged in as {}".format(username))
    else:
        print("incorrect username or password")
        