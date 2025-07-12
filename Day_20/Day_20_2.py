## CONTROLLER -------- (MVC)

# UTILITY CLASS -> where we have file i/o functions
# IO -> Input (reading data from file from program)
#    -> Output (writing data into filr from program)

import os                                        #OPERATING SYSTEM
class FileHelper:                                # It is utility Class, it doesnt denotes object

    def __init(self):
        visitor_file_path = 'visitor-log.csv'

        if os.path.exists(visitor_file_path):
            print('File Helper Initialised')

        else:
            file = open('visitor-log.csv','a')        # a -> append mode
            headers = 'serial_no, date_time_stamp, name, address, whome_to_meet, purpose, phone'
            file.write(headers)

    def write_in_file(self, content):
        file = open('visitor-log.csv', a)
        file.write(content)
        print('Content : ', content, 'Saved in File')

    def read_file(self):
        file = open('visitor-log.csv', a)
        lines = file.readLines()
        print('Reading Data from Files.Total Lines : ', len(lines))
        for line in lines:
            print(line)

    
    def file_size(self):
        file = open('visitor-log.csv', 'r')
        data = file.read()
        return len(data)
    
    def lines_in_file(self):
        file = open('visitor-log.csv', 'r')
        lines = file.readlines()
        return len(lines)