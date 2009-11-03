# $Id$
# Authority: dag

%define xmms_generaldir %(xmms-config --general-plugin-dir)

Summary: XMMS plugin to stop playing/quit XMMS/suspend/shutdown at a given time
Name: xmms-goodnight
Version: 0.3.2
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://fiktiv.szgtikol.kando.hu/~folti/src/

Source: http://fiktiv.szgtikol.kando.hu/~folti/src/xmms-goodnight-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel


%description
An XMMS plugin to stop playing/quit XMMS/suspend/shutdown at a given time.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 libgoodnight.so %{buildroot}%{xmms_generaldir}/libgoodnight.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc Changes COPYING README TODO
%{xmms_generaldir}/*.so


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.2-0.2
- Rebuild for Fedora Core 5.

* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 0.3.2-0
- Initial package. (using DAR)
