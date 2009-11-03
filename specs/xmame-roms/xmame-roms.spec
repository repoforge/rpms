# $Id$
# Authority: matthias
# Dist: nodist

Summary: Freely available ROMs to use with xmame
Name: xmame-roms
Group: Applications/Emulators
Version: 1.0
Release: 1%{?dist}
License: Freeware
URL: http://www.mame.net/downmisc.html
Source0: http://www.mame.net/roms/polyplay.zip
Source1: http://www.mame.net/roms/robby.zip
Source2: http://www.mame.net/roms/gridlee.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmame
BuildArch: noarch
BuildRequires: unzip

%description
This package contains 3 arcade games that are freely available:
- Gridlee © 1983 Videa.
- Poly-Play © 1985 VEB Polytechnik Karl-Marx-Stadt.
- Robby Roto © 1981 Bally Midway, © 1999 Jay Fenton.


%prep


%build


%install
%{__rm} -rf %{buildroot}

# Install the ROMs
%{__mkdir_p} %{buildroot}%{_datadir}/xmame/roms/
%{__install} -p -m0644 %{SOURCE0} %{SOURCE1} %{SOURCE2} \
    %{buildroot}%{_datadir}/xmame/roms/


%clean
%{__rm} -rf %{buildroot}


%files
%attr(644, root, games) %{_datadir}/xmame/roms/*.zip


%changelog
* Thu Nov 25 2004 Matthias Saou <http://freshrpms.net/> 1.0-1
- Change the dependency from xmame-bin to xmame.

* Thu Aug 26 2004 Matthias Saou <http://freshrpms.net/> 1.0-0
- Split off the roms from the main xmame source package at last, it will save
  unnecessary downloads since they don't change much.

