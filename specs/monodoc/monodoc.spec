# $Id$
# Authority: dag

Summary: C# documentation browser
Name: monodoc
Version: 1.0.5
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.go-mono.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.go-mono.org/archive/monodoc-%{version}.tar.gz
Patch0: monodoc-fix-gac.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono-core, mono-web, gtk-sharp-gapi
Requires: mono-core, gtkhtml3 >= 3.0, libglade2-devel, gtk2-devel, 

%description
Monodoc is a documentation browser for the Mono Project. It's written
in C# using the GTK# libraries.

%prep
%setup
%patch

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
%{_datadir}/applications/monodoc.desktop
%{_datadir}/pixmaps/monodoc.png

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.11-0
- Initial package. (using DAR)
