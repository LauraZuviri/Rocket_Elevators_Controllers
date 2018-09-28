floorNames = ["basement2", "basement1", "lobby", "floor2", "floor3", "floor4", "floor5", "floor6", "floor7", "floor8"]
Number_of_floors = 10
elevatorList = ["elevator1", "elevator2"]
Number_of_elevators = 2
elevators = []
floors = []
ElevatorDirection = ["goingUp", "goingDown", "goingNowhere"]
status = ["idle", "stopped", "moving"]

class Controller:
    def __init__(self, number_of_floor, nb_elevators):
        self.columns = []
        self.columns.append(Column(number_of_floor, nb_elevators))

    def requestElevator (self, floor_Number, wanted_direction):
        print("I want to go = "+str(wanted_direction))
        print("I am on floor = "+str(floor_Number))
        elevator = self.findBestElevator(floor_Number, wanted_direction)
        print("found elevator " +str(elevator.elevator_name))
        elevator.floorList.append(floor_Number)
        self.operateElevator(elevator)
        return elevator
        self.requestElevator = []

    def operateElevator(self, elevator):
        if elevator.direction == "goingUp":
            elevator.floorList.sort()
        else:
            elevator.floorList.sort(reverse = True)

        if elevator.floorList == []:
            elevator.status = "idle"
        else:
            nextFloor = elevator.floorList[0]
            if nextFloor == elevator.currentFloor:
                elevator.status = "stopped"
                elevator.openDoor()
            elif nextFloor > elevator.currentFloor:
                elevator.status = "moving"
                elevator.moveUp()
            else:
                elevator.status = "moving"
                elevator.moveDown()

    def requestFloor(self, floor_number, elevator):
        elevator.activateButton(floor_number)
        elevator.floorList.append(floor_number)
        self.operateElevator(elevator)

    def findBestElevator (self, floor_number, wanted_direction):
        print("trying to find elevator for direction " + str(wanted_direction))
        print("trying to find elevator for floor_number " + str(floor_number))
        for elevator in self.columns[0].elevators:
            print("elevator " + str(elevator.elevator_name) + ", direction " + str(elevator.direction) + ", status " + str(elevator.status))
            if elevator.currentFloor == floor_number and elevator.status == "stopped":
                return elevator
            elif elevator.status == "Idle":
                return elevator
            elif elevator.status == "moving" and elevator.currentFloor < floor_number and elevator.direction == "goingUp" and wanted_direction == "up":
                return elevator
            elif elevator.status == "moving" and elevator.currentFloor > floor_number and elevator.direction == "goingDown" and wanted_direction == "down":
                return elevator
            else:
                return self.elevatorWithShortestFloorList()

    def elevatorWithShortestFloorList(self):
           shortestListElevator = None
           for elevator in self.columns[0].elevators:

               if shortestListElevator == None or len(elevator.floorList) < len(shortestListElevator.floorList):
                shortestListElevator = elevator

                print("elevator in elevatorWithShortestFloorList " + str(shortestListElevator))
           return shortestListElevator

class Column:
    def __init__(self, numberOfFloor, numberOfElevators):
        self.elevators = []
        self.floors = []
        for index in range (numberOfElevators):
            self.elevators.append(Elevator(index+1, numberOfFloor))
            print("elevator added " + str(self.elevators[index].elevator_name))

        for index in range (numberOfFloor):
            callButtons = []
            if index is 0:
                callButtons.append(CallButton("up", index))
            elif index is numberOfFloor -1:
                callButtons.append(CallButton("down", index))
            else:
                callButtons.append(CallButton("up", index))
                callButtons.append(CallButton("down", index))

            self.floors.append(Floor(index, floorNames[index], callButtons))

class Elevator:
    def __init__(self, elevator_name, nbOfFloors):
        self.elevator_name = elevator_name
        self.direction = "goingNowhere"
        self.status = "Idle"
        self.currentFloor = 0
        self.floorList = []
        self.floorButtons = []
        self.openDoorButton = OpenDoorsButton()
        self.closeDoorsButton = CloseDoorsButton()
        self.door = Door()
        self.elevatorTargetFloor = []
        self.nextFloorInFloorList = "next"
        self.maximumCapacity = 0

        for index in range (nbOfFloors):
            self.floorButtons.append(FloorButton(index+1, self.elevator_name))

    def moveUp(self):
        print("moving elevator up")
        self.status = "goingUp"
        nextFloor = self.floorList[0]
        while nextFloor != self.currentFloor:
            self.currentFloor = self.currentFloor + 1

        self.floorList.remove(nextFloor)
        self.openDoor()
        print("done moving elevator up. on floor " + str(self.currentFloor))

    def moveDown(self):
        print("moving elevator down")
        self.status = "goingDown"
        nextFloor = self.floorList[0]
        while nextFloor != self.currentFloor:
            self.currentFloor = self.currentFloor -1

        self.floorList.remove(nextFloor)
        self.openDoor()
        print("done moving elevator down. on floor " + str(self.currentFloor))

    def openDoor(self):
        if self.status is "moving":
            self.door.status is "closed"
        elif self.currentFloor is 0:
            self.door.status is "opened" and self.door.doorTimer is "activated"

    def closeDoor(self):
        if self.door.doorTimer > 0:
            self.door.status = "opened"
        elif self.maximumCapacity is 0:
            self.door.status = "opened"
        elif elevator.status is "blocked":
            self.door.status = "opened"
        else:
            self.door.status = "closed"

    def activateButton(self, floorNumber):
        print("activating floor button for floor number " + str(floorNumber))
        buttonToActivate = 0
        for button in self.floorButtons:
            if button.floorNumber == floorNumber:
                buttonToActivate = button

        buttonToActivate.status = "active"

class Floor:
    def __init__(self, number, name, callButtons):
        self.number = number
        self.name = name
        self.callButtons = callButtons

class FloorButton:
    def __init__(self, floorNumber, number_of_elevator):
        self.floorNumber = floorNumber
        self.number_of_elevator = number_of_elevator
        self.status = []

    def setButton (self, floor, Direction):
        b = findButton(floor, Direction)
        b.self.status = "active"

    def findbutton(self, floor, direction):
        return Button()

class Door:
    def __init__(self):
        self.status = "closed", "opened"
        self.doorTimer = 5
    def setDoorTimer(self):
        self.status = "activated"

    def open(self):
        self.status = "opened"
        print("door opened, status = " + str(self.status))

    def close(self):
        self.status = "closed"
        print("door closed, status = " + str(self.status))

class CallButton:
    def __init__(self, direction, floor):
        self.direction = direction
        self.floor = floor
        self.activated = False

class OpenDoorsButton:

    def __init__(self):
        self.status = "deactivated"

class CloseDoorsButton:
    def __init__(self):
        self.status = "deactivated"


controller = Controller(10, 2)
controller.columns[0].elevators[0].currentFloor = 1
controller.columns[0].elevators[1].currentFloor = 4
elevator = controller.requestElevator(2, "up")
floor = controller.requestFloor(6, elevator)

print("REQUEST ELEVATOR DONE")

controller = Controller(10, 2)
controller.columns[0].elevators[0].currentFloor = 9
controller.columns[0].elevators[1].currentFloor = 2
elevator = controller.requestElevator(0, "up")
floor = controller.requestFloor(4, elevator)
elevator = controller.requestElevator(2, "up")
floor = controller.requestFloor(3, elevator)
elevator = controller.requestElevator(7, "down")
floor = controller.requestFloor(1, elevator)

#A User located at Floor 1 calls for elevators Originating from Basement 1 and Floor 4,
#he gets one and gets to the Fifth floor with it'

#A User located at Floor Basement 2 calls for elevators Originating from Floor 8 and Floor 1, he gets one to get to the 4th floor,
#Simultaneously, someone at Floor 1 requests an elevator to get to 3rd floor as someone at 7th requests to go down to basement 1'

#A User located at Floor 8 calls for elevators Originating from Floor 8 and Floor 1, he gets one to get to the 1st floor.
#Simultaneously Someone at Floor 1 requests an elevator to get to Basement 1'
