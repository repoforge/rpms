# $Id$

# Authority: dag

Summary: Simple encryption tool
Name: gcipher
Version: 1.0
Release: 1
License: BSD
Group: Applications/System
URL: http://gcipher.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gcipher/gcipher-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.2
Requires: python >= 2.2

%description
This is a simple encryption tool to work with home-grown encryption algorithms.
It can run as either a GUI, a command-line application, or a network proxy.

%prep
%setup

%{__perl} -pi.orig -e 's|^GLADEDIR = "."$|GLADEDIR = "%{_datadir}/gcipher/lib"|' src/Const.py
%{__perl} -pi.orig -e 's|^# sys.path.append.+$|sys.path.append("%{_datadir}/gcipher/lib")|' src/gcipher

%build
python %{_libdir}/python2.2/compileall.py src

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/applications \
			%{buildroot}%{_mandir}/man1 \
			%{buildroot}%{_datadir}/gcipher/lib/{cipher,ciphergui} \
			%{buildroot}%{_datadir}/gcipher/plugins/{cipher,ciphergui}

%{__install} -m0644 gcipher.1 %{buildroot}%{_mandir}/man1/

%{__install} -m0755 src/gcipher %{buildroot}%{_bindir}
%{__install} -m0644 src/gcipher.desktop %{buildroot}%{_datadir}/applications/gnome-gcipher.desktop
%{__install} -m0644 src/*.{py,pyc,glade,gladep} %{buildroot}%{_datadir}/gcipher/lib/

%{__install} -m0644 src/cipher/*.{py,pyc} %{buildroot}%{_datadir}/gcipher/lib/cipher/
%{__install} -m0644 src/ciphergui/*.{py,pyc,glade,gladep} %{buildroot}%{_datadir}/gcipher/lib/ciphergui/

%{__install} -m0644 plugins/cipher/*.py %{buildroot}%{_datadir}/gcipher/plugins/cipher/
%{__install} -m0644 plugins/ciphergui/*.py %{buildroot}%{_datadir}/gcipher/plugins/ciphergui/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CONTRIB LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/gcipher/

%changelog
* Thu Jun 26 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
