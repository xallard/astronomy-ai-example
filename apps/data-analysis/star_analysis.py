# star_analysis.py
# Script for analyzing stellar data using Astropy

# could be part of a larger module for analyzing stellar data

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.io import fits
from astropy.table import Table


class StarAnalyzer:
    def __init__(self, fits_file):
        self.fits_file = fits_file
        self.star_data = None

    def load_data(self):
        """
        Load FITS file data into an Astropy table
        """
        with fits.open(self.fits_file) as hdul:
            self.star_data = Table(hdul[1].data)
        print("Data loaded successfully.")

    def calculate_coordinates(self):
        """
        Calculate and return the sky coordinates of stars
        """
        ra = self.star_data["ra"] * u.degree
        dec = self.star_data["dec"] * u.degree
        return SkyCoord(ra, dec, frame="icrs")

    def filter_by_brightness(self, min_brightness):
        """
        Filter and return stars above a certain brightness threshold
        """
        return self.star_data[self.star_data["brightness"] > min_brightness]


# Example usage
if __name__ == "__main__":
    analyzer = StarAnalyzer("path/to/your/fits/file.fits")
    analyzer.load_data()

    coordinates = analyzer.calculate_coordinates()
    print("Star Coordinates:", coordinates)

    bright_stars = analyzer.filter_by_brightness(min_brightness=10.0)
    print("Bright Stars:", bright_stars)

# In this script:

# Astropy is used to handle FITS files, a common format for astronomical data.
# The StarAnalyzer class provides functionalities to load star data, calculate their coordinates, and filter stars based on brightness.
# The example usage at the bottom demonstrates how to instantiate the class and use its methods.
# This script, part of the data-analysis application, would serve as a cornerstone for further stellar analysis and could be integrated with AI models for predictive analytics or pattern recognition within the broader Astronomy AI project.
