import datetime


def log_init(dt):
    with open('logs.html', 'w') as file:
        file.write(
            '<!DOCTYPE html>\n<html>\n<head>\n<title>Test Results</title>\n</head>\n<body>\n<p><span style="font-size:16px"><span style="font-family:Arial,Helvetica,sans-serif"><strong>Test Results ' + dt + '</strong></span></span></p>\n<style type="text/css">\ntable {width: 100%;margin-bottom: 20px;border: 1px solid #dddddd;border-collapse: collapse;}\ntable th {font-weight: bold;padding: 5px;background: #efefef;border: 1px solid #dddddd;}\ntable td {border: 1px solid #dddddd;padding: 5px;}\n</style>\n<table align="left" border="1" cellpadding="1" cellspacing="1" style="width:100%">\n<tbody>\n<tr>\n<td><span style="font-size:14px"><strong><span style="font-family:Arial,Helvetica,sans-serif">Test</span></strong></span></td>\n<td><span style="font-size:14px"><strong><span style="font-family:Arial,Helvetica,sans-serif">Result</span></strong></span></td>\n<td><span style="font-size:14px"><strong><span style="font-family:Arial,Helvetica,sans-serif">Message</span></strong></span></td></tr>\n')


def passed(test):
    with open('logs.html', 'a') as file:
        file.write(
            '\n<tr><td><span style="font-size:14px"><span style="font-family:Arial,Helvetica,sans-serif">' + test + '</span></span></td><td><span style="font-size:14px"><span style="font-family:Arial,Helvetica,sans-serif"><span style="color:#2ecc71">Passed</span></span></span></td><td><span style="font-size:14px"><span style="font-family:Arial,Helvetica,sans-serif"></span></span></td></tr>\n')


def failed(test):
    with open('logs.html', 'a') as file:
        file.write(
            '\n<tr><td><span style="font-size:14px"><span style="font-family:Arial,Helvetica,sans-serif">' + test + '</span></span></td><td><span style="font-size:14px"><span style="font-family:Arial,Helvetica,sans-serif"><span style="color:#e74c3c">Failed</span></span></span></td><td><span style="font-size:14px"><span style="font-family:Arial,Helvetica,sans-serif"></span></span></td></tr>\n')


def log_write(test):
    with open('logs.html', 'a') as file:
        file.write(
            '\n<tr><td><span style="font-size:14px"><span style="font-family:Arial,Helvetica,sans-serif">' + test + '</span></span></td><td><span style="font-size:14px"><span style="font-family:Arial,Helvetica,sans-serif"><span style="color:#e74c3c">Failed</span></span></span></td><td><span style="font-size:14px"><span style="font-family:Arial,Helvetica,sans-serif"></span></span></td></tr>\n')


def log_stop():
    with open('logs.html', 'a') as file:
        file.write('\n</tbody>\n</table>\n</body>\n</html>')


log_init(dt=str(datetime.datetime.now()))
passed('aaa')
failed('ihdbcdskjhs')
log_stop()