from mako.template import Template
import io
from os import path

class BlueCli(object):
    def __init__(self):
        self.out_file=''

    def version(self):
        """
        $ python -m bluefn version
        :return:
        """
        from bluefn.version import __version__
        print(f".. blue-cli version: {__version__}")

    def gen(self, name):
        """
        $ bluefn gen Box
        :param name:
        :return:
        """
        from bluefn.cli.fixtures.contract_unitest import test_js_template
        mytemplate = Template(test_js_template)
        result=mytemplate.render(name=name)
        if self.out_file:
            with io.open(self.out_file, 'w', encoding="utf-8") as f:
                f.write(result)
                print('ok.')
        else:
            print(result)

    def gen_file(self, name):
        self.out_file=f"./test/{name}.test.js"
        if path.exists(self.out_file):
            print(f"{self.out_file} exists, doesn't overwrite it")
        else:
            self.gen(name)

    def eth_connected(self, test=True):
        from bluefn.eth.contract_loader import ContractLoader
        loader=ContractLoader(provider='tester' if test else 'local')
        return loader.connected

