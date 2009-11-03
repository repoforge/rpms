# $Id$
# Authority: dag

%define real_version 0_9_1

Summary: Hymn allows you to free your iTunes purchases
Name: hymn
Version: 0.9.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://hymn-project.org/

Source: http://hymn-project.org/download/JHymn_%{real_version}_source.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Hymn allows you to free your iTunes Music Store purchases from
their DRM restrictions with no sound quality loss. These songs
can then be played outside of the iTunes environment, even on
operating systems not supported by iTunes.

%prep
%setup -n JHymn

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
%doc AUTHORS ChangeLog doc/*.png doc/hymn-manual* NEWS README THANKS
%{_bindir}/hymn

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Updated to release 0.9.1.

* Sun Aug 01 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package. (using DAR)
