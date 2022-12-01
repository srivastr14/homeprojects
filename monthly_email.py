# import docx
import pandas as pd

df = pd.read_csv('monthly_jif.csv')
df = df.fillna('')

print(df)

# Concept: Take csv and make lists and then add as paragraphs (including adding "JIF: " and "Linked: ")
# This includes highlighting "JIF: number" in Green and red text for "linked: number", bold instrument/noninstrument, and hyperlinked doi
# Then separate by instrument and make note of any DOI above 25 as "Notable High Impact Papers this Month:"
# Other headers: "HFIR and SNS Instrument Publications" and "NScD Publications (including Accelerator Physics, Irradiation, Isotopes, Facility, and Staff publications)"

# Make sure to manually add two charts from https://snsapp1.sns.ornl.gov/xprod/f?p=133:19:104649382691778:::::