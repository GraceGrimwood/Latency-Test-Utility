# Latency Test Utility (LatUtil)

<h3>A simple Python latency testing script.</h3>

<h4>How it works:</h4>

The tool pings all of the above servers and then averages the time taken to receive a response from each. It then writes the data to a CSV file.

Pings <i>8.8.8.8</i>, <i>8.8.4.4</i>, <i>139.130.4.5</i>, <i>208.67.222.222</i>, <i>208.67.220.220</i>, of which the first two are Google's DNS servers, the second is a Telstra Australia gateway (we were with Orcon NZ when I wrote this tool, and they use Telstra servers), and the last two are OpenDNS servers.

<h4>System Requirements:</h4>

This tool uses Windows-specific commands to ping (using CMD), so it won't work on GNU/Unix systems without modification.

<h4>Attribution/License:</h4>

GNU GPLv3 (For more info, see the License file.)

This is a pretty basic script, so feel free to use it and modify it. You don't need to credit me, but if you wanted to that would be awesome.
