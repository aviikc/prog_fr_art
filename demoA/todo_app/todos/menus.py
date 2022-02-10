class Menus:
    def main_menu(self):
        return """
        1.) Insert Note
        2.) Modify Note
        3.) Display Notes
        q/Q) Exit
        """

    def insert_note_menu(self):
        return """
        1.) Insert content for today's todos.
        2.) Insert content for tomorrow's todos.
        3.) Insert content for a particular date.
        4.) Previous Menu.
        """

    def modify_note_menu(self):
        return """
        1.) Modify content for today's todos.
        2.) Modify content for tomorrow's todos.
        3.) Modify content for a particular date.
        4.) Previous Menu.
        """

    def display_note_menu(self):
        return """
        1.) Display content for today's todos.
        2.) Display content for tomorrow's todos.
        3.) Display content for a particular date.
        4.) Display content for a range of dates.
        5.) Previous Menu.
        """