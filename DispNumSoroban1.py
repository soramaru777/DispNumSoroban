from microbit import *

counter = 0
old_counter = ["-1", "-1", "-1", "-1", "-1"]

# disp_mode
#  0 : soroban
#  1 : digit
disp_mode = 0
old_disp_mode = 0

# light level

def DipsNumSoroban(i_num):
  if i_num >= 100000:
    display.scroll("Error: The digit is too large.")
    return

  # if i_num == 0:
  #   num_string = "00000"
  # else:
  #   num_string = str(i_num)
  #   num_string = "0" * (5 - len(num_string)) + num_string

  num_string = str(i_num)
  num_string = "0" * (5 - len(num_string)) + num_string

  # len_num_string = len(num_string)

  for i in range(5):
    if old_counter[4 - i] != num_string[4 - i]:
      DipsDigSoroban(num_string[4 - i], 4 - i)
      old_counter[4 - i] = num_string[4 - i]


def DipsDigSoroban(i_digit: str, i_pos_x: int):
  digit = int(i_digit)
  pos_x = int(i_pos_x)

  if digit >= 5:
    display.set_pixel(pos_x, 0, 9)
    digit -= 5
  else:
    display.set_pixel(pos_x, 0, 2)

  if digit >= 1:
    display.set_pixel(pos_x, 1, 5)
  else:
    display.set_pixel(pos_x, 1, 0)

  if digit >= 2:
    display.set_pixel(pos_x, 2, 5)
  else:
    display.set_pixel(pos_x, 2, 0)

  if digit >= 3:
    display.set_pixel(pos_x, 3, 5)
  else:
    display.set_pixel(pos_x, 3, 0)

  if digit == 4:
    display.set_pixel(pos_x, 4, 5)
  else:
    display.set_pixel(pos_x, 4, 0)


while True:
  if button_a.is_pressed() and button_b.is_pressed():
    # Switch DispMode Soroban <-> Digit
    display.show(Image.YES)
    disp_mode ^= 1
    bit_wait = 0
    sleep(1000)
  else:
    # Count Up or Down
    if button_a.is_pressed():
      if bit_wait < 100:
        # Wait for button A & B simultaneously press
        bit_wait += 1
        continue

      counter += 1

      if is_pressing == False:
        # Detect one click.
        sleep(200)
        is_pressing = True

    elif button_b.is_pressed():
      if bit_wait < 100:
        # Wait for button A & B simultaneously press
        bit_wait += 1
        continue

      counter -= 1

      if is_pressing == False:
        # Detect one click.
        sleep(200)
        is_pressing = True
    else:
      bit_wait = 0
      is_pressing = False

  # Loop Number Max<->Min
  if counter < 0:
    counter = 99999
  elif counter > 99999:
    counter = 0

  if disp_mode == 0:
    DipsNumSoroban(counter)
    if old_disp_mode != disp_mode:
      old_disp_mode = disp_mode
      sleep(1000)
  else:
    display.scroll(str(counter))
    old_counter = ["-1", "-1", "-1", "-1", "-1"]
    sleep(1000)
