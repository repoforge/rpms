# $Id$
# Authority: dag

%define xmms_generaldir %(xmms-config --general-plugin-dir)

Summary: Reports XMMS status via named pipe
Name: xmms-infopipe
Version: 1.3
Release: 2.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.beastwithin.org/users/wwwwolf/code/xmms/infopipe.html

Source: http://www.beastwithin.org/users/wwwwolf/code/xmms/xmms-infopipe-1.3.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel

%description
XMMS InfoPipe is a plugin that reports XMMS status via named pipe.
Useful if you want to add interesting real-time information for a
personal web page, or a web cam page.

%prep
%setup

%{__perl} -pi.orig -e 's|(fread \(\$info,) 261\)|$1 2048)|' applications/xmms-info.php

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{xmms_generaldir}"

%{__mv} -f %{buildroot}%{xmms_generaldir}/libinfopipe-?.?.so.?.?.? %{buildroot}%{xmms_generaldir}/libinfopipe.so

chmod 0644 applications/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc applications/*.php applications/*.pl AUTHORS ChangeLog COPYING INSTALL NEWS README
%{xmms_generaldir}/libinfopipe.so
%exclude %{xmms_generaldir}/libinfopipe.a
%exclude %{xmms_generaldir}/libinfopipe.la
%exclude %{xmms_generaldir}/libinfopipe-?.?.so.*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-2.2
- Rebuild for Fedora Core 5.

* Mon Dec 06 2004 Dag Wieers <dag@wieers.com> - 1.3-2
- Exclude docs from find-requires.

* Sat Aug 14 2004 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
