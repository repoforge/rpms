# $Id$
# Authority: dag

%define real_version 0.6pre3

Summary: GNOME Photo Printer
Name: gpp
Version: 0.6.5
Release: 1.2%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://www.fogman.de/gpp/

Source: http://www.fogman.de/gpp/gpp-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel libgnomeprintui-devel libglade-devel
Requires: libgnomeui libgnomeprintui libglade

%description
Gnome Photo Printer is intended for printing photos in an easy way.
Just drag your Photos from Nautilus to the Gnome Photo Printer window
and drop it.  Make some selections like Photo or Paper size, hit Preview
or  Print , and see your pictures printed.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/gnome-photo-printer/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.5-1.2
- Rebuild for Fedora Core 5.

* Fri Feb 11 2005 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Updated to release 0.6.5.

* Sun Jan 25 2004 Dag Wieers <dag@wieers.com> - 0.6-0.pre3
- Initial package. (using DAR)
