# $Id$

# Override libdir for plugin install
%define _libdir /usr/lib/kino-gtk2

Summary: Kino titling plugin
Name: kino-dvtitler
Version: 0.1.1
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://dvtitler.sourceforge.net/
Source0: http://dl.sf.net/dvtitler/dvtitler-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: kino >= 0.7.0
BuildRequires: kino >= 0.7.0, libgnomeui-devel

%description
A GNOME2 titler for Kino that uses fontconfig and the Freetype2 rendering
backend to Pango international text layout. Titles can be animated as well.


%prep
%setup -q -n dvtitler-%{version}


%build
%configure
%{__make} %{_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%exclude %{_libdir}/libdvtitler.la
%{_libdir}/libdvtitler.so*


%changelog
* Mon Nov 22 2004 Matthias Saou <http://freshrpms.net/> 0.1.0-0
- Rename package to kino-dvtitler.

* Mon Jan 19 2004 Dan Dennedy <dan@dennedy.org>	0.1.0-1
- Package created

