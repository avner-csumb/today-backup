sandwich = [
                ["rye", "sourdough", "baguette"],
                [
                    ["ham", "salami", "turkey", "chicken"],
                    ["swiss", "munster", "cheddar"]
                ],
                ["mayo", "mustard", "tabasco"]
            ]


# print(sandwich[1][0][3])
# print(sandwich[2][2])

city_info = {'new_york' : { 'mayor' : "Bill DeBlasio",
                            'population' : 8406000,
                            'website' : "http://www.nyc.gov"
                            },
             'los_angeles' : { 'mayor' : "Eric Garcetti",
                            'population' : 3884307,
                            'website' : "http://www.lacity.org"
                            },
             'miami' : { 'mayor' : "Tomas Regalado",
                            'population' : 417650,
                            'website' : "http://www.miamigov.com"
                            },
             'chicago' : { 'mayor' : "Rahm Emanuel",
                            'population' : 2719000,
                            'website' : "http://www.cityofchicago.org/"
                            },
            'salinas' : {   'mayor' : 'Joe Gunter',
                            'population' : 157218,
                            'website' : 'http://cityofsalinas.org',
                            'parks': ['Central', 'Laurelwood', 'Toro']
                        }
        }

# print(city_info['los_angeles']['mayor'])
print(city_info['salinas']['parks'][2])
