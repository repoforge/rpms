# $Id$

# Authority: dag

Summary: C# documentation browser.
Name: monodoc
Version: 0.11
Release: 0
License: GPL
Group: Development/Tools
URL: http://www.go-mono.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.go-mono.org/archive/monodoc-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: mono-devel, gtk-sharp
Requires: mono >= 0.30, gtkhtml3 >= 3.0, libglade2-devel, gtk2-devel, 

%description
Monodoc is a documentation browser for the Mono Project. It's written
in C# using the GTK# libraries.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/*
%{_libdir}/*
%{_libdir}/monodoc/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.11-0
- Initial package. (using DAR)
