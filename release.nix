{ nixpkgs ? import ./fetchNixpkgs.nix { } }:

rec {
  gscn_pioneeer = nixpkgs.callPackage ./default.nix { };
}
