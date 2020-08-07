"""
$ python simple_c.py
"""
from bluefn.cloud import simple

class SimpleCli(object):
    def invoke(self):
        """
        $ python -m bluefn.cloud.simple_c invoke
        :return:
        """
        result = simple.add.delay(4, 4)
        rd=result.get(timeout=1)
        print(rd)

if __name__ == '__main__':
    import fire
    fire.Fire(SimpleCli)


