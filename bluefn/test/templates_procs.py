class TemplateProcs(object):
    def simple(self):
        """
        $ python -m bluefn.test.templates_procs simple
        :return:
        """
        from mako.template import Template

        mytemplate = Template("hello, ${name}!")
        print(mytemplate.render(name="jack"))

if __name__ == '__main__':
    import fire
    fire.Fire(TemplateProcs)

