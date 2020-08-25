import logging

logger = logging.getLogger(__name__)

class Backups(object):
    def get_files(self, dir='.'):
        import os
        result=[]
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".md") and not file.lower().endswith('readme.md'):
                    file_name=os.path.join(root, file)
                    result.append(file_name)
                    logger.info(f"file -> {file_name}")
        return result

    def scan_files(self, dir='.', zip=None):
        """
        $ python -m bluefn.tools.backups scan_files .
        $ python -m bluefn.tools.backups scan_files .. docs.zip
        $ python -m bluefn.tools.backups scan_files . docs_sagas.zip
        :param dir:
        :return:
        """
        import zipfile

        files=self.get_files(dir)

        if zip:
            ignore_files=[]
            with zipfile.ZipFile(zip, 'a') as file:
                for f in files:
                    print(f"write {f} ..")
                    try:
                        file.write(f)
                    except:
                        ignore_files.append(f)
            print('done.')
            if ignore_files:
                print(f"ignore files -> {ignore_files}")

if __name__ == '__main__':
    import fire
    fire.Fire(Backups)

