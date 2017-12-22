SRCDIR = src

.PHONY: clean

lc3grade:
	$(MAKE) -C $(SRCDIR) ../lc3grade

clean:
	$(MAKE) -C $(SRCDIR) clean
