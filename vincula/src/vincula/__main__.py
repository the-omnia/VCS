from argparse import ArgumentParser
from os import getcwd
from sys import argv

from vincula.v import Vincula
from vincula.foundation import Module
from vincula.foundation import Workspace


def init_parser() -> ArgumentParser:
	parser = ArgumentParser("vincula")
	parser.add_argument("--cwd", action="store", default=getcwd())

	# ---> Workspace parser
	sub_commands = parser.add_subparsers(dest="command")
	workspace = sub_commands.add_parser(
		name="workspace", description="Workspace manipulation commands"
	)

	# Info command (workspace)
	w_info_class = workspace.add_subparsers(title="Informational", dest="sub_command")
	w_info_parser = w_info_class.add_parser(
		name="info",
		description="Info about current workspace",
		epilog="Omnia Community",
	)
	w_info_parser.add_argument(
		"--expanded",
		action="store_true",
		default=False,
		help="Expand information about wokspace",
	)

	# ---> Module parser
	module_commands_parser = sub_commands.add_parser(name="module")

	# Info command (modules)
	m_info_class = module_commands_parser.add_subparsers(
		title="Informational", dest="sub_command"
	)
	m_info_parser = m_info_class.add_parser(
		name="info", description="Info about selected module"
	)

	m_info_parser.add_argument("module_name", action="store")

	return parser


def print_module_info(module: Module) -> None:
	print("Module info")

	# General header:
	print("-- General info")
	print(f"  | Name: {module.name}")
	print(f"  | Path: {module.path}")
	print(f"  | Language: {module.language.used_name}")
	print(f"  | Layout: {module.layout.value}")
	print(f"  | Type: {module.type.name}")


def print_workspace_info(w: Workspace, expanded: bool = False):
	print("Workspace information:")

	# Printing organization
	print("-- Organization:")
	print(f"  | ID: {w.__org_id__}")
	print(f"  | Name: {w.__org_name__}")

	# Languages used
	print(f"-- Languages ({len(w.languages)})")
	for i, lang in enumerate(w.languages):
		print(f"  | ({i+1}) {lang.used_name} v{lang.version} ({lang.name})")

	# Plugins
	for i, plug in enumerate(w.languages):
		pass

	# Modules in workspace
	print(f"-- Modules ({len(w.modules)})")
	for i, mod in enumerate(w.modules):
		print(
			f'  |{"-- " if expanded else " "}'
			+ f"({i+1}) {mod.name} - {mod.type.name} @ {mod.path} "
			+ f'using "{mod.language.used_name}"'
		)

		# Expanded information
		if expanded:
			print(f"    | Layout: {mod.layout.value}")


def main() -> int:
	parser = init_parser()

	args = parser.parse_args(argv[1:])

	v = Vincula()
	v.load_workspace(args.cwd)

	print(args)

	if args.command == "workspace" and args.sub_command == "info":
		w = v.workspaces[0]
		print_workspace_info(w, args.expanded)
	elif args.command == "module" and args.sub_command == "info":
		w = v.workspaces[0]
		m = None

		for mod in w.modules:
			if mod.name == args.module_name:
				m = mod

		if m is None:
			print("Module with such name not found")
			return 1

		print_module_info(m)

	return 0


if __name__ == "__main__":
	exit(main())
