{ rev    ? "c88e3f57f13d144ce37a4814dc92d5fc36f73174"             # The Git revision of nixpkgs to fetch
, sha256 ? "0fmv1mzak2b7pkxpw1vcf5blsw472jy65jqlpamvhjnhv5zgmb9r" # The SHA256 of the downloaded data
, system ? builtins.currentSystem                                 # This is overridable if necessary
}:

import (builtins.fetchTarball {
  url = "https://github.com/tuuzdu/airapkgs/archive/${rev}.tar.gz";
  inherit sha256;
}) { inherit system; }
