import base64
import urllib.parse
from google.protobuf.message import DecodeError
from google.protobuf import descriptor_pool, descriptor_pb2, message_factory

# OTP migration URL
url = "otpauth-migration://offline?data=CkAKCmI8RGRhQElNNm8SClJBTUtJTUFLRVIaC0JoYXJhdGhleGltIAEoATACQhNhM2U0MTYxNzQ1ODQwOTI5MTc0EAIYASAA"

# Extract and decode the base64 data
data_b64 = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)['data'][0]
raw_data = base64.urlsafe_b64decode(data_b64)

# Define the protobuf schema using descriptors
pool = descriptor_pool.Default()
file_desc_proto = descriptor_pb2.FileDescriptorProto()
file_desc_proto.name = 'otp_migration.proto'
file_desc_proto.package = 'migration'
file_desc_proto.syntax = 'proto2'

# Define MigrationPayload and nested OTPParameters
file_desc_proto.message_type.add(
    name='MigrationPayload',
    field=[
        descriptor_pb2.FieldDescriptorProto(
            name='otp_parameters',
            number=1,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_REPEATED,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE,
            type_name='OTPParameters'
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='version',
            number=2,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_INT32,
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='batch_size',
            number=3,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_INT32,
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='batch_index',
            number=4,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_INT32,
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='batch_id',
            number=5,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_INT32,
        ),
    ]
)

file_desc_proto.message_type.add(
    name='OTPParameters',
    field=[
        descriptor_pb2.FieldDescriptorProto(
            name='secret',
            number=1,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_REQUIRED,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_BYTES,
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='name',
            number=2,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_REQUIRED,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_STRING,
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='issuer',
            number=3,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_STRING,
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='algorithm',
            number=4,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_ENUM,
            type_name='Algorithm',
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='digits',
            number=5,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_ENUM,
            type_name='DigitCount',
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='type',
            number=6,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_ENUM,
            type_name='OTPType',
        ),
        descriptor_pb2.FieldDescriptorProto(
            name='counter',
            number=7,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_INT64,
        ),
    ]
)

# Add enums
for enum_name, values in {
    'Algorithm': ['ALGO_UNKNOWN', 'ALGO_SHA1', 'ALGO_SHA256', 'ALGO_SHA512', 'ALGO_MD5'],
    'DigitCount': ['DIGIT_COUNT_UNKNOWN', 'DIGIT_COUNT_SIX', 'DIGIT_COUNT_EIGHT'],
    'OTPType': ['OTP_TYPE_UNKNOWN', 'HOTP', 'TOTP'],
}.items():
    enum_type = file_desc_proto.enum_type.add()
    enum_type.name = enum_name
    for i, name in enumerate(values):
        enum_type.value.add(name=name, number=i)

# Register the schema and create a message class
pool.Add(file_desc_proto)
factory = message_factory.MessageFactory(pool)
MigrationPayload = factory.GetPrototype(pool.FindMessageTypeByName('migration.MigrationPayload'))

# Parse the payload
try:
    message = MigrationPayload.FromString(raw_data)
    for param in message.otp_parameters:
        print(f"Name   : {param.name}")
        print(f"Issuer : {param.issuer}")
        print(f"Secret : {base64.b32encode(param.secret).decode()}")
        print(f"Type   : {param.type}")
        print(f"Algo   : {param.algorithm}")
        print("-" * 40)
except DecodeError as e:
    print("Failed to decode payload:", e)
