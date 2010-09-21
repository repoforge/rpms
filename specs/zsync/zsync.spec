# $Id$
# Authority: dag
# Upstream: Colin Phipps <cph@moria.org.uk>

Summary: Partial/differential file transfer client over HTTP
Name: zsync
Version: 0.6.2
Release: 1%{?dist}
License: Artistic License v2
Group: Applications/Internet
URL: http://zsync.moria.org.uk/

Source: http://zsync.moria.org.uk/download/zsync-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
zsync is a file transfer program. It allows you to download a file from
a remote server, where you have a copy of an older version of the file
on your computer already. zsync downloads only the new parts of the file.

zsync uses the same algorithm as rsync. However, where rsync is designed
for synchronising data from one computer to another within an organisation,
zsync is designed for file distribution, with one file on a server to be
distributed to thousands of downloaders. zsync requires no special server
software just a web server to host the files and imposes no extra load on
the server, making it ideal for large scale file distribution.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README
%doc %{_mandir}/man1/zsync.1*
%doc %{_mandir}/man1/zsyncmake.1*
%{_bindir}/zsync
%{_bindir}/zsyncmake
%exclude %{_docdir}/zsync/

%changelog
* Tue Sep 21 2010 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Tue Jan 27 2009 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Sun Jul 09 2006 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Updated to release 0.4.3.

* Thu Jul 14 2005 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Initial package. (using DAR)
