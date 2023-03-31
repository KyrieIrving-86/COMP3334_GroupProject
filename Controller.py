import random
import re

class LoginController:
    def __init__(self, login_view, user_model):
        self.login_view = login_view
        self.user_model = user_model

    def login(self, username, password):
        # Handle login operation
        user = self.user_model.get_user_by_username(username)
        if user and user.check_password(password):
            self.login_view.show_success_message()
        else:
            self.login_view.show_error_message("Invalid username or password")
            # Reload the login view
            self.login_view.login_view()


class RegisterController:
    def __init__(self, register_view, user_model):
        self.register_view = register_view
        self.user_model = user_model

    def register(self, user_info):
        # Get user information
        real_name = user_info['real_name']
        id_card = user_info['id_card']
        verification_method = user_info['verification_method']
        phone_number = user_info.get('phone_number')
        email = user_info.get('email')

        # Check real name
        if not self.user_model.check_real_name(real_name):
            self.register_view.show_error_message("Invalid real name")
            return

        # Check ID card and account type
        account_type = None
        if self.user_model.check_student_id(id_card):
            account_type = 'student'
        elif self.user_model.check_teacher_id(id_card):
            account_type = 'teacher'
        elif self.user_model.check_admin_id(id_card):
            self.register_view.show_login_page()
            return
        else:
            self.register_view.show_error_message("Invalid ID card")
            return

        # Verify phone number or email
        if verification_method == 'phone':
            verification_code = self.generate_verification_code()
            self.register_view.show_phone_verification(verification_code)
            while True:
                code_input = self.register_view.get_verification_code()
                if code_input == verification_code:
                    break
                elif self.register_view.ask_resend_verification_code():
                    verification_code = self.generate_verification_code()
                    self.register_view.show_phone_verification(verification_code)
                else:
                    return
        elif verification_method == 'email':
            verification_code = self.generate_verification_code()
            self.register_view.show_email_verification(verification_code)
            while True:
                code_input = self.register_view.get_verification_code()
                if code_input == verification_code:
                    break
                elif self.register_view.ask_resend_verification_code():
                    verification_code = self.generate_verification_code()
                    self.register_view.show_email_verification(verification_code)
                else:
                    return

        # Set password
        while True:
            password = self.register_view.get_password()
            if not self.check_password_strength(password):
                self.register_view.show_error_message("Invalid password")
                continue
            confirm_password = self.register_view.get_confirm_password()
            if password != confirm_password:
                self.register_view.show_error_message("Passwords do not match")
                continue
            break

        # Add user to the model
        self.user_model.add_user(real_name, id_card, account_type, phone_number, email, password)

        # Show success message and go to personal information page
        self.register_view.show_success_message()
        self.register_view.show_personal_information_page()

    def generate_verification_code(self):
        # Generate a 6-digit verification code
        return str(random.randint(100000, 999999))

    def check_password_strength(self, password):
        # Check if the password meets the requirements
        if len(password) < 8 or len(password) > 16:
            return False
        if not re.search('[0-9]', password):
            return False
        if not re.search('[A-Z]', password):
            return False
        return True

class StudyRoomController:
    def __init__(self, study_room_view, study_record_model):
        self.study_room_view = study_room_view
        self.study_record_model = study_record_model

    def enroll(self, student_id, course_id):
        # Handle course enrollment operation
        pass

class MaterialLibraryController:
    def __init__(self, material_library_view, material_model):
        self.material_library_view = material_library_view
        self.material_model = material_model

    def upload(self, material_info):
        # Handle material upload operation
        pass

class ChatController:
    def __init__(self, chat_view, message_model):
        self.chat_view = chat_view
        self.message_model = message_model

    def send_message(self, message_info):
        # Handle message sending operation
        pass

class StudyController:
    def init(self, study_record_model):
        self.study_record_model = study_record_model

    def add_study_record(self, study_record_info):
        # Handle adding study record operation
        pass

    def query_study_record(self, student_id):
        # Handle querying study record operation
        pass

    def update_study_record(self, study_record_info):
        # Handle updating study record operation
        pass

    def delete_study_record(self, study_record_id):
        # Handle deleting study record operation
        pass

class UserController:
    def init(self, user_model):
        self.user_model = user_model

    def login(self, username, password):
        # Handle login operation
        pass

    def register(self, user_info):
        # Handle register operation
        pass

    def logout(self, user_id):
        # Handle logout operation
        pass

    def query_user_info(self, user_id):
        # Handle querying user information operation
        pass

    def update_user_info(self, user_info):
        # Handle updating user information operation
        pass






