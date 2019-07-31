# Profess Copyright (c) 2019 Joshua 'joshuas3' Stockin
# <https://github.com/JoshuaS3/profess/>.


# This file is part of Profess.

# Profess is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Profess is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Profess. If not, see <https://www.gnu.org/licenses/>.

newline = "\r\n"
accepted_methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE"] # defined in RFC 7231 in section 4

http11 = "HTTP/1.1"
http20 = "HTTP/2.0"

status_reasons = { # https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml
	# 1xx Informational
	100: "Continue",
	101: "Switching Protocols",
	102: "Processing",
	103: "Early Hints",

	# 2xx Successful
	200: "OK",
	201: "Created",
	202: "Accepted",
	203: "Non-Authoritative Information",
	204: "No Content",
	205: "Reset Content",
	206: "Partial Content",
	207: "Multi-Status",
	208: "Already Reported",
	226: "IM Used",

	# 3xx Redirection
	300: "Multiple Choices",
	301: "Moved Permanently",
	302: "Found",
	303: "See Other",
	304: "Not Modified",
	305: "Use Proxy",
	307: "Temporary Redirect",
	308: "Permanent Redirect",

	# 4xx Client Error
	400: "Bad Request",
	401: "Unauthorized",
	402: "Payment Required",
	403: "Forbidden",
	404: "Not Found",
	405: "Method Not Allowed",
	406: "Not Acceptable",
	407: "Proxy Authentication Required",
	408: "Request Time-out",
	409: "Conflict",
	410: "Gone",
	411: "Length Required",
	413: "Request Entity Too Large",
	414: "Request-URI Too Large",
	415: "Unsupported Media Type",
	416: "Range Not Satisfiable",
	417: "Expectation Failed",
	421: "Misdirected Request",
	422: "Unprocessable Entity",
	423: "Locked",
	424: "Failed Dependency",
	425: "Too Early",
	426: "Upgrade Required",
	428: "Precondition Required",
	429: "Too Many Requests",
	431: "Request Header Fields Too Large",
	451: "Unavailable For Legal Reasons",

	# 5xx Server Error
	500: "Internal Server Error",
	501: "Not Implemented",
	502: "Bad Gateway",
	503: "Service Unavailable",
	504: "Gateway Timeout",
	505: "HTTP Version Not Supported",
	506: "Variant Also Negotiates",
	507: "Insufficient Storage",
	508: "Loop Detected",
	510: "Not Extended",
	511: "Networking Authentication Required"
}

def get_status_reason(status_code):
	try:
		return (status_code, status_reasons[status_code])
	except KeyError:
		if status_code >= 100:
			if status_code < 200: return (status_code, "Informational")
			if status_code < 300: return (status_code, "Successful")
			if status_code < 400: return (status_code, "Redirection")
			if status_code < 500: return (status_code, "Client Error")
			if status_code < 600: return (status_code, "Server Error")
		return (status_code, "Unknown Error")

def format_headers(headers_list):
	header_string = ""
	for header_tuple in headers_list:
		header_name = header_tuple[0]
		header_value = header_tuple[1]
		if len(header_string) > 0:
			header_string += newline
		header_string += header_name + ": " + str(header_value)
	return header_string

def status_line(ver_string, status):
	return ver_string + " " + str(status[0]) + " " + str(status[1]) + newline
