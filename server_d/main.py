import argparse

import os
import pydicom
from pydicom.filewriter import write_file_meta_info
from pynetdicom import (
    AE, debug_logger, evt, AllStoragePresentationContexts,
    ALL_TRANSFER_SYNTAXES
)




def handle_store(event, storage_dir):
    """Handle EVT_C_STORE events."""
    try:
        os.makedirs(storage_dir, exist_ok=True)
    except:
        # Unable to create output dir, return failure status
        return 0xC001

    # print(event.dataset.PatientName)
    #file name
    fname = os.path.join(storage_dir, event.timestamp.strftime('%Y%m%d%H%M') + '.' + str(event.dataset.PatientName) + '.dcm')

    with open(fname, 'wb') as f:
        # Write the preamble, prefix and file meta information elements
        f.write(b'\x00' * 128)
        f.write(b'DICM')
        write_file_meta_info(f, event.file_meta)
        # Write the raw encoded dataset
        f.write(event.request.DataSet.getvalue())


    return 0x0000



parser = argparse.ArgumentParser()

parser.add_argument("-s", "--startserver",
                    help="start dicom server, your argument will be a name of output directory for dicom files")

# parser.add_argument("-p", "--password", help="password (min 8 characters)")
#


args = parser.parse_args()

if __name__ == '__main__':
    #if argument for start server
    if args.startserver:
        # show in terminal pynetdicom logging output
        debug_logger()


        handlers = [(evt.EVT_C_STORE, handle_store, [args.startserver])]

        #DICOM Application Entities
        ae = AE()

        #get list of all syntaxes
        storage_sop_classes = [
            cx.abstract_syntax for cx in AllStoragePresentationContexts
        ]

        for uid in storage_sop_classes:
            #accept all syntaxes
            ae.add_supported_context(uid, ALL_TRANSFER_SYNTAXES)

        #start server at port 11112 on localhost in blocking mode.
        ae.start_server(("127.0.0.1", 11112), block=True, evt_handlers=handlers)
    else:
        parser.print_help()