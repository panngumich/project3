###### name: NENG PAN  #######
###### uniqname: panng #######
import sqlite3
import plotly.graph_objs as go

# proj3_choc.py 

# Part 1: Read data from a database called choc.db
DBNAME = 'choc.sqlite'

# Part 1: Implement logic to process user commands
    
def bars_query(first_command, second_command, third_command, forth_command, fifth_command):
    if first_command:
        if forth_command:
            query = "SELECT SpecificBeanBarName, Company, EnglishName, Rating, CocoaPercent, BroadBeanOriginId" + " FROM Bars JOIN Countries ON " + second_command + " " + first_command + " ORDER BY " + third_command + " " + forth_command + " LIMIT " + fifth_command
        else:
            query = "SELECT SpecificBeanBarName, Company, EnglishName, Rating, CocoaPercent, BroadBeanOriginId" + " FROM Bars JOIN Countries ON " + second_command + " " + first_command + " ORDER BY " + third_command + " LIMIT " + fifth_command
    else:
        if forth_command:
            query = "SELECT SpecificBeanBarName, Company, EnglishName, Rating, CocoaPercent, BroadBeanOriginId" + " FROM Bars JOIN Countries ON " + second_command + " ORDER BY " + third_command + " " + forth_command + " LIMIT " + fifth_command
        else:
            query = "SELECT SpecificBeanBarName, Company, EnglishName, Rating, CocoaPercent, BroadBeanOriginId" + " FROM Bars JOIN Countries ON " + second_command + " ORDER BY " + third_command + " LIMIT " + fifth_command
    print(query)
    return query

def bars_origin_query(originid):
    query = """
    SELECT EnglishName
    FROM Bars
    JOIN Countries
        ON BroadBeanOriginId = Countries.Id
    WHERE BroadBeanOriginId =
    """ + str(originid)
    return query
    
def companies_query(first_command, second_command, third_command, forth_command, fifth_command):
    if first_command:
        if forth_command:
            query = "SELECT Company, EnglishName, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " " + first_command + " GROUP BY Company HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " " + forth_command + " LIMIT " + fifth_command
        else:
            query = "SELECT Company, EnglishName, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " " + first_command + " GROUP BY Company HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " LIMIT " + fifth_command
    else:
        if forth_command:
            query = "SELECT Company, EnglishName, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " GROUP BY Company HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " " + forth_command + " LIMIT " + fifth_command
        else:
            query = "SELECT Company, EnglishName, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " GROUP BY Company HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " LIMIT " + fifth_command
    print(query)   
    return query

    
def countries_query(first_command, second_command, third_command, forth_command, fifth_command):
    if first_command:
        if forth_command:
            query = "SELECT EnglishName, Region, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " " + first_command + " GROUP BY EnglishName HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " " + forth_command + " LIMIT " + fifth_command
        else:
            query = "SELECT EnglishName, Region, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " " + first_command + " GROUP BY EnglishName HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " LIMIT " + fifth_command
    else:
        if forth_command:
            query = "SELECT EnglishName, Region, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " GROUP BY EnglishName HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " " + forth_command + " LIMIT " + fifth_command
        else:
            query = "SELECT EnglishName, Region, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " GROUP BY EnglishName HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " LIMIT " + fifth_command
    print(query)    
    return query

    
def regions_query(second_command, third_command, forth_command, fifth_command):
    if forth_command:
        query = "SELECT Region, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " GROUP BY Region HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " " + forth_command + " LIMIT " + fifth_command
    else:
        query = "SELECT Region, " + third_command + " FROM Bars JOIN Countries ON " + second_command + " GROUP BY Region HAVING COUNT(*) > 4 " +"ORDER BY " + third_command + " LIMIT " + fifth_command
    print(query)    
    return query


def categorize_command(command):
    parsed_command = command.split(' ')
    if parsed_command[0] == 'bars':
        return 1
    elif parsed_command[0] == 'companies':
        return 2
    elif parsed_command[0] == 'countries':
        return 3
    elif parsed_command[0] == 'regions':
        return 4

def parse_command(command):
    parsed_command = command.split(' ')
    for command in parsed_command:
        command.strip()
    return parsed_command

def first_command_query(parsed_command):
    ''' Generate the first set of command option query: none(default)/country/region.
    
    Parameters
    ----------
    parsed_command: string
    
    Returns
    -------
    first_command: string
    '''
    for option in parsed_command:
        if 'country' or 'region' in option:
            if 'country' in option:
                return "WHERE Alpha2 = '" + option.split('=')[1] + "'"
            elif 'region' in option:
                return "WHERE Region = '" + option.split('=')[1] + "'"
        else:
            return ''

def second_command_query(parsed_command):
    ''' Generate the second set of command option query: sell(default)/source.
    
    Parameters
    ----------
    parsed_command: string
    
    Returns
    -------
    second_command: string
    '''
    for option in parsed_command:
        if 'sell' in option:
            second_command = "CompanyLocationID = Countries.Id"
            break
        elif 'source' in option:
            second_command =  "BroadBeanOriginID = Countries.Id"
            break
        else:
            second_command = "CompanyLocationID = Countries.Id"
    
    return second_command


def third_command_query(parsed_command):
    ''' Generate the third set of command option query: ratings(default)/cocoa/num_of_bars.
    
    Parameters
    ----------
    parsed_command: string
    
    Returns
    -------
    second_command: string
    '''
    for option in parsed_command:
        if 'ratings' in option:
            third_command =  "Rating"
            break
        else:
            if 'cocoa' in option:
                third_command =  "CocoaPercent"
                break
            else:
                third_command = "Rating"
    
    return third_command

def third_agg_command_query(parsed_command):
    ''' Generate the third set of command option query: agg ratings(default)/cocoa/num_of_bars.
    
    Parameters
    ----------
    parsed_command: string
    
    Returns
    -------
    second_command: string
    '''
    for option in parsed_command:
        if 'ratings' in option:
            third_agg_command =  "AVG(Rating)"
            break
        else:
            if 'cocoa' in option:
                third_agg_command =  "AVG(CocoaPercent)"
                break
            elif 'number_of_bars' in option:
                third_agg_command = "COUNT(Company)"
                break
            else:
                third_agg_command = "AVG(Rating)"
    
    return third_agg_command


def forth_command_query(parsed_command):
    ''' Generate the forth set of command option query: top(default)/bottom.
    
    Parameters
    ----------
    parsed_command: string
    
    Returns
    -------
    string
    '''
    for option in parsed_command:
        if 'top' in option:
            forth_command = "DESC"
            break
        elif 'bottom' in option:
            forth_command = ''
            break
        else:
            forth_command = "DESC"
    return forth_command

def fifth_command_query(parsed_command):
    ''' Generate the fifth set of command option query: 10(default).
    
    Parameters
    ----------
    parsed_command: string
    
    Returns
    -------
    fifth_command
    '''
    if parsed_command[-1].isdigit():
        return str(parsed_command[-1])
    else:
        if parsed_command[-2].isdigit():
            return str(parsed_command[-2])
        else:
            return str(10)
    
def make_query(query):
    '''
    Parameters
    ----------
    country: string
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("choc.sqlite")
    cursor = connection.cursor() 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def process_command(command):
    """
    Takes a command string and returns a list of tuples representing records that match the query.

    Parameters
    ----------
    command: string
        a command that would be entered by a user
        
    Returns
    -------
    list: a list of tuples
        records that match the query
    """
    command_type = categorize_command(command)
    parsed_command = parse_command(command)
    
    second_command = second_command_query(parsed_command)
    third_command = third_command_query(parsed_command)
    third_agg_command = third_agg_command_query(parsed_command)
    forth_command = forth_command_query(parsed_command)
    fifth_command = fifth_command_query(parsed_command)
    

    if command_type == 1:
        first_command = first_command_query(parsed_command)
        part_result = make_query(bars_query(first_command,second_command,third_command,forth_command,fifth_command))
        result = []
        for item in part_result:
            origin = make_query(bars_origin_query(item[-1]))
            complete_result = item[:-1] + origin[0]
            result.append(complete_result)
    elif command_type == 2:
        first_command = first_command_query(parsed_command)
        result = make_query(companies_query(first_command,second_command,third_agg_command,forth_command,fifth_command))
    elif command_type == 3:
        first_command = first_command_query(parsed_command)
        result = make_query(countries_query(first_command,second_command,third_agg_command,forth_command,fifth_command))
    else:
        result = make_query(regions_query(second_command,third_agg_command,forth_command,fifth_command))
    return result

def draw_bar_plot(command):
    command_type = categorize_command(command)
    xvals = []
    yvals = []
    result = process_command(command)

    if command_type == 1:
        if 'cocoa' in command:
            for item in result:
                xvals.append(item[0])
                yvals.append(item[4])
        else:
            for item in result:
                xvals.append(item[0])
                yvals.append(item[3])
    elif command_type == 4:
        for item in result:
            xvals.append(item[0])
            yvals.append(item[1])
    else:
        for item in result:
            xvals.append(item[0])
            yvals.append(item[2])
    
    bar_data = go.Bar(x = xvals,y = yvals)
    fig = go.Figure(data = bar_data)
    fig.show()

def bars_result_format(bars):
    row = "{barname:12s}\t{company:12s}\t{location:12s}\t{rating:.1f}\t{cocoa:.0%}\t{origin:<12s}".format
    new_bars = []
    for bar in bars:
        new_bars.append(list(bar))
    
    for bar in new_bars:
        if len(bar[0]) > 12:
            bar[0] = bar[0][:12] + "..."
        
        if len(bar[1]) > 12:
            bar[1] = bar[1][:12] + "..."
        
        if len(bar[2]) > 12:
            bar[2] = bar[2][:12] + "..."
        
        if len(bar[5]) > 12:
            bar[5] = bar[5][:12] + "..."
        print(row(barname=bar[0], company=bar[1], location=bar[2], rating=bar[3], cocoa=bar[4], origin=bar[5])) 

def countries_and_companies_result_format(results,command):
    new_results = []
    for result in results:
        new_results.append(list(result))
    
    for result in new_results:
        if len(result[0]) > 12:
            result[0] = result[0][:12] + "..."
        
        if len(result[1]) > 12:
            result[1] = result[1][:12] + "..."
        
        if 'cocoa' in command:
            row = "{name:12s}\t{location:12s}\t{agg:.0%}".format
        elif 'number_of_bars' in command:
            row = "{name:12s}\t{location:12s}\t{agg:.0f}".format
        elif 'ratings' in command:
            row = "{name:12s}\t{location:12s}\t{agg:.1f}".format
        else:
            row = "{name:12s}\t{location:12s}\t{agg:.1f}".format
        
        print(row(name=result[0], location=result[1], agg=result[2]))

def regions_result_format(results,command):
    new_results = []
    for result in results:
        new_results.append(list(result))
    
    for result in new_results:
        if len(result[0]) > 12:
            result[0] = result[0][:12] + "..."
        
        if 'cocoa' in command:
            row = "{name:12s}\t{agg:.0%}".format
        elif 'number_of_bars' in command:
            row = "{name:12s}\t{agg:.0f}".format
        elif 'ratings' in command:
            row = "{name:12s}\t{agg:.1f}".format
        else:
            row = "{name:12s}\t{agg:.1f}".format
        
        print(row(name=result[0], agg=result[1]))        

def invalid_input_check(command):
    if 'bars' and 'number_of_bars' in command:
        return False
    elif 'companies' and 'sell' in command:
        return False
    elif 'companies' and 'source' in command:
        return False
    elif 'countries' and 'country' in command:
        return False
    elif 'regions' and 'country' in command:
        return False
    elif 'regions' and 'region' in command:
        return False
    elif 'bars' and 'countries' and 'companies' and 'regions' not in command:
        return False
    else:
        return True

def load_help_text():
    with open('help.txt') as f:
        return f.read()

# Part 2 & 3: Implement interactive prompt and plotting. We've started for you!
def interactive_prompt():
    help_text = load_help_text()
    
    while True:
        response = input('Enter a command: ')

        if response == 'help':
            print(help_text)
            continue
        elif response == 'exit':
            print('bye')
            exit()
        else:
            if(invalid_input_check(response)):
                if 'barplot' in response:
                    draw_bar_plot(response)
                else:
                    command_type = categorize_command(response)
                    if command_type == 1:
                        bars_result_format(process_command(response))
                    elif command_type == 4:
                        regions_result_format(process_command(response),response)
                    else:
                        countries_and_companies_result_format(process_command(response),response)
            else:
                print('Command not recognized: ' + str(response))
    


# Make sure nothing runs or prints out when this file is run as a module/library
if __name__=="__main__":
    interactive_prompt()
    
