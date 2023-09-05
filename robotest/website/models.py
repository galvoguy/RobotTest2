from django.db import models

class Procedure(models.Model):
    procedureId = models.AutoField("procedure id", primary_key=True)
    partId=models.CharField("part id", max_length=200)
    description = models.CharField("procedure description", max_length=600)
    parameterOverrides = models.JSONField

    def __str_(self):
        return self.procedureId + ' ' + self.description
    

class Test(models.Model):
    testID = models.AutoField("test id", primary_key=True)
    parameters = models.JSONField
    docDirectory = models.FilePathField("document directory", path="/home/images")
    partId = models.CharField("part id", max_length=200)
    testDescription = models.CharField("test description", max_length=600)

    def __str__(self):
        return self.testID + ' ' + self.testDescription
    

class Result(models.Model):
    outputId = models.AutoField("output id", primary_key=True)
    data = models.BinaryField("test data")
    testID = models.ForeignKey(Test, on_delete=models.PROTECT, verbose_name="test id") #Don't delete a result if Test.testId gets deleted.
    logNotes = models.CharField("log notes", max_length=200)
    partInfo = models.JSONField #PN, SN, PCB Rev, PCBA rev, FW, Mods

    def __str__ (self):
        return self.outputId + ' ' + self.logNotes
    

class Attachments(models.Model):
    outputId = models.ForeignKey(Result, on_delete=models.PROTECT, verbose_name="output id") # Don't delete attachments if Result.outputId is deleted.
    reportDate = models.DateField("date", auto_now=True) 
    outputFileAttachments = models.FilePathField("output file directory", path="/home/screenshots")   # A path to any images, screenshots saved to a file location. 

    def __str__(self):
        return self.outputId + ' ' + self.reportDate
    
    





