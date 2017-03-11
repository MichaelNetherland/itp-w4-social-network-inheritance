from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None
        if timestamp is None:
            self.timestamp = datetime.now()

  

    def set_user(self, user):
        self.user = user

#strftime("%A %d. %B %Y")
class TextPost(Post):  # Inherit properly
    def __init__(self,text, timestamp):
        super(TextPost,self).__init__(text, timestamp)
#'@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'
#dt.strftime("%A, %d. %B %Y %I:%M%p") -->'Tuesday, 21. November 2006 04:30PM'
    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp):
        super(PicturePost,self).__init__(text, timestamp)
        self.image_url = image_url
        
#'@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'
    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp):
        super(CheckInPost,self).__init__(text,timestamp)
        self.latitude = latitude
        self.longitude = longitude
        

#'@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp.strftime("%A, %b %d, %Y"))
