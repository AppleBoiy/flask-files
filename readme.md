# Flask File Management App

This repository contains a Flask application for managing file upload, download, and viewing functionalities. Users can
upload files, view a list of available files, and download files based on specified user permissions.

## Features

- **File Upload**: Users can upload files with associated user permissions.
- **File Download**: Download files based on specified user permissions.
- **File Listing**: View all available files with download links.

### Usage

- **File Upload**: Navigate to the `/upload` endpoint to upload files.
- **File Listing**: Visit the `/files` endpoint to view all available files.
- **File Download**: Use the `/download/<filename>` endpoint to download specific files.

### Example `.http` Requests

You can use the included `.http` files with the REST Client extension in Visual Studio Code to test file upload and
download functionalities directly.

- `upload.http`: Test file upload with different users.
- `download.http`: Test file download scenarios.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
