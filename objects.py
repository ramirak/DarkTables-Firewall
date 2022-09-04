
class Host:
   
  def __init__(self, name, ip_addr):
    self.name = name
    self.ip_addr = ip_addr

  def getName(self):
    return self.name
    
  def getAddr(self):
    return self.ip_addr
    
class Service:
   
  def __init__(self, name, port, protocol):
    self.name = name
    self.port = port
    self.protocol = protocol
    
  def getName(self):
    return self.name
    
  def getPort(self):
    return self.port
    
  def getProtocol(self):
    return self.protocol
    
