class Main inherits IO {
	main() : IO {{
		a <- in_int();
		b <- in_int();
		out_int(a + b);
		out_string("\n");
		a_s <- "Hola, ";
		b_s <- in_string();
		out_string(a_s.concat(b_s));
	}};
};