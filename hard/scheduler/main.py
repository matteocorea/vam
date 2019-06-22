from time import sleep
import sys

"""Proof of concept for a simple scheduler.

This provides a minimal skeleton for a system able to schedule polling
and processing workloads on a number of streams.
"""

def schedule_work_for_stream(stream):
    """Schedule work for a single stream.
    
    In the current proof of concept implementation this method is just
    printing some message. In the actual implementation it should send
    a SQS message to a given queue, containing the id of the stream to
    be scheduled.
    """
    print (f'We need to poll stream #{stream}')
    
def get_streams_to_poll():
    """Retrieve the list of streams we need to subscribe to.
    
    This currently returns a simple proof of concept list. In a proper
    implementation this should get the list of streams from an external
    file (so that it's easy to ask the system to subscribe to 100s of
    streams).
    
    :return: List of stream id to be processed.
    """
    return [185260, 1234, 5423, 6534, 9345]
    
def main():
    if (len(sys.argv) != 2):
        print (f"Usage: {sys.argv[0]} scheduling_frequency_seconds")
        exit(1)
    poll_frequency_seconds = (int)(sys.argv[1])

    streams = get_streams_to_poll()
    
    while(True):
        for stream in streams:
            schedule_work_for_stream(stream)
        sleep(poll_frequency_seconds)
        
if __name__ == '__main__':
    main()