# $Id$
# Authority: dag

Summary: Python-based vector drawing program
Name: sketch
Version: 0.6.14
Release: 1.2%{?dist}
License: LGPL, Python style
Group: Applications/Multimedia
URL: http://sketch.sourceforge.net/

Source: http://dl.sf.net/sketch/sketch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-imaging >= 1.1, python-devel, python
BuildRequires: tcl-devel, tk-devel
Requires: python >= 1.5.1, python-imaging >= 1.1

%description
Sketch is an interactive X11 vector drawing program. It is written
almost completely in Python, an object oriented interpreted programming
language.

%prep
%setup
%{__mv} -vf Pax/README Pax/README.pax
%{__mv} -vf Pax/COPYING Pax/COPYING.pax
%{__mv} -vf Filter/COPYING Filter/COPYING.filter
%{__mv} -vf Filter/README Filter/README.filter

%build
./setup.py configure --with-nls
./setup.py build

%install
%{__rm} -rf %{buildroot}
strip -S Pax/*.so
strip -S Filter/*.so
strip -S Sketch/Modules/*.so
./setup.py install --prefix="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Doc/ Examples/
%doc BUGS COPYING CREDITS FAQ INSTALL NEWS PROJECTS README TODO
%doc Pax/COPYING.pax Pax/COPYING.xext Pax/README.pax
%doc Filter/COPYING.filter Filter/README.filter
%{_libdir}/sketch-%{version}
%{_bindir}/sketch
%{_bindir}/sk2ps
%{_bindir}/skshow

%changelog
* Sat Jan 04 2003 Dag Wieers <dag@wieers.com> - 0.6.14-1
- Updated to 0.6.14.

* Fri Jul 06 2001 Dag Wieers <dag@wieers.com> - 0.6.13
- Initial package.
