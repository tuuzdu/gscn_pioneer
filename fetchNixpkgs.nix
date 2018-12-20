{ rev    ? "005c3812ca6e1525103a0a18e927d3c052e9fe17"             # The Git revision of nixpkgs to fetch
, sha256 ? "0w0qfsmcqdilj9c6jxx89q7jlc7bl25zlapfk8djn0hl7vgab2ik" # The SHA256 of the downloaded data
, system ? builtins.currentSystem                                 # This is overridable if necessary
}:

import (builtins.fetchTarball {
  url = "https://github.com/tuuzdu/airapkgs/archive/${rev}.tar.gz";
  inherit sha256;
}) { inherit system; }
