
class UserList:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        return self.repository.list()
        