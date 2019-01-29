class Facebook(object):
    version = '1.2'

    def __init__(self):
        self.post = []

    def new_post(self, subject):
        self.post.append(subject)

# About Facebook class
facebook = Facebook()
print(facebook.version, facebook.post)

facebook.new_post('I am looking for new job!')

print(facebook.post)