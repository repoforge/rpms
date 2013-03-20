# $Id$
# Authority: dag
# Upstream: Romain Coltel <romain,coltel$hsc,fr>

%define real_name dislocker

Summary: FUSE-Filesystem to access BitLocker filesystems
Name: fuse-dislocker
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.hsc.fr/ressources/outils/dislocker/download/

Source: http://www.hsc.fr/ressources/outils/dislocker/download/dislocker.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2
BuildRequires: openssl-devel
Requires: fuse >= 2.2

Obsoletes: dislocker <= %{version}-%{release}
Provides: dislocker = %{version}-%{release}

%description
dislocker has been designed to read BitLocker encrypted partitions under a
Linux system. The driver used to only read volumes encrypted under a Windows 7
system but is now Windows Vista capable.

%prep
%setup -n %{real_name}-pub

%build
%{__make} -C src %{?_smp_mflags} \
    CC="%{__cc}" \
    __RUN_FUSE="1" \
    __RUN_FILE="0" \
    WFLAGS="%{optflags} $(pkg-config fuse --cflags --libs)"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__make} -C src install DESTDIR="%{buildroot}" \
    CC="%{__cc}" \
    __RUN_FUSE="1" \
    __RUN_FILE="0" \
    WFLAGS="%{optflags} $(pkg-config fuse --cflags --libs)" \
    INSTALL_PATH="%{buildroot}%{_bindir}/" \
    MAN_PATH="%{buildroot}%{_mandir}/man1/" \

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%doc %{_mandir}/man1/dislocker.1*
%{_bindir}/dislocker

%changelog
* Tue Sep 11 2012 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
