if __name__ == "__main__":
    print("This is a module that is imported by 'uGecko.py'. Don't run it directly.")
    exit()
else:
    from enum import Enum

class Commands(Enum):
    POKE_8                      = b'\x01'
    POKE_16                     = b'\x02'
    POKE_32                     = b'\x03'
    READ_MEMORY                 = b'\x04'
    READ_MEMORY_KERNEL          = b'\x05'
    VALIDATE_ADDRESS_RANGE      = b'\x06'
    MEMORY_DISASSEMBLE          = b'\x08'
    # READ_MEMORY_COMPRESSED    = b'\x09' -> Obsolete
    KERNEL_WRITE                = b'\x0B' 
    KERNEL_READ                 = b'\x0C'
    #TAKE_SCREENSHOT            = b'\x0D' -> 
    UPLOAD_MEMORY               = b'\x41'
    SERVER_STATUS               = b'\x50'
    GET_DATA_BUFFER_SIZE        = b'\x51'
    READ_FILE                   = b'\x52'
    READ_DIRECTORY              = b'\x53'
    REPLACE_FILE                = b'\x54'
    GET_CODE_HANDLER_ADDRESS    = b'\x55'
    READ_THREADS                = b'\x56'
    ACCOUNT_IDENTIFIER          = b'\x57'
    # WRITE_SCREEN              = b'\x58' -> Exception DSI
    FOLLOW_POINTER              = b'\x60'
    REMOTE_PROCEDURE_CALL       = b'\x70'
    GET_SYMBOL                  = b'\x71'
    MEMORY_SEARCH               = b'\x72'
    ADVANCED_MEMORY_SEARCH      = b'\x73'
    EXECUTE_ASSEMBLY            = b'\x81'
    PAUSE_CONSOLE               = b'\x82'
    RESUME_CONSOLE              = b'\x83'
    IS_CONSOLE_PAUSED           = b'\x84'
    GET_SERVER_VERSION          = b'\x99'
    GET_OS_VERSION              = b'\x9A'
    SET_DATA_BREAKPOINT         = b'\xA0'
    SET_INSTRUCTION_BREAKPOINT  = b'\xA2'
    TOGGLE_BREAKPOINT           = b'\xA5'
    REMOVE_ALL_BREAKPOINT       = b'\xA6'
    POKE_REGISTERS              = b'\xA7'
    GET_STACK_TRACE             = b'\xA8'
    GET_ENTRY_POINT_ADDRESS     = b'\xB1'
    RUN_KERNEL_COPY_SERVICE     = b'\xCD'
    IOSU_HAX_READ_FILE          = b'\xD0'
    GET_VERSION_HASH            = b'\xE0'
    PERSIST_ASSEMBLY            = b'\xE1'
    CLEAR_ASSEMBLY              = b'\xE2'
