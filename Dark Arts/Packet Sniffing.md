# Packet Sniffing

Friendly reminder to go to the career panel tonight!

So, why study networks first? Well, depressingly few people are familir with how computers talk to each other and what kind of data is locked up in the packets being sent.

## The OSI Model

This is the most basic thing that every hacker should know, the 7 layers of transmission.

* Application
* Presentation
* Session
* Transport
* Network
* Data Link
* Physical

Thse layers are all abstracted from each other and only speak through API's. When you hit "send", your computer sends the data down through all 7, the network transmits the data on the physical link layer, and mine works the data all the way back up.

So, let's get started, working our way up!

### Hardware

Stuff like cards, cables, switches. This stuff is below assembly, running on pure machine code. This stuff is unradable to humans.

### Data Link

All this layer does is transfer data between two machines. The lowest thing humans would ever code on. Stuff like the ARP and Ethernet Protocol lives on this layer. The only addresses you see down here are MAC addresses. We can no longer transmit ANY SIGNAL ANY TIME, this layer imposes simple restrictions like basic traffic lights.

### Network

This layer provides addressign and routing. No longer can shit just go wherever it wants, the IP and ICMP protocols live on this layer, routing packets to where they need to go. Nothing on this layer has anything to do with the *nature* of the delivery or the content of the packet. Only the *source* and *destination* are dealt with here, as well as some optional flags that no one is under any duty to read.

### Transport

Now that we know where the packets are going, we need to make sure it delivers reliably, or quickly. Protocols for prioritizing accuracy or speed, like TCP and UDP, live on this layer. No longer can packets just fly through the network, their delivery is now monitored.

Friendly reminder, this stuff was invented in ***1981***, and still fucking works.

### Session

This layer is responsible for maintaining connections.

### Presentation

Encryption, compression, etc.

### Application

HTTP, DNS, Git, literally any fucking network connected program.

Wow, we blew through those last 3 fast.

Anyhow, turns out Ming runs the Wall of Sheep at DEFCON. He shames people who don't encrypt their stuff properly by displaying it on a huge screen. Also, he wrote the first implementation of juice jacking. (those bastards at BlackHat stole 2 years later)

## Anatomy of a Packet

Every network packet is self-sufficient, one of the big reasons the Internet can be decentralized. Packets contain source and destination IP's, a MAC address, the protocol, a self-destruct timer in the event of a lost packet, and of course the payload.

## Basics of Sniffing

This is *not* exhaustive; this is designed to yank the pacifier out of your mouth and get you working on these ```.pcap``` files.

### ```tcpdump```

This program can record and/or analyze packets live on a network. We'll get to this later.

### Wireshark

Similar to tcpdump, but features filtering and a GUI.

### Practice

Download [this](http://www.cs.tufts.edu/comp/116/set0.pcap) file, and run:

```
tcpdump -r set0.pcap
```

Or, if you want to do it live:

```
tcpdump eth0
```

and open your browser. Not too hard.

You can then go through and look at all the information, ports, addresses, the whole 9 yards.

Also, turns out Ming browses ```/g/```.

Now, what if we want to reconstruct the conversation? Simple! WireShark has a contextual option called "Follow TCP Stream". You'll basically get a bunch of protocol info. How do we dig through these files and find the needle in the haystack?

Well, one option is ```ettercap```! Your old friend from those MiTM attacks in high school can also sniff out passwords! Ming's reccommending a pipe to ```grep``` first.

Oh, and a friendly reminder that you should ***NEVER FUCKING LOG IN TO A PASSWORD YOU GOT THIS WAY THAT SHIT IS SUPER FUCKING ILLEGAL***.

Now, let's assume we want to, anyway... First things first, verify it isn't a honeypot. We've captured the IP and the port number, so we can just filter all the packets by that. WireShark lets you filter like this with ```ip.addr==[SOURCE]```. It's then trivial to reconstruct the conversation.
