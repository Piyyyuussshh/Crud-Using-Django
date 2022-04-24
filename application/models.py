from django.db import models

catageroies = (
    ('horror','horror'),
    ('comedy','comedy'),
    ('sci-fi','sci-fi'),
    ('romantic','romantic'),
    ('technology','technology'),
    ('other','other')
)
# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.first_name

class Books(models.Model):
    bookId = models.IntegerField(primary_key=True)
    BookName = models.CharField(max_length=50)
    category = models.CharField(max_length=40,choices=catageroies,default='none')

    def __str__(self):
        return self.BookName

class Orders(models.Model):
    full_name = models.ForeignKey(Users,null=False,on_delete=models.CASCADE)
    Book = models.ForeignKey(Books,null=False,on_delete=models.CASCADE)
    orderId = models.IntegerField(primary_key=True)
    IssueDate = models.DateTimeField()
    returnDate = models.DateTimeField()
