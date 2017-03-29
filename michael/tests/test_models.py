from michael.models import Person, Education, Job

from django.test import TestCase

class JobModelTest(TestCase):
    def test_default_text(self):
        job = Job()
        self.assertEqual(job.employer,'')
        self.assertEqual(job.endYear,'')
        self.assertEqual(job.jobTitle,'')
        self.assertEqual(job.startYear,'')

    def test_actual_text(self):
        job = Job(employer='Lockheed Martin', endYear='2014',
                  jobTitle='Staff Software Engineer', startYear='2002'
                  )
        self.assertEqual(job.employer,'Lockheed Martin')
        self.assertEqual(job.endYear,'2014')
        self.assertEqual(job.jobTitle,'Staff Software Engineer')
        self.assertEqual(job.startYear,'2002')

class EducationModelTest(TestCase):
    def test_default_text(self):
        edu = Education()
        self.assertEqual(edu.degree, '')
        self.assertEqual(edu.major,'')
        self.assertEqual(edu.school,'')
        self.assertEqual(edu.yearCompleted,'')

    def test_actual_text(self):
        edu = Education(degree='Master of Science', major='Systems Engineering',
                        school='Missouri University of Science and Technology',
                        yearCompleted='2016')
        self.assertEqual(edu.degree,'Master of Science')
        self.assertEqual(edu.major,'Systems Engineering')
        self.assertEqual(edu.school,'Missouri University of Science and Technology')
        self.assertEqual(edu.yearCompleted,'2016')

class PersonModelTest(TestCase):
    def test_default_text(self):
        person = Person()
        self.assertEqual(person.firstName,'')
        self.assertEqual(person.lastName,'')
        self.assertEqual(person.middleInitial,'')

    def test_actual_text(self):
        person = Person(firstName='Michael', lastName='Hunter', middleInitial='K')
        self.assertEqual(person.firstName,'Michael')
        self.assertEqual(person.lastName,'Hunter')
        self.assertEqual(person.middleInitial,'K')

