input_second = input("please enter seconds ")
to_int_input = int(input_second)

total_secs = to_int_input
hours = total_secs // 3600
secs_remaining = to_int_input % 3600
minutes = secs_remaining // 60
secs_remaining_final = secs_remaining % 60

print('this is total secs', to_int_input)
print('has', hours, 'hours', minutes, 'minutes and',
      secs_remaining_final, 'seconds')
