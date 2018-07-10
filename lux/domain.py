class About():
    '''
    Summary of this service
    '''

    def __init__(self):
        self.summary = "Hi my name is lux"


class Health():
    '''
    Summary of server health
    '''

    def __init__(self):
        self.status = 'UP'


class ChatMessage():
    '''
    A chat message
    '''

    def __init__(self, author="", text="", source=""):
        self.author = author
        self.text = text
        self.source = source
