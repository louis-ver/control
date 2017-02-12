from urllib.parse import urlparse
import sched
import time

test_file = "/Users/louisolivier/test.txt"
def add_website_to_block_list(url):
    hostname = urlparse(url).hostname
    block_host = "0.0.0.0 " + hostname + "\n"
    try:
        host_file = open(test_file, 'a')
        host_file.write(block_host)
        host_file.close()
    except:
        return "Problem writing to file"
    return True

def remove_website_from_block_list(url):
    hostname = urlparse(url).hostname
    block_host = "0.0.0.0 " + hostname + "\n"
    host_file = open(test_file, "r")
    host_file_string = host_file.readlines()
    host_file.close()
    if block_host in host_file_string:
        host_file = open(test_file, "w")
        for line in host_file_string:
            if line != block_host:
                host_file.write(line)
        host_file.close()
        return True
    return False

# Add website to block list for specific amount of time (hours)
def add_website_to_block_list_for_duration(url, duration):
    add_website_to_block_list(url)
    scheduled_event = sched.scheduler(time.time, time.sleep)
    scheduled_event.enter(duration, 1, remove_website_from_block_list(url))
