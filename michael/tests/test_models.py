from michael.models import Person, Education, Job

from django.test import TestCase

class JobModelTest(TestCase):
    def test_default_text(self):
        job = Job()
        self.assertEqual(job.employer,'')
        self.assertEqual(job.endYear,'')
        self.assertEqual(job.jobTitle,'')
        self.assertEqual(job.startYear,'')

class EducationModelTest(TestCase):
    def test_default_text(self):
        edu = Education()
        self.assertEqual(edu.degree, '')
        self.assertEqual(edu.major,'')
        self.assertEqual(edu.school,'')
        self.assertEqual(edu.yearCompleted,'')

class PersonModelTest(TestCase):
    def test_default_text(self):
        person = Person()
        self.assertEqual(person.firstName,'')
        self.assertEqual(person.lastName,'')
        self.assertEqual(person.middleInitial,'')

