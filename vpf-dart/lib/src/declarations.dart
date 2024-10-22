part of 'package.dart';


/// Organization declaration.
class _Organization {
	static _Organization fromJSON(Map<String, String> data) {
		return _Organization(data["name"] as String, data["id"] as String);
	}

	String name;
	String id;

	_Organization(this.name, this.id);
}


class _Package {
	static _Package fromJSON(Map<String, String> data) {
		if(data.isEmpty) {
			throw exceptions.DeclarationMalformed();
		}

		for (var key in ["name", "version", "license"]) {
			if(!data.containsKey(key)) {
				throw exceptions.DeclarationKeyMissing(key);
			}
		}

		return _Package(
			data["name"] as String, 
			data["version"] as String,
			data["license"] as String,
		);
	}

	String name;
	String version;
	String license;

	/// Initiate package from raw values
	_Package(this.name, this.version, this.license);
}


/// General VPF declaration.
class VpfDeclaration {
	static VpfDeclaration fromJson(Map<String, dynamic> declaration) {
		for (var key in ["organization", "package"]) {
		  if(!declaration.containsKey(key)) {
				throw exceptions.DeclarationKeyMissing(key);
			}
		}

		final organization = _Organization.fromJSON(declaration["organization"] as Map<String, String>);
		final package = _Package.fromJSON(declaration["package"] as Map<String, String>);

		return VpfDeclaration(organization, package);
	}

	/// General organization information
	final _Organization organization;

	/// Package meta information
	final _Package package;

	// ignore: library_private_types_in_public_api
	VpfDeclaration(this.organization, this.package);
}
