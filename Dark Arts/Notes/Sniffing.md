# Network Sniffing, ARP Poisoning, and MiTM

OK, so Ming just told us a funny story about goatse. Apparently some asshole at defcon made him look at it.

So, how do we efficiently grab traffic from a live network? Well, first it's important to differentiate between the two types of networks:

## Switched Networks

In these networks, packets are only delivered to specific devices, and flow through those. You can quickly see a tiny hole, here, in that the network trusts you not to lie about who you are.

## Unswitched Networks

These networks just don't give a fuck. Packets can go through all devices on the network, *but*, you can only look at your packets. And by only, we mean network policy says "please" and you're on the honor system. And of course the consequences other devices can mete out if they catch you.

So, I think it's pretty obvious what we're doing today...

Let's start with unswitched networks, which is easy, and it's called promiscuous mode.

```
ifconfg [interface] promisc
```

If you can't find the name of your interface, I genuinely have no hope.

In order to prevent sniffing, ALWAYS TRANSMIT ENCRYPTED PACKETS. USE A VPN FOR SENSITIVE DATA. And use a switched network if you can help it, unless Paweł and Harsh show up with too much spare time.

Now, on to switched networks! Our friend ARP poisoning is here to help!

Now, before we start, ARP stands for Address Resolution Protocol, and is used to match IP's with MAC address. There's a utility for accessing it in every *nix-like OS. Using it with the ```-a``` flag will just dump a whole table of domains, IP addresses, and associated MAC addresses. Of course, it's the trivial to have your computer lie and say it's the router. Flood the network until everyone believes your MAC address is the router, not the router itself. This is known as "poisoning the ARP table".

```arpspoof``` is the most basic way to do it, (check the man page), but the poisoning, MiTM, and sniffing are all done by BetterCap, which also comes on Kali, so you can just use that. (use the ```-X``` flag).
