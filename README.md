Two and a half years ago, I built some buttons as seen on my
[blog](https://blog.joshgordon.net/the-robots-are-taking-over-theyll-most-likely-kill-us-in-the-morning/).

A while ago (and a while after that) I re-did them to use a particle photon
inside, but couldn't ever get the software going, and the original software for
the original buttons stopped working a while after that. For over two years now
I've been either turning stuff on and off through the web interface, or with a
few buttons on my keyboard, which means my computer needs to be turned on.

A week ago I decided to patch my relaybox to use mqtt for control, and I finally
decided to resurrect the old buttons with the photon in it. Having had frustrations
with the particle cloud in the past, I decided to circumvent that entirely,
and just use mqtt directly from the photon.

Guess what. It works great.

This listens for button presses from the photons and dispatches other messages into
mqtt to turn stuff on and off.
