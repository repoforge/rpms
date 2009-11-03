# $Id$
# Authority: dag

%define xmms_inputdir %(xmms-config --input-plugin-dir)

Summary: XMMS input plugin to play shorten (.shn) files
Name: xmms-shn
Version: 2.4.0
Release: 1.2%{?dist}
License: Distributable
Group: Applications/Multimedia
URL: http://www.etree.org/shnutils/xmms-shn/

Source: http://www.etree.org/shnutils/xmms-shn/source/xmms-shn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel, gtk+-devel, gcc-c++
Requires: xmms

%description
XMMS input plugin to play shorten (.shn) files. As of version 2.0,
xmms-shn no longer depends on an external shorten executable to
function. However, to take advantage of the real-time seeking
capabilities built into version 2.x, you have to seek-enable your
.shn's with the new version 3 of shorten.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	libdir="%{xmms_inputdir}" \
	DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README doc/CREDITS doc/LICENSE.shorten
%exclude %{xmms_inputdir}/*.la
%{xmms_inputdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.0-1.2
- Rebuild for Fedora Core 5.

* Wed Jul 14 2004 Dag Wieers <dag@wieers.com> - 2.4.0-1
- Initial package. (using DAR)
