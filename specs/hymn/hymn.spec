# $Id$
# Authority: dag

Summary: Hymn allows you to free your iTunes purchases
Name: hymn
Version: 0.7.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://hymn-project.org/

#Source: http://hymn-project.org/download.php?dl=dlsrc
Source: hymn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Hymn allows you to free your iTunes Music Store purchases from
their DRM restrictions with no sound quality loss. These songs
can then be played outside of the iTunes environment, even on
operating systems not supported by iTunes.

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
%doc AUTHORS ChangeLog doc/*.png doc/hymn-manual* NEWS README THANKS
%{_bindir}/hymn

%changelog
* Sun Aug 01 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package. (using DAR)
