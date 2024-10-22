import 'package:vpf/general.dart' as general;
import 'package:vpf/src/osx/plist.dart';

/// Wrapper around Apple Darwin application layout.
class Application {
	static Application? fromVpfApplication(general.Application nativeApp) {
		return null;
	}

	/// Read native application and provide it's info as object.
	static Application? readNative(String location) {
		return null;
	}

	late PList _pList;
	get plist => _pList;
}
