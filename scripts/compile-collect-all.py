#!/bin/python3
import os
import shutil
import fitz  #PyMuPDF

def extract_title(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            # Access metadata directly using 'info'
            title = doc.metadata.get('title')
        return title
    except Exception as e:
        # print(f"Error extracting title from {pdf_path}: {e}")
        return None

source_folder = '~/notes'        #adjust to your needs
collected_folder = '~/collected' #adjust to your needs

# Iterate through subfolders in the source folder
for root, dirs, files in os.walk(os.path.expanduser(source_folder)):
    for file in files:
        if file == 'master.pdf':
            pdf_path = os.path.join(root, file)

            # print(f"Processing: {pdf_path}")

            # Extract title from the PDF
            title = extract_title(pdf_path)

            if title:
                # print(f"Title extracted: {title}")

                # Rename the file to its title
                new_name = os.path.join(root, f'{title}.pdf')
                try:
                    os.rename(pdf_path, new_name)
                    # print(f"File renamed to: {new_name}")

                    # Copy the renamed file to the collected folder
                    shutil.copy(new_name, os.path.expanduser(collected_folder))
                    # print(f"File copied to: {collected_folder}")

                except Exception as e:
                    # print(f"Error processing {pdf_path}: {e}")
