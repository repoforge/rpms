# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

Summary: free vector drawing application
Name: gestalter
Version: 0.7.6
Release: 1.2%{?dist}
License: GPL
Group: Applications/Editors
URL: http://www.linotux.ch/gestalter/

Source: http://www.linotux.ch/gestalter/gestalter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2.0, gnome-libs >= 1.4.0, gcc-c++
BuildRequires: glib-devel >= 1.2.0, gtkmm2-devel >= 2.0.0
BuildRequires: gdk-pixbuf-devel >= 0.18.0, libsigc++-devel >= 1.0.0
BuildRequires: expat-devel >= 1.95.0, freetype-devel >= 2.0.0, libxml-devel
#%{?rh8:BuildRequires: gtkmm2-devel >= 2.0.0, gnomemm-devel >= 2.0.0}
#%{?rh7:BuildRequires: gtkmm-devel >= 1.2.0, gnomemm-devel >= 1.2.1}
%{?fc4:BuildRequires: libgnomemm26-devel}

%description
Gestalter is a free vector drawing program. The user interface is loosly
modelled after the famous Illustrator (tm) by Adobe. The central
element is the Bezier curve used as a base part for almost every other
object. Complex paths are possible, compound paths can be constructed,
grouping of elements is enabled and everything can be screened by a mask.
The object model is multi-layered.

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
%doc COPYING README
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.6-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.6-1
- Updated to release 0.7.6.

* Sat Oct 25 2003 Dag Wieers <dag@wieers.com> - 0.6.7-0
- Updated to release 0.6.7.

* Sun Oct 19 2003 Dag Wieers <dag@wieers.com> - 0.6.6-0
- Updated to release 0.6.6.

* Sat Sep 20 2003 Dag Wieers <dag@wieers.com> - 0.6.5-0
- Updated to release 0.6.5.

* Fri May 16 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Initial package. (using DAR)
