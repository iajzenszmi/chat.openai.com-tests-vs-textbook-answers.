PROGRAM lift_sim

INTEGER current_floor, destination_floor, direction
INTEGER floors(10)
LOGICAL stop(10)

! Initialize the floors and stop array
DO i = 1, 10
  floors(i) = i
  stop(i) = .FALSE.
ENDDO

! Start at ground floor
current_floor = 1
direction = 1

! Main loop
DO WHILE (.TRUE.)
  WRITE(*,*) "Current floor:", current_floor

  ! Set the destination floor based on button presses
  READ(*,*) destination_floor
  stop(destination_floor) = .TRUE.

  ! Determine the direction to travel
  IF (destination_floor > current_floor) THEN
    direction = 1
  ELSEIF (destination_floor < current_floor) THEN
    direction = -1
  ENDIF

  ! Travel to the destination floor
  DO WHILE (current_floor /= destination_floor)
    current_floor = current_floor + direction
    IF (stop(current_floor)) THEN
      WRITE(*,*) "Stopping at floor:", current_floor
      stop(current_floor) = .FALSE.
    ENDIF
  ENDDO
ENDDO

END PROGRAM lift_sim

