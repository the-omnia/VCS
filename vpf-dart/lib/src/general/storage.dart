import 'package:vpf/general.dart';
import 'package:vpf/src/general/library.dart';

/// Place where all [Application]'s and [Library]'s goes.
class Storage {
	final String _location;

	get location => _location;
	
	Storage(this._location);

	/// Install new application.
	/// 
	/// Installs new [application] in system, where it should be. If [systemWide] is provided, then will attempt to
	/// install [application] as part of system (following all condtions and etc).
	void installApplication(
		Application application, 
		{ 
			bool systemWide = false,
		}
	) {
	}

	/// Install new library entity.
	void installLibrary(Library library) {}
}
