from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterUpdate(_message.Message):
    __slots__ = ("address", "mask", "value")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    address: int
    mask: int
    value: int
    def __init__(self, address: _Optional[int] = ..., mask: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class XclbinRequest(_message.Message):
    __slots__ = ("data", "overlay_name", "topology", "prepare_only", "firmware", "partial", "expected_marker", "marker", "shutdown_addresses", "registers", "firmware_data")
    DATA_FIELD_NUMBER: _ClassVar[int]
    OVERLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    PREPARE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_MARKER_FIELD_NUMBER: _ClassVar[int]
    MARKER_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    REGISTERS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    overlay_name: str
    topology: str
    prepare_only: bool
    firmware: str
    partial: bool
    expected_marker: str
    marker: str
    shutdown_addresses: _containers.RepeatedScalarFieldContainer[int]
    registers: _containers.RepeatedCompositeFieldContainer[RegisterUpdate]
    firmware_data: bytes
    def __init__(self, data: _Optional[bytes] = ..., overlay_name: _Optional[str] = ..., topology: _Optional[str] = ..., prepare_only: bool = ..., firmware: _Optional[str] = ..., partial: bool = ..., expected_marker: _Optional[str] = ..., marker: _Optional[str] = ..., shutdown_addresses: _Optional[_Iterable[int]] = ..., registers: _Optional[_Iterable[_Union[RegisterUpdate, _Mapping]]] = ..., firmware_data: _Optional[bytes] = ...) -> None: ...

class XclbinResponse(_message.Message):
    __slots__ = ("data", "loaded")
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOADED_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    loaded: bool
    def __init__(self, data: _Optional[bytes] = ..., loaded: bool = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("file_path", "data")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    data: bytes
    def __init__(self, file_path: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExistsFileRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class ExistsFileResponse(_message.Message):
    __slots__ = ("exists",)
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    def __init__(self, exists: bool = ...) -> None: ...

class MakeDirRequest(_message.Message):
    __slots__ = ("dir_path",)
    DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    dir_path: str
    def __init__(self, dir_path: _Optional[str] = ...) -> None: ...

class MakeDirResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveDirRequest(_message.Message):
    __slots__ = ("dir_path",)
    DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    dir_path: str
    def __init__(self, dir_path: _Optional[str] = ...) -> None: ...

class RemoveDirResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetBitstreamAttrsRequest(_message.Message):
    __slots__ = ("binfile_name", "partial")
    BINFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    binfile_name: str
    partial: bool
    def __init__(self, binfile_name: _Optional[str] = ..., partial: bool = ...) -> None: ...

class SetBitstreamAttrsResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class ShutdownRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShutdownResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class SetPlClkRequest(_message.Message):
    __slots__ = ("i", "div0", "div1", "clk_mhz")
    I_FIELD_NUMBER: _ClassVar[int]
    DIV0_FIELD_NUMBER: _ClassVar[int]
    DIV1_FIELD_NUMBER: _ClassVar[int]
    CLK_MHZ_FIELD_NUMBER: _ClassVar[int]
    i: int
    div0: int
    div1: int
    clk_mhz: int
    def __init__(self, i: _Optional[int] = ..., div0: _Optional[int] = ..., div1: _Optional[int] = ..., clk_mhz: _Optional[int] = ...) -> None: ...

class SetPlClkResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class DownloadRequest(_message.Message):
    __slots__ = ("buffer",)
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    buffer: bytes
    def __init__(self, buffer: _Optional[bytes] = ...) -> None: ...

class DownloadResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...
