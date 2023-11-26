class MobilePhone:
    # constructor
    def __init__(self, manufactured, screen_size, num_cores, status = 0):
        self.__manufactured = manufactured
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = ["basicGim", "clock", "navig"]
        self.status = status
        
        
    """ @property
    def manufactured(self):
        #print('inside the getter')
        return self.hidden_manufactured
    
    @manufactured.setter
    def manufactured(self, manufactured):
        #print('inside the setter')
        self.hidden_manufactured = manufactured
    """
    # metodos
    def install_apps(self, *apps_for_install):
        for app in apps_for_install:
            self.apps.append(app)
            
    def uninstall_apps(self, app):
        uninstall = ""
        if app in self.apps:
            self.apps.pop(app)
            uninstall = f"app {app} desinstalada correctamente"
        else:
            uninstall = f"app {app} no esta en este disp."
        print(uninstall)
    def get_apps(self):
        return self.apps
    def power_on(self):
        self.status = 1
        return self.status
    def power_off(self):
        self.status = 0
        return self.status
    def get_status(self):
        if self.status == 0:
            result = "apagado"
        else:
            result = "encendido"
        return self.status
    def getManufactured(self):
        return self.__manufactured
    