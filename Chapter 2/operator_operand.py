total_secs = 16500
hours = total_secs // 3600
secs_remaining = total_secs % 3600
minutes = secs_remaining // 60
secs_remaining_final = secs_remaining % 60

print('this is total secs', total_secs)
print('has', hours, 'hours', minutes, 'minutes and',
      secs_remaining_final, 'seconds')
