from abc import ABC,abstractmethod

class Description:
    def __init__(self,description) -> None:
        self.__description=description

    def get_description(self):
        return self.__description


class Media(ABC):
    def __init__(self,title,duration) -> None:
        self.title=title
        self.duration=duration

    @abstractmethod
    def play(self):
        pass

    def info(self):
        print(f"Title: {self.title}duration: {self.duration} description{self.get_description()}")

class Music(Media,Description):
    def __init__(self,title,duration,description):
        Media.__init__(self,title,duration)
        Description.__init__(self,description)
    def play(self):
        print(f"Playing Music: {self.title}")

    def info(self):
        print(f"Title: {self.title}duration: {self.duration} description{self.get_description()}")

class Video(Media,Description):
    def __init__(self,title,duration,description):
        Media.__init__(self,title,duration)
        Description.__init__(self,description)
    def play(self):
        print(f"Playing Video{self.title}")
    def info(self):
        print(f"Title: {self.title}duration: {self.duration} description{self.get_description()}")

class AudioBook(Media,Description):
    def __init__(self,title,duration,description):
        Media.__init__(self,title,duration)
        Description.__init__(self,description)
    def play(self):
        print(f"Playing Audio Book: {self.title}")

    def info(self):
        print(f"Title: {self.title}duration: {self.duration} description{self.get_description()}")


class Library:
    def __init__(self) -> None:
        self.__media_item=[]
        self.__media_by_genre={}
        self.__genr=""

    def get_media_items(self):
        return self.__media_item
    
    def get_media_by_genre(self):
        return self.__media_by_genre

    def add_media(self,media):
        if isinstance(media,Music):
            self.__genr="Music"

        if isinstance(media,Video):
            self.__genr="Video"

        if isinstance(media,AudioBook):
            self.__genr='Audio Book' 

        self.__media_item.append(media)

        if self.__genr in self.__media_by_genre:
            self.__media_by_genre[self.__genr].append(media)

        else:
            self.__media_by_genre[self.__genr]=[media,]

class User(ABC):
    def __init__(self,name) -> None:
        self.__name=name

    @abstractmethod
    def play_media(self):
        pass

class FreeUser(User):
    def __init__(self, name) -> None:
        super().__init__(name)
    def play_media(self,library):
        for media in library.get_media_items():
            media.play()


class PremiumUser(User):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__favourite_genr= ""
    def set_favourite_genr(self,genr):
        self.__favourite_genr=genr

    def get_favourite_genr(self,genr):
        return self.__favourite_genr

    def play_media(self,library):
        if self.__favourite_genr in library.get_media_by_genr():
            for media in library.get_media_by_genr()[self.__favourite_genr]:
                media.play()

        else:
            print("Invallid gener Selected")
library=Library()

music1=Music("Music Track 1","3.45","Author: Phitrion")
music2=Music("Music Track 2","5.45","Author: Phitrion")

video=Video("video Track 1","45:67","Artist: T-Series" )
video.play()
audio1=AudioBook("AudioBook Track 1","29:00","Author: Programming Hero")
library.add_media(music1)
library.add_media(music2)
library.add_media(video)
library.add_media(audio1)


freeUser=FreeUser("Mahmud")
premiumuser=PremiumUser("sakib")
# freeUser.play_media(library)
# print(isinstance(video,Music))

