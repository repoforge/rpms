# $Id$

# Authority: dag

Summary: The GNOME Fax Application
Name: gfax
Version: 0.5
Release: 0
License: GPL
URL: http://www.cowlug.org/gfax/
Group: Applications/Communications

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cowlug.org/gfax/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Requires: gnome-libs >= 1.2, libglade >= 0.7, python >= 1.5.2

%description
Gfax is a popup tool for easily sending
facsimilies by printing to a fax printer.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir}/gfax \
			%{buildroot}%{_datadir}/pixmaps \
			%{buildroot}%{_datadir}/gnome/apps/Applications
%{__install} -m0755 gfax.py %{buildroot}%{_bindir}/gfax
%{__install} -m0644 *.py *.glade %{buildroot}%{_libdir}/gfax/
%{__install} -m0644 gfax.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/
%{__install} -m0644 gfax.png %{buildroot}%{_datadir}/pixmaps/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog COPYING HACKING TODO
%{_bindir}/*
%{_libdir}/gfax/
%{_datadir}/pixmaps/*.png
%{_datadir}/gnome/apps/Applications/*

%changelog
* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Initial package. (using dar)
