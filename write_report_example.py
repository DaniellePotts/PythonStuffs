#add other details in the parameters
def write_report(file_name, name, movie, tickets, total_cost):
    with open(file_name, 'w') as f:
        f.write('======REPORT======\n') #\n says move to next line
        f.write('Name: {0}\n'.format(name))#{0} says the first variable in format fills this spot
        f.write('Movie: {0}\n'.format(movie))
        f.write('Tickets: {0}\n'.format(tickets))
        f.write('Total Tickets: {0}\n'.format(total_cost))


write_report('report.txt','Danielle','Sonic 2',3,1)
