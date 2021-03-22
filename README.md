# hypixel-skyblock-coins-per-bit
A cmd tool to get coins per bit

# How to use
##### Make sure python 3 is installed
##### Make sure request library is also installed, if not, you can install it with `pip install requests` if you downloaded python and checked "Add to Path

## flags
#####  -h --help for help
#####  -n value --name value item name(instead of space use - and instead of - use _ )
#####  -b value --bits  amount of bits required to buy item from bits shop
#####  -k  --key  hypixel API key
#####  -o --output display update status( "Finished searching page " )

### Example for god potion

##### python main.py -n God-Potion -b 1500 -k your-hypixel-api-key -o
