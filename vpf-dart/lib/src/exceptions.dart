/// General error for all kinds of VPF errors/exceptions.
/// 
/// Since:
/// 	0.1.0
/// 
/// Version:
/// 	0.1.0
class VpfException extends Error {}


class DeclarationError extends VpfException {}

/// Error thrown when Vpf declaration is missing.
class DeclarationMissing extends DeclarationError {}

/// Error thrown when declaration is malformed.
class DeclarationMalformed extends VpfException {}

/// Error thrown when one of important keys is missing.
class DeclarationKeyMissing extends DeclarationMalformed {
	String key;

	DeclarationKeyMissing(this.key);
}
