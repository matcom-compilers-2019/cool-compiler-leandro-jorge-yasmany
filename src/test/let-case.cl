class A{
	do_if(n:String):String
	{
		if n.length() = 5
			then
				"Es Pequeño\n"
			else
				"Es grande\n"
		fi
	};
};
class B inherits A{
	concat(n:String):String{
		n.concat(" y mas...\n")
	};
};

class C inherits B{
	substring(n:String):String{
		n.substring(0, 6)
	};
};

class Main inherits IO{
	main(): IO{
		let d : Object <- new Object in {
		d <- 5;
		
		case d of
			e : Object => out_string("Es Object de 5\n");
			e : String => out_string("Es String de 5\n");
			e : Int => out_string("Es Int de 5\n");
		esac;
		
		case new C of
			e : A => out_string(e.do_if("Compilacion\n"));
			e : B => out_string(e.concat("Algo"));
		esac;
		out_string((new C).substring("Listo!!!!!!"));
		}
	};
};