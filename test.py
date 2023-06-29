import financedatabase as fd

# Initialize the Equities database
equities = fd.Equities()

# Obtain all countries from the database
equities_countries = equities.options('country')

# Obtain all sectors from the database
equities_sectors = equities.options('sector')

# Obtain all industry groups from the database
equities_industry_groups = equities.options('industry_group')

# Obtain all industries from a country from the database
equities_germany_industries = equities.options('industry', country='Germany')

# Obtain a selection from the database
equities_united_states = equities.select(country="United States")

# Obtain a detailed selection from the database
equities_usa_consumer_electronics = equities.select(country="United States", industry="Consumer Electronics")

# Search specific fields from the database
equities_uk_biotech = equities.search(country='United Kingdom', summary='biotech', exchange='LSE')