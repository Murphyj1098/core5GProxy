from core.api.grpc import client
from core.api.grpc.wrappers import Position, Interface, Session, Node

def create_nr_ue(session: Session, id: int) -> Node:
    position = Position(x=100, y=100)
    node = session.add_node(id, position=position, name=f"nrUE{id}")
    return node

def create_gNB(session: Session, id: int) -> Node:
    position = Position(x=100, y=100)
    node = session.add_node(id, position=position, name=f"gNB{id}")
    return node

def create_proxy(session: Session, id: int) -> Node:
    position = Position(x=100, y=100)
    node = session.add_node(id, position=position, name=f"proxy")
    return node

def main():
    core = client.CoreGrpcClient()
    core.connect()
    session = core.create_session()

    core.start_session(session)
    

if __name__ == "__main__":
    main()
