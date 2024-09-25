is_morning = True
is_mother = True
is_asleep = False
answering_phone = True

if is_morning and not is_mother:
    answering_phone = False

if (is_asleep or not answering_phone):
    print("I'm not answering my phone")
else:
    print("I'm answering my phone")
