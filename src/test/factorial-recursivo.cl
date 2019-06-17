class Factorial {
	factorial(n : Int) : Int {
		if n < 2 then 
			1
		else
			n * factorial(n - 1)
		fi
	};
};

class Main inherits IO {
	test : Factorial;
	main() : IO {{
		test <- new Factorial;
		out_int((test.factorial(5) + test.factorial(5)) / 5);
	}};
};