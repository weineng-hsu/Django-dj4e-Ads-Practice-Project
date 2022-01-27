import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Region, Iso, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name,description,justificaion, year, longtitude, latitude, area_hectares, category, state, region, iso

    for row in reader:
        print(row)

        category, created = Category.objects.get_or_create(name=row[7])
        category.save()
        state, created = State.objects.get_or_create(name=row[8])
        state.save()
        region, created = Region.objects.get_or_create(name=row[9])
        region.save
        iso, created = Iso.objects.get_or_create(name=row[10])
        iso.save
        try:
            y = int(row[3])
        except:
            y = None
        try:
            long = float(row[4])
        except:
            long = None
        try:
            lat = float(row[5])
        except:
            lat = None
        try:
            a = float(row[6])
        except:
            a = None
        site, created = Site.objects.get_or_create(name=row[0], desciption=row[1], justification=row[2], year=y, longtitude=long, latitude=lat, area_hectares=a, category=category, state=state, region=region, iso=iso)
        site.save()
