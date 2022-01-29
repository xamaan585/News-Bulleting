class Article:
    '''
    Article class to define article objects
    '''
    def __init__(self,image,title,author,description,time,url):
        self.image = image
        self.title = title
        self.author = author
        self.description = description
        self.time = time
        self.url = url