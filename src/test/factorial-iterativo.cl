class A{
	factorial(n:Int):Int{{
	d <- 1;
	while 2 <= n 
		loop{
		d <- d * n;
		n <- n - 1;
		}
		pool;
	d;
	}};
};
class B inherits A{
	print(n: Int):IO{
		(new IO).out_int(n)
	};
};

class Main{
	main(): IO{{
	(new IO).out_string("Factorial de 5: \n");
	b <- new B;
	b.print(b.factorial(5));
	}};
};