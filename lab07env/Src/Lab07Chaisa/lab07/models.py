from django.db import models

# Create your models here.
class Simple(models.Model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')

    def __str__(self):
        return self.url
    
class DateExample(models.Model):
    the_date = models.DateTimeField()

class NullExample(models.Model):
    col = models.CharField(max_length=10, blank=True, null=True)

# One to Many RelationShip

class Language(models.Model):
    name = models.CharField(max_length=10)
    #Para Quary one to Many
    def __str__(self):
        return self.name

class FrameWork(models.Model):
    name = models.CharField(max_length=10)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)
    #Para Queary one to Many
    def __str__(self):
        return self.name
    
# Many to Many RelationShip

class Movie(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=20)
    movies = models.ManyToManyField(Movie)
    def __str__(self):
        return self.name
    
# Many to Many Query

#>>> Character.objects.filter(movies__name='Civil War')
#<QuerySet [<Character: Captain America>]>
#>>> Movie.objects.filter(character__name='Captain America')
#<QuerySet [<Movie: Avengers>, <Movie: Civil War>, <Movie: Winter Soldier>]>
#>>> captain_america = Character.objects.get(name='Captain America')
#>>> captain_america
#<Character: Captain America>
#>>> captain_america.movies.all()
#<QuerySet [<Movie: Avengers>, <Movie: Civil War>, <Movie: Winter Soldier>]>
#>>> avengers = Movie.objects.get(name='Avengers')
#>>> avengers.character_set.all()
#<QuerySet [<Character: Captain America>, <Character: Thor>]>
#>>> avengers = Movie.objects.get(name='Avengers')
#>>> avengers
#<Movie: Avengers>
#>>> avengers.character_set.all()
#<QuerySet [<Character: Captain America>, <Character: Thor>]>
#>>>