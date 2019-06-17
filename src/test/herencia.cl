class Base {
	base : IO <- new IO;
	getBase() : IO {
		base
	};
};
class Parent inherits Base {
	child : String <- "Soy Child\n";
	f() : IO {
		getBase().out_string("f en Parent\n")
	};
};
class Child inherits Parent {
	f() : IO {
		getBase().out_string("f en Child\n")
	};
};

class Main inherits IO {
	main() : IO {{
		io <- new IO;
		child <- new Child;
		parent <- new Parent;
		child.f();
		parent.f();
		parent <- child;
		parent.f();
		parent@Parent.f();
		io.out_string("Listo!\n");
	}};
};