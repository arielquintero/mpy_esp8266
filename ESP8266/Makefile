PORT = /dev/tty.wchusbserial141110
AMPY = ampy -p $(PORT)
MPYCROSS = mpy-cross

SRC = \
	cSensor.py \
	cNetwork.py

OBJ = $(SRC:.py=.mpy)

STATIC = main.py boot.py

%.mpy: %.py
	$(MPYCROSS) -o $@ $<

all: $(OBJ)

install: .lastbuild

.lastbuild: $(OBJ) $(STATIC)
	set -x; for src in $?; do $(AMPY) put $$src; done
	date > .lastbuild


.PHONY: reset clean

reset:
	$(AMPY) reset

clean:
	rm -f .lastbuild $(OBJ)
