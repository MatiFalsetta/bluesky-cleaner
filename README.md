# 🦋 Bluesky Like Cleaner

*Read this in other languages: [Español](README.es.md)*

A Python tool to remove all likes from your Bluesky account using the official ATProto API.

## ✨ Features

- 🔐 Secure authentication with the official Bluesky API
- 📊 Shows statistics of your likes before deletion
- 🔄 Real-time progress with counter
- ⚠️ Safety confirmation before proceeding
- 🛡️ Error handling and rate limiting
- ⏸️ Ability to interrupt the process at any time

## 📋 Requirements

- Python 3.10 or higher
- A Bluesky account
- Internet access

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/MatiFalsetta/bluesky-cleaner
cd bluesky-cleaner
```

2. Create and activate virtual environment (Recommended):
```bash
python -m venv env
.\env\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install atproto
```

## 💻 Usage

1. **Create an App Password** (Required):
   - Go to [https://bsky.app/settings/app-passwords](https://bsky.app/settings/app-passwords)
   - Add a new application password for this script with a unique name
   - You do not need to check the box to allow access to your direct messages
   - Save the generated password in xxxx-xxxx-xxxx-xxxx format (you'll need it in step 3)

2. Run the script:
```bash
python delete_likes.py
```

3. Enter your Bluesky handle (e.g., `user.bsky.social`)
4. Enter your **app password** (not your regular account password)
5. Review the displayed statistics
6. Confirm if you want to proceed with the deletion

## 🗑️ Uninstallation

To completely remove the tool from your system:

1. Delete the repository folder:
```bash
# Navigate to the parent directory where you cloned the repository
cd ..
# Remove the entire bluesky-cleaner folder
rm -rf bluesky-cleaner
```

**Note**: This will permanently delete all files including the script and any logs. Make sure you don't need any files from the folder before deletion.

## ⚠️ Important Warnings

- **This action is IRREVERSIBLE**: Once deleted, likes cannot be recovered
- **Slow process**: With safety pauses, deleting thousands of likes may take time
- **Requires credentials**: You need your Bluesky username and password

## 🔧 How it Works

1. **Authentication**: Connects to Bluesky using the official ATProto SDK
2. **Retrieval**: Uses `com.atproto.repo.list_records` to get all your like records
3. **Deletion**: Deletes each record using `com.atproto.repo.delete_record`
4. **Progress**: Shows real-time statistics and handles errors

## 🤝 Contributing

Contributions are welcome! If you find a bug or have an improvement:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚡ FAQ

**Is it safe to use my credentials?**
Yes, the script uses the official ATProto library and does not store your credentials.

**Can I interrupt the process?**
Yes, you can use Ctrl+C at any time to stop execution.

**Does it affect the original posts?**
No, it only deletes your like records, not the original posts from other users.

## 🙋‍♂️ Support

If you have problems or questions, open an [issue](https://github.com/MatiFalsetta/bluesky-cleaner/issues) in this repository.

---

⭐ If this project was useful to you, give it a star!