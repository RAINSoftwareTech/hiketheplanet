#!/bin/bash
function pause(){
   read -p "Press Enter to continue testing or Ctrl+c to quit"
}

find . -type f -name '*.pyc' -delete

coverage run --source=equipment --omit="*/migrations*" manage.py test equipment.tests --settings=Hiking.settings.tests
coverage report -m
pause

coverage run --source=hazards --omit="*/migrations*" manage.py test hazards.tests --settings=Hiking.settings.tests
coverage report -m
pause

coverage run --source=hikers --omit="*/migrations*" manage.py test hikers.tests --settings=Hiking.settings.tests
coverage report -m
pause

coverage run --source=hikes --omit="*/migrations*" manage.py test hikes.tests --settings=Hiking.settings.tests
coverage report -m
pause

coverage run --source=reviews --omit="*/migrations*" manage.py test reviews.tests --settings=Hiking.settings.tests
coverage report -m
pause

coverage run --source=search --omit="*/migrations*" manage.py test search.tests --settings=Hiking.settings.tests
coverage report -m
pause

coverage run --source=sights --omit="*/migrations*" manage.py test sights.tests --settings=Hiking.settings.tests
coverage report -m
pause

coverage run --source=core manage.py test core.tests --settings=Hiking.settings.tests
coverage report -m
pause

coverage run --source=middleware manage.py test middleware.tests --settings=Hiking.settings.tests
coverage report -m
pause

coverage run --source=mixins manage.py test mixins.tests --settings=Hiking.settings.tests
coverage report -m

flake8 --exclude='*zjunk/*' ../hiketheplanet/
