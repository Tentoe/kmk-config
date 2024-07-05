{
  inputs = { nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable"; };

  outputs = { self, nixpkgs }:
    let pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in {

      devShell.x86_64-linux =
        pkgs.mkShell {
          buildInputs = with pkgs; [
            python312
            python312Packages.pip
            python312Packages.virtualenv
            pyright
          ];
          shellHook = ''
            virtualenv venv
            source venv/bin/activate
            pip install -r requirements.txt
            # TODO use your board
            circuitpython_setboard 0xcb_helios
          '';
        };

    };
}
