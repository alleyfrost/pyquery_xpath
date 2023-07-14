from pyquery import PyQuery

class PyQuery(PyQuery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def xpath(self, xpath=None, namespaces=None):
        """
        >> h = '<a class="foo1"><span class="foo2"><span class="foo3">Hello</span></span></a>'
        >> d = PyQuery(h)
        >> d('a').xpath('.//span[@class="foo2"]')
        [<span.foo2>]
        >> d.xpath('//span[@class="foo2"]')('.foo3')
        [<span.foo3>]
        >> d.xpath('.//span[@class="foo2"]')('.foo1')
        []
        """
        namespaces_ = namespaces if namespaces else self.namespaces
        elements = []
        for tag in self:
            elements.extend(tag.xpath(xpath, namespaces = namespaces_))
        return self._copy(elements, parent=self)