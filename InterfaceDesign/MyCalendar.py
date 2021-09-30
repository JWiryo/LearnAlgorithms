class MyCalendar:

    def __init__(self):
      
      # Initialize calendar array
      self.calendar = []
    
    # Time Complexity: O(N)
    def book(self, start: int, end: int) -> bool:
      
      # If calendar is empty, just append
      if len(self.calendar) == 0:
        self.calendar.append([start,end])
        return True
      
      # Else, iterate through calendar
      for interval in self.calendar:
        
        bookedStart = interval[0]
        bookedEnd = interval[1]
        
        # If new end time > bookedMeetingStart time and new start time < bookedMeetingEnd time
        if bookedStart < end and start < bookedEnd:
          return False
        
      self.calendar.append([start,end])
      return True