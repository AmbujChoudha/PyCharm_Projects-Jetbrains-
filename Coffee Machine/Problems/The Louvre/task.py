class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


Title, artist, year_creation = input(), input(), input()

painting1 = Painting(Title, artist, year_creation)

print(f'"{painting1.title}" by {painting1.painter} ({painting1.year}) hangs in the Louvre.')