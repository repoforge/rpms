# Authority: dag

Summary: Python-based vector drawing program.
Name: sketch
Version: 0.6.14
Release: 1
License: LGPL, Python style
Group: Applications/Multimedia
URL: http://sketch.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/sketch/sketch-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: python-imaging >= 1.1
Requires: python >= 1.5.1, python-imaging >= 1.1

%description
Sketch is an interactive X11 vector drawing program. It is written
almost completely in Python, an object oriented interpreted programming
language.

%prep
%setup
mv Pax/README Pax/README.pax
mv Pax/COPYING Pax/COPYING.pax
mv Filter/COPYING Filter/COPYING.filter
mv Filter/README Filter/README.filter

%build
./setup.py configure --with-nls
./setup.py build

%install
strip -S Pax/*.so
strip -S Filter/*.so
strip -S Sketch/Modules/*.so
./setup.py install --prefix="%{buildroot}%{_prefix}"

%files
%doc Examples/ Doc/
%doc README INSTALL BUGS CREDITS COPYING TODO PROJECTS FAQ NEWS
%doc Pax/README.pax Pax/COPYING.pax Pax/COPYING.xext
%doc Filter/README.filter Filter/COPYING.filter
%{_libdir}/sketch-%{version}
%{_bindir}/sketch
%{_bindir}/sk2ps
%{_bindir}/skshow

%changelog
* Sat Jan 04 2003 Dag Wieers <dag@wieers.com> - 0.6.14-1
- Updated to 0.6.14.

* Fri Jul 06 2001 Dag Wieers <dag@wieers.com> - 0.6.13
- Initial package.
