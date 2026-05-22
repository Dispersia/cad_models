{
  description = "build123d dev environment with uv";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
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
      };
    };
}
