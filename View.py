class LoginView:
    def display(self):
        # Display login interface
        pass
    def show_success_message(self, username, password):
        # Read username and password from file
        with open('user_data.txt', 'r') as f:
            for line in f:
                u, p = line.strip().split(',')
                if u == username and p == password:
                    print("Login successful!")
                    return
        # If the username or password is incorrect
        print("Invalid username or password")
        pass

    def show_error_message(self, username, password):
        # Read username and password from file
        with open('user_data.txt', 'r') as f:
            for line in f:
                u, p = line.strip().split(',')
                if u == username and p != password:
                    print("Invalid password")
                    return
        # If the username or password is incorrect
        print("Invalid username or password")

class RegisterView:
    def display(self):
        # Display register interface

        pass

class StudyRoomView:
    def display(self):
        # Display study room interface

        pass


class MaterialLibraryView:
    def display(self):
        # Display material library interface

        pass

class ChatView:
    def display(self):
        # Display chat interface pass

        pass




