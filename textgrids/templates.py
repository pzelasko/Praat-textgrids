'''

  templates.py

  2019-07-15    Done.
  2019-08-02    Bug fix. Always TEXT_{LONG|SHORT}, never
                {LONG|SHORT}_TEXT.

'''

# Symbolic names for the formats

TEXT_LONG = 0
TEXT_SHORT = 1
BINARY = 2

# Formatting templates

long_header = '''File type = "ooTextFile"
Object class = "TextGrid"

xmin = {}
xmax = {}
tiers? <exists>
size = {}
item []:'''

short_header = '''File type = "ooTextFile"
Object class = "TextGrid"

{}
{}
<exists>
{}'''

long_tier = '''    item [{}]:
        class = "{}"
        name = "{}"
        xmin = {}
        xmax = {}
        {}: size = {}'''

short_tier = '''"{}"
"{}"
{}
{}
{}'''

long_point = '''        points [{}]:
            xpos = {}
            text = "{}"'''

short_point = '''{}
"{}"'''

long_interval = '''        intervals [{}]:
            xmin = {}
            xmax = {}
            text = "{}"'''

short_interval = '''{}
{}
"{}"'''
