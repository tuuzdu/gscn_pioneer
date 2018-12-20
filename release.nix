{ nixpkgs ? import ./fetchNixpkgs.nix { } }:

rec {
  de_robonomics = nixpkgs.callPackage ./default.nix { };
}
