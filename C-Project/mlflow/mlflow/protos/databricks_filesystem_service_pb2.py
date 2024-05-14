# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: databricks_filesystem_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import databricks_pb2 as databricks__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#databricks_filesystem_service.proto\x12\x11mlflow.filesystem\x1a\x10\x64\x61tabricks.proto\x1a\x15scalapb/scalapb.proto\")\n\nHttpHeader\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"`\n\x18\x43reateDownloadUrlRequest\x12\x0c\n\x04path\x18\x01 \x01(\t:6\xe2?3\n1com.databricks.rpc.RPC[CreateDownloadUrlResponse]\"\x82\x01\n\x19\x43reateDownloadUrlResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\x12.\n\x07headers\x18\x02 \x03(\x0b\x32\x1d.mlflow.filesystem.HttpHeader:(\xe2?%\n#com.databricks.rpc.DoNotLogContents\"\\\n\x16\x43reateUploadUrlRequest\x12\x0c\n\x04path\x18\x01 \x01(\t:4\xe2?1\n/com.databricks.rpc.RPC[CreateUploadUrlResponse]\"\x80\x01\n\x17\x43reateUploadUrlResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\x12.\n\x07headers\x18\x02 \x03(\x0b\x32\x1d.mlflow.filesystem.HttpHeader:(\xe2?%\n#com.databricks.rpc.DoNotLogContents\"\x96\x01\n\x0e\x44irectoryEntry\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x14\n\x0cis_directory\x18\x02 \x01(\x08\x12\x11\n\tfile_size\x18\x03 \x01(\x03\x12\x15\n\rlast_modified\x18\x04 \x01(\x03\x12\x0c\n\x04name\x18\x05 \x01(\t:(\xe2?%\n#com.databricks.rpc.DoNotLogContents\"\x8f\x01\n\x15ListDirectoryResponse\x12\x33\n\x08\x63ontents\x18\x01 \x03(\x0b\x32!.mlflow.filesystem.DirectoryEntry\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t:(\xe2?%\n#com.databricks.rpc.DoNotLogContents2\xcb\x02\n\x11\x46ilesystemService\x12\x9d\x01\n\x11\x43reateDownloadUrl\x12+.mlflow.filesystem.CreateDownloadUrlRequest\x1a,.mlflow.filesystem.CreateDownloadUrlResponse\"-\xf2\x86\x19)\n%\n\x04POST\x12\x17/fs/create-download-url\x1a\x04\x08\x02\x10\x00\x10\x03\x12\x95\x01\n\x0f\x43reateUploadUrl\x12).mlflow.filesystem.CreateUploadUrlRequest\x1a*.mlflow.filesystem.CreateUploadUrlResponse\"+\xf2\x86\x19\'\n#\n\x04POST\x12\x15/fs/create-upload-url\x1a\x04\x08\x02\x10\x00\x10\x03\x42\x30\n#com.databricks.api.proto.filesystem\x90\x01\x01\xa0\x01\x01\xe2?\x02\x10\x01')



_HTTPHEADER = DESCRIPTOR.message_types_by_name['HttpHeader']
_CREATEDOWNLOADURLREQUEST = DESCRIPTOR.message_types_by_name['CreateDownloadUrlRequest']
_CREATEDOWNLOADURLRESPONSE = DESCRIPTOR.message_types_by_name['CreateDownloadUrlResponse']
_CREATEUPLOADURLREQUEST = DESCRIPTOR.message_types_by_name['CreateUploadUrlRequest']
_CREATEUPLOADURLRESPONSE = DESCRIPTOR.message_types_by_name['CreateUploadUrlResponse']
_DIRECTORYENTRY = DESCRIPTOR.message_types_by_name['DirectoryEntry']
_LISTDIRECTORYRESPONSE = DESCRIPTOR.message_types_by_name['ListDirectoryResponse']
HttpHeader = _reflection.GeneratedProtocolMessageType('HttpHeader', (_message.Message,), {
  'DESCRIPTOR' : _HTTPHEADER,
  '__module__' : 'databricks_filesystem_service_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.filesystem.HttpHeader)
  })
_sym_db.RegisterMessage(HttpHeader)

CreateDownloadUrlRequest = _reflection.GeneratedProtocolMessageType('CreateDownloadUrlRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOWNLOADURLREQUEST,
  '__module__' : 'databricks_filesystem_service_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.filesystem.CreateDownloadUrlRequest)
  })
_sym_db.RegisterMessage(CreateDownloadUrlRequest)

CreateDownloadUrlResponse = _reflection.GeneratedProtocolMessageType('CreateDownloadUrlResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOWNLOADURLRESPONSE,
  '__module__' : 'databricks_filesystem_service_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.filesystem.CreateDownloadUrlResponse)
  })
_sym_db.RegisterMessage(CreateDownloadUrlResponse)

CreateUploadUrlRequest = _reflection.GeneratedProtocolMessageType('CreateUploadUrlRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUPLOADURLREQUEST,
  '__module__' : 'databricks_filesystem_service_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.filesystem.CreateUploadUrlRequest)
  })
_sym_db.RegisterMessage(CreateUploadUrlRequest)

CreateUploadUrlResponse = _reflection.GeneratedProtocolMessageType('CreateUploadUrlResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUPLOADURLRESPONSE,
  '__module__' : 'databricks_filesystem_service_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.filesystem.CreateUploadUrlResponse)
  })
_sym_db.RegisterMessage(CreateUploadUrlResponse)

DirectoryEntry = _reflection.GeneratedProtocolMessageType('DirectoryEntry', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTORYENTRY,
  '__module__' : 'databricks_filesystem_service_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.filesystem.DirectoryEntry)
  })
_sym_db.RegisterMessage(DirectoryEntry)

ListDirectoryResponse = _reflection.GeneratedProtocolMessageType('ListDirectoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDIRECTORYRESPONSE,
  '__module__' : 'databricks_filesystem_service_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.filesystem.ListDirectoryResponse)
  })
_sym_db.RegisterMessage(ListDirectoryResponse)

_FILESYSTEMSERVICE = DESCRIPTOR.services_by_name['FilesystemService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.databricks.api.proto.filesystem\220\001\001\240\001\001\342?\002\020\001'
  _CREATEDOWNLOADURLREQUEST._options = None
  _CREATEDOWNLOADURLREQUEST._serialized_options = b'\342?3\n1com.databricks.rpc.RPC[CreateDownloadUrlResponse]'
  _CREATEDOWNLOADURLRESPONSE._options = None
  _CREATEDOWNLOADURLRESPONSE._serialized_options = b'\342?%\n#com.databricks.rpc.DoNotLogContents'
  _CREATEUPLOADURLREQUEST._options = None
  _CREATEUPLOADURLREQUEST._serialized_options = b'\342?1\n/com.databricks.rpc.RPC[CreateUploadUrlResponse]'
  _CREATEUPLOADURLRESPONSE._options = None
  _CREATEUPLOADURLRESPONSE._serialized_options = b'\342?%\n#com.databricks.rpc.DoNotLogContents'
  _DIRECTORYENTRY._options = None
  _DIRECTORYENTRY._serialized_options = b'\342?%\n#com.databricks.rpc.DoNotLogContents'
  _LISTDIRECTORYRESPONSE._options = None
  _LISTDIRECTORYRESPONSE._serialized_options = b'\342?%\n#com.databricks.rpc.DoNotLogContents'
  _FILESYSTEMSERVICE.methods_by_name['CreateDownloadUrl']._options = None
  _FILESYSTEMSERVICE.methods_by_name['CreateDownloadUrl']._serialized_options = b'\362\206\031)\n%\n\004POST\022\027/fs/create-download-url\032\004\010\002\020\000\020\003'
  _FILESYSTEMSERVICE.methods_by_name['CreateUploadUrl']._options = None
  _FILESYSTEMSERVICE.methods_by_name['CreateUploadUrl']._serialized_options = b'\362\206\031\'\n#\n\004POST\022\025/fs/create-upload-url\032\004\010\002\020\000\020\003'
  _HTTPHEADER._serialized_start=99
  _HTTPHEADER._serialized_end=140
  _CREATEDOWNLOADURLREQUEST._serialized_start=142
  _CREATEDOWNLOADURLREQUEST._serialized_end=238
  _CREATEDOWNLOADURLRESPONSE._serialized_start=241
  _CREATEDOWNLOADURLRESPONSE._serialized_end=371
  _CREATEUPLOADURLREQUEST._serialized_start=373
  _CREATEUPLOADURLREQUEST._serialized_end=465
  _CREATEUPLOADURLRESPONSE._serialized_start=468
  _CREATEUPLOADURLRESPONSE._serialized_end=596
  _DIRECTORYENTRY._serialized_start=599
  _DIRECTORYENTRY._serialized_end=749
  _LISTDIRECTORYRESPONSE._serialized_start=752
  _LISTDIRECTORYRESPONSE._serialized_end=895
  _FILESYSTEMSERVICE._serialized_start=898
  _FILESYSTEMSERVICE._serialized_end=1229
FilesystemService = service_reflection.GeneratedServiceType('FilesystemService', (_service.Service,), dict(
  DESCRIPTOR = _FILESYSTEMSERVICE,
  __module__ = 'databricks_filesystem_service_pb2'
  ))

FilesystemService_Stub = service_reflection.GeneratedServiceStubType('FilesystemService_Stub', (FilesystemService,), dict(
  DESCRIPTOR = _FILESYSTEMSERVICE,
  __module__ = 'databricks_filesystem_service_pb2'
  ))


# @@protoc_insertion_point(module_scope)
