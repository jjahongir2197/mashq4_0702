class Post:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.likes = 0

    def like(self):
        self.likes += 1


class User:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def create_post(self, text):
        p = Post(self.name, text)
        self.posts.append(p)
        return p


class SocialNetwork:
    def __init__(self):
        self.users = []

    def add_user(self, u):
        self.users.append(u)

    def feed(self):
        for u in self.users:
            for p in u.posts:
                print(f"{p.author}: {p.text} ❤️ {p.likes}")


sn = SocialNetwork()
u1 = User("Ali")
u2 = User("Jahongir")

sn.add_user(u1)
sn.add_user(u2)

p1 = u1.create_post("Hello world")
p1.like()
p1.like()

sn.feed()
