import pyuac
import time
import os


def block_site(hosts_path, website_list):
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass  # The site is already blocked
            else:
                file.write("127.0.0.1 " + website + "\n")
    return website_list


def unblock_site(hosts_path, website_list):
    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)  # Go to the start of the file
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()  # Remove the trailing lines (the blocked websites)


def main():
    # The list of websites to block
    website_list = []
    while True:
        site = input("Enter a website to block (or 'done' to finish): ")
        if site.lower() == "done":
            break
        website_list.append(f"www.{site}.com")
        website_list.append(f"{site}.com")

    # Set hosts_path based on the operating system
    if os.name == "nt":  # Windows
        hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    else:  # Linux and MacOS
        hosts_path = "/etc/hosts"

    try:
        block_site(hosts_path, website_list)
        print("Websites are blocked.")
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        unblock_site(hosts_path, website_list)
        print("Websites are unblocked.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()
