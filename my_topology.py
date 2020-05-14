from mininet.topo import Topo
class my_topology(Topo):
	"11 Switches connected to 11 hosts."
		def __init__ (self):
			"create my topology"
			
			# Initialize topology
			Topo.__init__( self )
			# Adding Hosts
			Host1 = self.addHost('s1')
			Host2 = self.addHost('s2')
			Host3 = self.addHost('s3')
			Host4 = self.addHost('s4')
			Host5 = self.addHost('s5')
			Host6 = self.addHost('s6')
			Host7 = self.addHost('s7')
			Host8 = self.addHost('s8')
			Host9 = self.addHost('s9')
			Host10 = self.addHost('s10')
			Host11 = self.addHost('s11')
			# Adding Switches
			Switch1 = self.addSwitch('s1')
			Switch2 = self.addSwitch('s2')
			Switch3 = self.addSwitch('s3')
			Switch4 = self.addSwitch('s4')
			Switch5 = self.addSwitch('s5')
			Switch6 = self.addSwitch('s6')
			Switch7 = self.addSwitch('s7')
			Switch8 = self.addSwitch('s8')
			Switch9 = self.addSwitch('s9')
			Switch10 = self.addSwitch('s10')
			Switch11 = self.addSwitch('s11')
			
			# Adding Links
			self.addLink(Switch1, Switch2)
			self.addLink(Switch2, Switch3)
			self.addLink(Switch3, Switch4)
			self.addLink(Switch4, Switch5)
			self.addLink(Switch5, Switch6)
			self.addLink(Switch6, Switch7)
			self.addLink(Switch7, Switch8)
			self.addLink(Switch8, Switch9)
			self.addLink(Switch9, Switch10)
			self.addLink(Switch10, Switch11)
			
			self.addLink(Host1, Switch1)
			self.addLink(Host2, Switch2)
			self.addLink(Host3, Switch3)
			self.addLink(Host4, Switch4)
			self.addLink(Host5, Switch5)
			self.addLink(Host6, Switch6)
			self.addLink(Host7, Switch7)
			self.addLink(Host8, Switch8)
			self.addLink(Host9, Switch9)
			self.addLink(Host10, Switch10)
			self.addLink(Host11, Switch11)
			
topos = {'my_topology' : ( lambda:my_topology() )}			
			
		
