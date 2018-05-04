from microbit import *

counter = 0
old_counter = ["-1", "-1", "-1", "-1", "-1"]

# disp_mode
#  0 : soroban
#  1 : digit
disp_mode = 0
old_disp_mode = 0

# light level
light_lv_top_on     = 9
light_lv_top_off    = 2
light_lv_bottom_on  = 6
light_lv_bottom_off = 0

button_a_is_purresing = 0
button_b_is_purresing = 0

def DipsNumSoroban(i_num):
  if i_num >= 100000:
    display.scroll("Error: The digit is too large.")
    return

  num_string = str(i_num)
  num_string = "0" * (5 - len(num_string)) + num_string

  for i in range(5):
    if old_counter[4 - i] != num_string[4 - i]:
      DispDigSoroban(num_string[4 - i], 4 - i)
      old_counter[4 - i] = num_string[4 - i]


def DispDigSoroban(i_digit: str, i_pos_x: int):
  digit = int(i_digit)
  pos_x = int(i_pos_x)

  if digit >= 5:
    display.set_pixel(pos_x, 0, light_lv_top_on)
    digit -= 5
  else:
    display.set_pixel(pos_x, 0, light_lv_top_off)

  if digit >= 1:
    display.set_pixel(pos_x, 1, light_lv_bottom_on)
  else:
    display.set_pixel(pos_x, 1, light_lv_bottom_off)

  if digit >= 2:
    display.set_pixel(pos_x, 2, light_lv_bottom_on)
  else:
    display.set_pixel(pos_x, 2, light_lv_bottom_off)

  if digit >= 3:
    display.set_pixel(pos_x, 3, light_lv_bottom_on)
  else:
    display.set_pixel(pos_x, 3, light_lv_bottom_off)

  if digit == 4:
    display.set_pixel(pos_x, 4, light_lv_bottom_on)
  else:
    display.set_pixel(pos_x, 4, light_lv_bottom_off)


while True:

  if button_a.is_pressed() and button_b.is_pressed():
    # Switch DispMode Soroban <-> Digit
    display.show(Image.YES)
    disp_mode ^= 1
    button_a_is_purresing = 0
    button_b_is_purresing = 0
    sleep(1000)
  else:

    # Check button A
    if int(button_a.get_presses()) > 0:
      # Single click
      if button_a_is_purresing <= 10:
        # It may be that it is only late to press button B
        button_a_is_purresing += 1
        sleep(10)
        continue
    elif button_a.is_pressed() == True:
      # Pressing
      if button_a_is_purresing <= 50:
        # There is nothing that is late for releasing the button
        button_a_is_purresing += 1
        sleep(10)
        continue
      counter += 1
    elif button_a_is_purresing > 0:
      counter += 1
      button_a_is_purresing = 0

    # Check button B
    if int(button_b.get_presses()) > 0:
      # Single click
      if button_b_is_purresing <= 10:
        # It may be that it is only late to press button A
        button_b_is_purresing += 1
        sleep(10)
        continue
    elif button_b.is_pressed() == True:
      # Pressing
      if button_b_is_purresing <= 50:
        # There is nothing that is late for releasing the button
        button_b_is_purresing += 1
        sleep(10)
        continue
      counter -= 1
    elif button_b_is_purresing > 0:
      counter -= 1
      button_b_is_purresing = 0


  # Loop Number Max<->Min
  if counter < 0:
    counter = 99999
  elif counter > 99999:
    counter = 0

  # Display Number
  if disp_mode == 0:
    DipsNumSoroban(counter)
    if old_disp_mode != disp_mode:
      old_disp_mode = disp_mode
      sleep(1000)
  else:
    display.scroll(str(counter))
    old_counter = ["-1", "-1", "-1", "-1", "-1"]

