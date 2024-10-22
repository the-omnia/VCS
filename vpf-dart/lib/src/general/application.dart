import 'dart:io' as io;

/// Wrapper around compiled applications of [VpfPackage].
class Application {
	String _name;
	String _location;
	String _version;

	/// Name of application, without prefixes
	get name => _name;

	/// Location of application, not symlink
	get location => _location;

	/// Version of application
	get version => _version;

	/// Execute application
	void run() {
		// final process = io.Process.run("", [], runInShell: false);
	}

	/// Check if aplication is stable.
	void check() {
		for(String segment in [ "Executables", "Resources", "Logs" ]) {
			final direcotry = io.Directory.fromUri(Uri.directory('$_location/$segment'));
			if(!direcotry.existsSync()) {}  // TODO: Throw here error when segment is missing
		}

		// Checks for application element
		final file = io.File('$_location/Executables/app');
		if(!file.existsSync()) {}  // TODO: throw here error when application file is missing
		// TODO: Add here checks for executable
	}

	Application(this._name, this._location, this._version);
}
