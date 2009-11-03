# $Id$
# Authority: dag
# Upstream: <kingleo$gmx,at>

%define xmms_generaldir %(xmms-config --general-plugin-dir)
%define real_name real_random

Summary: Plugin for XMMS providing better shuffling
Name: xmms-real-random
Version: 0.3
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://home.pages.at/kingleo/index.php?show=/development/stuff

Source: http://home.pages.at/kingleo/development/stuff/real_random-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel


%description
A plugin for XMMS providing better shuffling.


%prep
%setup -n %{real_name}-%{version}


%build
%configure \
        --enable-shared \
        --libdir="%{xmms_generaldir}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{xmms_generaldir}"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{xmms_generaldir}/*.so
%exclude %{xmms_generaldir}/*.la


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-0.2
- Rebuild for Fedora Core 5.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Updated to release 0.3.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
