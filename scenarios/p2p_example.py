from core.api.grpc import client
from core.api.grpc.wrappers import Position

iface_helper = client.InterfaceHelper(ip4_prefix="10.0.0.0/24", ip6_prefix="2001::/64")

core = client.CoreGrpcClient()
core.connect()

session = core.create_session()

position = Position(x=100, y=100)
node1 = session.add_node(1, position=position)
position = Position(x=300, y=100)
node2 = session.add_node(2, position=position, name="OldName")

node2.name = "NewName"

iface1 = iface_helper.create_iface(node1.id, 0)
iface2 = iface_helper.create_iface(node2.id, 0)
session.add_link(node1=node1, node2=node2, iface1=iface1, iface2=iface2)

core.start_session(session)
