# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     def save(self, *args, **kwargs):
#         do_something()
#         super().save(*args, **kwargs)  # Call the "real" save() method.
#         do_something_else()


class one:
    def func1(self):
        pass

class two(one):
    def func1(self):
        do_something()
        super().func1()
        do_somethingelse()