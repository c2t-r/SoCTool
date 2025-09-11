from .Proto import protobuf_pb2
from google.protobuf.message import Message
from google._upb._message import RepeatedCompositeContainer, RepeatedScalarContainer

protobuf = protobuf_pb2.protobuf()

def messageToObject(message):
    proto = {}
    for i in message.DESCRIPTOR.fields_by_name:
        data = getattr(message, i)

        if type(data) == RepeatedCompositeContainer:
            proto[i] = []
            for e in data:
                proto[i].append(messageToObject(e))
        elif type(data) == RepeatedScalarContainer:
            proto[i] = []
            for e in data:
                proto[i].append(e)
        else:
            if isinstance(data, Message):
                data = messageToObject(data)
            proto[i] = data
    return proto

def bytesToProto(bin: bytes):
    protobuf.ParseFromString(bin)
    proto = messageToObject(protobuf)

    protobuf.Clear()

    return proto
