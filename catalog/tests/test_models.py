from django.test import TestCase
from catalog.models import Author

class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set non-modified object used by all test methods
        Author.objects.create(first_name = 'Boy', last_name = 'Key')

    def test_first_name_label(self):
        author = Author.objects.get(id = 1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id = 1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id = 1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id = 1)
        excepted_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEqual(excepted_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id = 1)
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')


    def test_last_name_label(self):
        author = Author.objects.get(id = 1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id = 1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_last_name_max_length(self):
        author = Author.objects.get(id = 1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)
#TODO: Need write tests for under classes
class BookModelTest(TestCase):
    pass

class GenreModelTest(TestCase):
    pass

class BookInstanceModelTest(TestCase):
    pass


    

    