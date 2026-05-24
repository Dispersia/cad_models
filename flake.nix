{
  description = "build123d dev environment with uv";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        isLinux = pkgs.stdenv.isLinux;
      in
      {
        devShells.default = pkgs.mkShell ({
          packages = with pkgs; [
            uv
            python312
            pyright
          ];

          shellHook = ''
            if [ ! -d .venv ]; then
              uv venv .venv --python python3.12
              uv pip install build123d
            fi
            source .venv/bin/activate
          '';
        } // pkgs.lib.optionalAttrs isLinux {
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath (with pkgs; [
            libGL
            libGLU
            libx11
            libxrender
            libxmu
            stdenv.cc.cc.lib
            expat
            zlib
          ]);
        });
      }
    );
}
