
from pkg2.pkg3.test import multiplication

multiplication()


##################################################################################################################

from pkg2.pkg3 import test as t

obj=t.test()
obj.addition()

t.multiplication()
t.division()