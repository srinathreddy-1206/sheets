import unittest
import sheets
import datetime
class SheetsTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_object_creation(self):
        class Author(sheets.Row):
            name = sheets.StringColumn()
            birthdate = sheets.DateColumn()
            age = sheets.IntegerColumn()

        author = Author('Marty Alchin', '1981-12-17', '28')
        self.assertEqual(author.name, 'Marty Alchin')
        self.assertEqual(author.birthdate, datetime.date(1981,12,17))
        self.assertEqual(author.age, 28)
        author = Author('Marty Alchin', birthdate='1981-12-17', age='28')
        self.assertEqual(author.name, 'Marty Alchin')
        self.assertEqual(author.birthdate, datetime.date(1981,12,17))
        self.assertEqual(author.age, 28)
        author = Author('Marty Alchin', '1981-12-17', age='28')
        self.assertEqual(author.name, 'Marty Alchin')
        self.assertEqual(author.birthdate, datetime.date(1981,12,17))
        self.assertEqual(author.age, 28)
        author = Author(name='Marty Alchin', birthdate='1981-12-17', age='28')
        self.assertEqual(author.name, 'Marty Alchin')
        self.assertEqual(author.birthdate, datetime.date(1981,12,17))
        self.assertEqual(author.age, 28)
    def test_sample_csv_file_read(self):
        class Content(sheets.Row):
            chapter = sheets.IntegerColumn()
            title = sheets.StringColumn()
        with open('sample.csv', 'r') as f:
            print ('\n')
            for entry in Content.reader(f):
                print ("%s: %s" %(entry.chapter, entry.title))
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
