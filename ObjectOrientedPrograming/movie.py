#initializing attributes (instance variables)
#costructor

#initializing instance variables constructor

#java(class name)
#javascript(constructor)
#python(__init__)
#it will call when object create
class Movie:

    title:str
    run_time:int
    rating:int
    director:str
    genre:str

    def set_Movie(self,title,run_time,rating,director,genre):

     self.title=title

     self.run_time=run_time

     self.rating=rating

     self.director=director

     self.genre=genre

    def display(self):

     print(self.title,self.run_time,self.rating,self.director,self.genre)

movie_instance1=Movie()

movie_instance2=Movie()

movie_instance1.set_Movie("ARM",2.45,7.7,"Jithin lal","Action Drama")

movie_instance2.set_Movie("KGF",2.50,8.5,"Prashanth Neel","Action Drama")

movie_instance1.display()

movie_instance2.display()