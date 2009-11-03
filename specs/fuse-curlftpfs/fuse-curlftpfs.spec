# $Id$
# Authority: dag

%define real_name curlftpfs

Summary: FUSE filesystem for accessing FTP hosts using libcurl
Name: fuse-curlftpfs
Version: 0.9.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://curlftpfs.sourceforge.net/

Source: http://dl.sf.net/curlftpfs/curlftpfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel >= 7.15.2, fuse-devel, glib2-devel
Requires: fuse

Provides: curlftpfs = %{version}-%{release}
Obsoletes: curlftpfs <= %{version}-%{release}

%description
curlftpfs is a filesystem for accessing FTP hosts based on FUSE and
libcurl. It features SSL support, connecting through tunneling HTTP
proxies, and automatically reconnecting if the server times out.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/curlftpfs.1*
%{_bindir}/curlftpfs

%changelog
* Thu Sep 13 2007 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (using DAR)
