{ stdenv
, ros_comm
, mkRosPackage
, python3Packages
, mavros
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "gscn_pioneer_mission";
  version = "master";

  src = ./.;

  propagatedBuildInputs = with python3Packages;
  [ mavros ros_comm ];

  meta = with stdenv.lib; {
    description = "Geoscan Pioneer mavros";
    homepage = http://github.com/tuuzdu/gscn_pioneer_mission;
    license = licenses.bsd3;
    maintainers = [ maintainers.tuuzdu ];
  };
}