# Order map file symbols from command line

This is a personnal, experimental and dumb tool for ordering map file symbols produced by the ARM GCC linker.
I sometimes use it for tracking symbols memory usage on EFM32 embedded projects. It parses the GCC linker map file and orders symbols by size.
```shell
$ ./order_map_symbols.py --map blink.map 
            variable                    size                filename
     SystemCoreClock                       4    .\obj\system_efm32gg.o
             msTicks                       4           .\obj\blink.o
   clock_setup_state                       4    .\obj\setup_time_app.o
            activity                       7    .\obj\activity_app.o
            pomodoro                      20    .\obj\time_management.o
              alarm2                      20    .\obj\time_management.o
         currentTime                      20    .\obj\time_management.o
$
```
