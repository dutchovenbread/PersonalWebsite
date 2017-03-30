from michael.models import Person, Education, Job

per = Person(firstName='Michael', lastName='Hunter', middleInitial='K')
jobs = [Job(employer='Lockheed Martin', endYear='2014',
            jobTitle='Staff Software Engineer', startYear='2002',
            person=per.id
            ),
        Job(employer='SES Corporation', endYear='present',
            jobTitle='Engineering Manager', startYear='2014',
            person=per.id
            )
        ]
jobs[0].save()
jobs[1].save()

edus = [Education(degree='Master of Science', major='Systems Engineering',
                    school='Missouri University of Science and Technology',
                    yearCompleted='2016',
                    person=per.id
                  ),
        Education(degree='Bachelor of Science', major='Computer Engineering',
                    school='University of Virginia',
                    yearCompleted='2002',
                    person=per.id
                  )

        ]
edus[0].save()
edus[1].save()