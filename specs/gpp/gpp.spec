# $Id$

# Authority: dag

%define rversion 0.6pre3

Summary: GNOME Photo Printer
Name: gpp
Version: 0.6
Release: 0.pre3
License: GPL
Group: Applications/Publishing
URL: ?

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.fogman.de/gpp/%{name}-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libgnomeui-devel libgnomeprintui-devel libglade-devel 
Requires: libgnomeui libgnomeprintui libglade 

%description
Gnome Photo Printer is intended for printing photos in an easy way.
Just drag your Photos from Nautilus to the Gnome Photo Printer window
and drop it.  Make some selections like Photo or Paper size, hit Preview
or  Print , and see your pictures printed.

%prep
%setup -n %{name}-%{rversion}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#make install DESTDIR=${RPM_BUILD_ROOT}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/gnome-photo-printer/

%changelog
* Sun Jan 25 2004 Dag Wieers <dag@wieers.com> - 0.6-0.pre3
- Initial package. (using DAR)
