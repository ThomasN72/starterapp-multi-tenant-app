from tenant_app.models import Region, Member
from shared_app.models import Client
from django.db import connection

kaiser = Client.objects.get(schema_name="tenant1")

connection.set_schema(kaiser.schema_name)
washington_kaiser_region = Region.objects.create(name="Washington")
california_kaiser_region = Region.objects.create(name="California")

washington_kaiser_member = Member.objects.create(
    name="John",
    region=washington_kaiser_region,
)
washington_two_kaiser_member = Member.objects.create(
    name="Ashley",
    region=washington_kaiser_region,
)
california_kaiser_member = Member.objects.create(
    name="Mike",
    region=california_kaiser_region,
)


sutter = Client.objects.get(schema_name="tenant2")

connection.set_schema(sutter.schema_name)
new_york_sutter_region = Region.objects.create(name="New York")
california_sutter_region = Region.objects.create(name="California")

new_york_sutter_member = Member.objects.create(
    name="Henry",
    region=new_york_sutter_region,
)
new_york_two_sutter_member = Member.objects.create(
    name="Paul",
    region=new_york_sutter_region,
)
california_sutter_member = Member.objects.create(
    name="Matthew",
    region=california_sutter_region,
)