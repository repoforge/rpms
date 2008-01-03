# $Id$
# Authority: dries

Summary: Dynamips Configuration Generator
Name: dynagen
Version: 0.10.1
Release: 1
License: GPL
Group: Applications/Emulators
URL: http://www.dynagen.org/

Source: http://dl.sf.net/dyna-gen/dynagen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: python, dynamips

%description
Dynagen is a front-end for use with the Dynamips Cisco router emulator. It 
uses an INI-like configuration file to provision Dynamips emulator networks. 
It takes care of specifying the right port adapters, generating and matching 
up those pesky NIO descriptors, specifying bridges, frame-relay, ATM switches, 
etc. It also provides a management CLI for listing devices, suspending and 
reloading instances, determining and managing idle-pc values, performing 
packet captures, etc. 

%prep
%setup
%{__perl} -pi.orig -e 's|/usr/bin/env|/bin/env|g;' dynagen *.py
%{__cat}  <<EOF >dynagen-shellscript
#!/bin/bash
PYTHONPATH=%{_datadir}/dynagen python %{_datadir}/dynagen/dynagen \$@
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} %{buildroot}%{_datadir}/dynagen
%{__install} -m0755 dynagen-shellscript %{buildroot}%{_bindir}/dynagen
%{__install} -m0755 configobj.py configspec console.py dynagen dynagen.ini dynamips_lib.py validate.py %{buildroot}%{_datadir}/dynagen/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README.txt
%doc docs/* sample_labs
%{_bindir}/dynagen
%{_datadir}/dynagen/

%changelog
* Thu Jan  3 2008 Dries Verachtert <dries@ulyssis.org> - 0.10.1-1
- Initial package.
