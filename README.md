

# rpi_mjpg_streamer
Simple MJPG Streaming NodeJS application. 

## Installation

First of all install the prerequisites:

    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get install g++ curl pkg-config libv4l-dev libjpeg-dev build-essential libssl-dev cmake git-core build-essential libjpeg8-dev imagemagick subversion
    $ sudo apt-get autoremove
    $ sudo shutdown -r now

Then we can install motion-jpeg (mjpeg):

     $ cd /usr/src
     $ sudo mkdir mjpg-streamer
     $ sudo chown pi:users mjpg-streamer
     $ cd mjpg-streamer
     $ git clone //github.com/jacksonliam/mjpg-streamer.git .
     $ cd mjpg-streamer-experimental
     $ make
     $ sudo make install

After the compilation, shutdown the pi and attach the camera:

     $ cd /usr/src/mjpg-streamer/mjpg-streamer-experimental/
     $ export LD_LIBRARY_PATH=.
     $ ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 640 -y 480 -fps 20 -ex night"

My RPi has the following IP address: 192.168.20.83 so you can see the camera at http://192.168.20.83:8080/stream.html

## Configuration

The following tweaks are needed in order to make it work:




## Usage



## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
