# hypixel-skyblock-coins-per-bit
A cmd tool to get coins per bit

# How to use
## Requirements
##### Python 3
##### `request` library, if it is not installed, you can install it by typing this command in cmd if "Add to Path" was checked when downloading python: `pip install requests`

## flags
#####  -h --help for help
#####  -n value --name value item name(instead of space use - and instead of - use _ )
#####  -b value --bits  amount of bits required to buy item from bits shop
#####  -k  --key  hypixel API key
#####  -o --output display update status( "Finished searching page " )

### Example for god potion

##### python coins_per_bit.py -n God-Potion -b 1500 -k your-hypixel-api-key -o
