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
        pass

class PersonModelTest(TestCase):
    def test_default_text(self):
        pass
