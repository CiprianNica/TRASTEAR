
from clases import MobilePhone

#objetos
mobil_1 = MobilePhone("Nokia", 2345, 3)

print(mobil_1.get_status())
print(mobil_1.get_apps())
mobil_1.install_apps('app2')
mobil_1.uninstall_apps('app3')
        
