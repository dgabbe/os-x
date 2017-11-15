# os-x
Various OS X related scripts to setup/automate a Mac

# Batch OCR of PDF files

I switched from using Apple's Preview to Smile Software's [PDFpen](https://smilesoftware.com/pdfpen/) to view and manipulate PDFs. The automator `automators/PDFpen/Batch OCR folder.app` will OCR a file(s) and folder(s) dragged and dropped onto it. There are two workflows inside the Automator script and you should enable the one that is best suited to your needs.
 * `OCR file` will only OCR a file if PDFpen thinks it has not been OCR'd. If selectable text is present, PDFpen thinks the file does not need to be OCR'd. 99% of time this is the correct choice.
 * `OCR file with override` will pop-up a dialog box asking you if you want to force OCRing.  The automator will wait until you make a choice so it's not ideal for unattended operation.

 When you pull these scripts to your computer, the files need to be re-associated with their workflows in `Batch OCR folder`.
