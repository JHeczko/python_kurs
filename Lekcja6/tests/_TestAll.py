if __name__ == "__main__":
    import unittest

    # Załaduj testy z poszczególnych plików
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Dodaj testy z plików
    suite.addTests(loader.discover('.', pattern='TestPoints.py'))
    suite.addTests(loader.discover('.', pattern='TestRectangle.py'))
    suite.addTests(loader.discover('.', pattern='TestTriangle.py'))

    # Uruchom wszystkie zebrane testy
    runner = unittest.TextTestRunner()
    runner.run(suite)