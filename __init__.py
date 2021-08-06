from mycroft import MycroftSkill, intent_file_handler


class SimpleYoutube(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('youtube.simple.intent')
    def handle_youtube_simple(self, message):
        query = message.data.get('query')

        self.speak_dialog('youtube.simple', data={
            'query': query
        })


def create_skill():
    return SimpleYoutube()

