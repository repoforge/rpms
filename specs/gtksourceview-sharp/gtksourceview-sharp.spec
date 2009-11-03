# $Id$
# Authority: dag

Summary: C# wrapper for GtkSourceView
Name: gtksourceview-sharp
Version: 0.5
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://go-mono.com/

Source: http://www.go-mono.com/packagers/gtksourceview-sharp/gtksourceview-sharp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel
BuildRequires: atk-devel
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: gtk-sharp >= 0.93
BuildRequires: gtk-sharp-gapi >= 0.93
BuildRequires: gtksourceview-devel >= 0.7
BuildRequires: libart_lgpl-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libxml2-devel
BuildRequires: mono-devel
BuildRequires: pango-devel
BuildRequires: pkgconfig
Requires: gtksourceview >= 1.0

%description
C# wrapper for GtkSourceView

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}" \
	GACUTIL_FLAGS="/package gtk-sharp /root %{buildroot}%{_libdir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README
%{_datadir}/gtksourceview-1.0/
%exclude %{_datadir}/gtksourceview-1.0/language-specs/vbnet.lang
%{_datadir}/mime-info/gtksourceview-sharp.*
%dir %{_libdir}/monodoc/
%dir %{_libdir}/monodoc/sources/
%{_libdir}/monodoc/sources/gtksourceview-sharp-docs*
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/gac/
%{_libdir}/mono/gac/gtksourceview-sharp/
%{_libdir}/mono/gtk-sharp/
%{_libdir}/pkgconfig/gtksourceview-sharp.pc
%dir %{_datadir}/gapi/
%{_datadir}/gapi/gtksourceview-api.xml

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
