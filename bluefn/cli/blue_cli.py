class BlueCli(object):
    def version(self):
        """
        $ python -m bluefn version
        :return:
        """
        from bluefn.version import __version__
        print(f".. blue-cli version: {__version__}")


