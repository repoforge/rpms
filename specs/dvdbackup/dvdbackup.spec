# $Id$
# Authority: dag
# Upstream: Olaf Beck <olaf_sc$yahoo,com>

Summary: DVD-create (dvdbackup)
Name: dvdbackup
Version: 0.1.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://dvd-create.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dvd-create.sourceforge.net/dvdbackup-%{version}.tar.gz
BuildRoot: %{_builddir}/%{name}-%{version}-%{release}-root

Requires: libdvdread

%description
DVD-Createxi is a DVD-Video creation framework. It offers you a
framework that enables you to write DVD creation, editing, and
backup software without needing to know all the secrets of
DVD-Video.

%prep
%setup -n %{name}

%build
%{__cc} %{optflags} -ldvdread -ldl src/dvdbackup.c -o dvdbackup

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 dvdbackup %{buildroot}%{_bindir}/dvdbackup

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README
%{_bindir}/dvdbackup

%changelog
* Mon Dec 06 2004 Dag Wieers <dag@wieers.com> - 0.1.1-1
- Initial package. (using DAR)
