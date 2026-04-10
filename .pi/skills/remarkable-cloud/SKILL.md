---
name: remarkable-cloud
description: Skill for interacting with reMarkable cloud using rmapi binary.
---

# Skill: remarkable-cloud

This skill enables the assistant to interact with a reMarkable tablet's cloud storage using the `rmapi` Go executable and `bash` internal tool. The reMarkable tablet can store documents in PDF or ePub format.

## Prerequisites
- The `rmapi` command-line tool must be installed and accessible in the system's `PATH`. If it is missing, this skill must automatically stop and instruct the user to visit `https://github.com/janbkrejci/rmapi`.

## Capabilities
The `rmapi` tool supports the following operations on the reMarkable cloud:

1.  **Listing contents (`ls`)**
    - Command: `rmapi ls [path]`
    - Lists files and directories. If no path is provided, it lists the root directory `/`.
    - The return format is
        [f]     file1
        [f]     file2.pdf
        [d]     directory1
        [f]     file3
        ...
    - File and directory names may contain spaces.

2.  **Downloading and converting to PDF (`geta`)**
    - Command: `rmapi geta <filename>`
    - Downloads a specified document from the reMarkable cloud and automatically converts it to a PDF on the local machine.
    - Escape spaces in filename using backslash.

3.  **Uploading a local PDF (`put`)**
    - Command: `rmapi put <local_path_to_pdf> [folder]`
    - Uploads a local PDF file to the specified remote folder (defaults to root `/` if omitted).
    - **Important:** Before uploading, use `ls` to check if the file already exists in the target destination. If it exists there, you must delete it first.

4.  **Removing a file (`rm`)**
    - Command: `rmapi rm <path>`
    - Deletes a specific file or folder path on the reMarkable cloud.
    - Escape spaces in path using backslash.

## Example Usage

### Listing root directory
```bash
rmapi ls
```

### Listing a specific folder
```bash
rmapi ls /Documents
```

### Downloading a document as PDF
```bash
rmapi geta /Notes/MyMeetingNote
```

### Removing a file
```bash
rmapi rm "/Notes/OldNote"
```

### Uploading a PDF to a specific folder
```bash
rmapi put ./local_file.pdf /Books
```