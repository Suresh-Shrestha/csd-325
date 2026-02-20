

def format_city_country(city, country, population=None, language=None):
    """Return formatted city information with optional population and language."""
    
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" -population {population}"

    if language:
        result += f", {language.title()}"

    return result
    
    
if __name__ == "__main__":
    # City, Country only
    print(format_city_country("santiago", "chile"))

    # City, Country, Population
    print(format_city_country("kathmandu", "nepal", 1000000))

    # City, Country, Population, Language
    print(format_city_country("tokyo", "japan", 14000000, "japanese"))
