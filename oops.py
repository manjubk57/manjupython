class CSVlogger:
    def __init__(self,file_obj):
        self.file_obj=file_obj

    def log(self,message):
        word = message.split()
        import csv
        writer_obj=csv.writer(message+"\n")
        writer_obj.writerow(word)

class FilterLogger:
    def __init__(self,pattern):
        self.pattern
    def log(self,message):
        if self.pattern in message :
            super().log(message)







