{ rev    ? "06d5c06514d5548a1d8cbabc559231ed47513d32"             # The Git revision of nixpkgs to fetch
, sha256 ? "0gp43146wn9k10mkc0lqljv2vkf4zflr2ygwv07f2c5bdk7gifkq" # The SHA256 of the downloaded data
, system ? builtins.currentSystem                                 # This is overridable if necessary
}:

import (builtins.fetchTarball {
  url = "https://github.com/tuuzdu/airapkgs/archive/${rev}.tar.gz";
  inherit sha256;
}) { inherit system; }
