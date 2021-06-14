import json
WIKI = 'https://en.wikipedia.org/wiki/'


class CountriesLinks:
    def __init__(self, file, outfile):
        with open(file, 'r', encoding='utf-8') as counties_file:
            self.countries_dict = json.load(counties_file)
        self.outfile = outfile
        with open(self.outfile, 'w') as out:
            out.write('')

    def __iter__(self):
        return self

    def __next__(self):
        if not self.countries_dict:
            raise StopIteration
        country = self.countries_dict.pop(0)
        country_name = country['name']['official']
        country_link = WIKI + country_name.replace(' ', '_')
        with open(self.outfile, 'a', encoding='utf-8') as out:
            out.write(f'{country_name} - {country_link}\n')
        return f'{country_name} - {country_link}'


def main():
    for country in CountriesLinks('countries.json', 'output.txt'):
        print(country)


if __name__ == '__main__':
    main()
