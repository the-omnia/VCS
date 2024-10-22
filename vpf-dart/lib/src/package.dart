import 'dart:convert' as json;
import 'dart:io' as io;

import 'exceptions.dart' as exceptions;

part 'declarations.dart';


/// General container for VpfPackage
class VpfPackage {
	/// Load VPF package from local path.
	/// 
	/// Method used for loading package from [path], where it must point to directory, without anything else.
	/// When declaration file is missing in fp, then [VpfDeclarationMissing] is thrown.
	/// 
	/// Since:
	/// 	0.1.0
	static VpfPackage fromPath(String path) {
		final package_declaration_path = "${path}/vpf.json";

		final declaration_file = io.File(package_declaration_path);
		if(declaration_file.existsSync()) {
			throw exceptions.DeclarationMissing();
		}

		final data = json.jsonDecode(declaration_file.readAsStringSync()) as Map<String, dynamic>;

		final declaration = VpfDeclaration.fromJson(data);

		return VpfPackage(path, declaration.organization.name);
	}

	/// Location of package.
	String _location;

	/// Name of package
	late String _name;

	String get location => _location;

	/// Setter, with moving of package location.
	set location(String another) => _movePackage(another);

 	String get name => this._name;
	
	VpfPackage(
		this._location,
		this._name,
	);

	/// Move package from [location] to [destination].
	void _movePackage(String destination) => throw UnimplementedError("method '_movePackage' is not implemented");
}
