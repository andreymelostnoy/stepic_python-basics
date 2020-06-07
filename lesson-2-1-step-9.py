class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, element):
        if element > 0:
            x = super(PositiveList, self).append(element)
            return x
        else:
            raise NonPositiveError
