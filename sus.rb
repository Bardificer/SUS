require 'net/http'
require 'json'
require 'uri'
array_in=ARGV
#USAGE
# sus.rb <username> <password> <ip>

#DEFINE TARGET
uri = URI.parse("http://localhost:3000/submit")

#PREPARE JSON
header = {'Content-Type': 'text/json'}
submission = {submission: {
                user: array_in[0],
                pass: array_in[1],
                src: array_in[2]
}}

#CREATE HTTP OBJECT
http = Net::HTTP.new(uri.host, uri.port)
request = Net::HTTP::Post.new(uri.request_uri, header)
request.body = submission.to_json

#SEND IT
response = http.request(request)
puts("Output:")
puts(submission)
