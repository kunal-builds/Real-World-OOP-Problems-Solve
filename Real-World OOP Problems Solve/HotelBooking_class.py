class HotelBooking:
    def __init__(self):
        self.rooms = []
        self.booking = []
        self.availble = []

    def add_room(self, room_number):
        self.rooms.append(room_number)
        self.availble.append(room_number)
        print(f"Room {room_number} Added SuccesFully")
    
    def book_room(self, guest_name, days):
        if not self.availble:
            print("Room Not Avaible")
            return
        rooms = self.availble[0]

        booking = {
            "rooms": rooms,
            "guest": guest_name,
            "days": days
        }
        self.booking.append(booking)
        self.availble.remove(rooms)

        print(f"Room{rooms} booked succesfully for {guest_name}, for {days} days.")



hotel = HotelBooking()
hotel.add_room(101)
hotel.add_room(102)

hotel.book_room("kunal", 2)
hotel.book_room("aman", 2)

