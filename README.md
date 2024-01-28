# Website Blocker

A simple yet powerful Python script that gives you control over website accessibility on your computer, enabling you to focus on productivity by blocking distracting websites.

## Dependencies

- Python 3
- `pyuac` - A Python module for UAC elevation

## How to Use

1. **Run the script as an administrator:** The script requires administrative privileges to modify the hosts file.
2. **Enter the website URLs:** You will be prompted to enter the websites you want to block. Input them one at a time.
3. **Finish the input:** Once you've entered all the websites, type `done` to proceed.
4. **Keep the script running:** The script must remain active for the block to stay in effect.
5. **Unblock websites:** To unblock, interrupt the script by pressing `Ctrl+C`.

## Functions

- **`block_site(hosts_path, website_list)`**: Takes the path to your hosts file and a list of websites to block, then writes the entries to the hosts file.

- **`unblock_site(hosts_path, website_list)`**: Accepts the path to your hosts file and a list of websites to unblock, then removes the entries from the hosts file.

- **`main()`**: Orchestrates the script by prompting the user for website inputs, invoking `block_site` to enforce the block, and maintaining the script's run state. On interruption, it calls `unblock_site` to revert changes.

## Note

Ensure you run the script as an administrator for it to function correctly—failure to do so will trigger a re-launch attempt with administrative privileges.

## Disclaimer

Exercise caution when using this script. Blocking websites may lead to unintended effects. It's essential to verify the list of blocked and unblocked websites to avoid any issues. This tool is intended for responsible use.