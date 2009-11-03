# $Id$
# Authority: dag

Summary: C# documentation browser
Name: monodoc
Version: 1.0.5
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.go-mono.com/

Source: http://www.go-mono.com/archive/%{version}/monodoc-%{version}.tar.gz
Patch: monodoc-fix-gac.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono-core, mono-web, gtk-sharp-gapi
Requires: mono-core, gtkhtml3 >= 3.0, libglade2-devel, gtk2-devel, gtk-sharp

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
%{__make} install \
	DESTDIR="%{buildroot}" \
	GACUTIL_FLAGS="/package gtk-sharp /root %{buildroot}%{_libdir}"
%{__ln_s} -f %{_libdir}/mono/gac/monodoc/*/monodoc.dll %{buildroot}%{_libdir}/mono/gtk-sharp/monodoc.dll

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/mod
%{_bindir}/monodoc
%{_libdir}/monodoc/
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/gac/
%{_libdir}/mono/gac/monodoc/
%{_libdir}/mono/gtk-sharp/
%{_libdir}/pkgconfig/monodoc.pc
%{_datadir}/applications/monodoc.desktop
%{_datadir}/pixmaps/monodoc.png

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.11-0
- Initial package. (using DAR)
