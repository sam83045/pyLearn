class Sample:
    # For public fields/method no _
    pub_x = 10
    # For private fields/methods double __
    __priv_y = 20
    # For protected feilds/methods protected _
    _prot_z = 30

    def priv(self):
        return self.__priv_y

    priv2 = lambda self: self.__priv_y


s = Sample()
print(s.priv2())
