# $Id$
# Authority: dag

Summary: Pack a file in MIME format for mailing and news
Name: mpack
Version: 1.6
Release: 2%{?dist}
License: GPL
Group: Applications/File
URL: http://ftp.andrew.cmu.edu/pub/mpack/

Source: http://ftp.andrew.cmu.edu/pub/mpack/mpack-%{version}.tar.gz
Patch0: mpack-1.6-buildfix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The mpack program encodes the the named file in one or more MIME
messages.  The resulting messages are mailed to one or more
recipients, written to a named file or set of files, or posted 
to a set of newsgroups.  Lighter than Metamail - unmaintained

About MIME: See RFC 1521 and RFC 1522. 
From: http://www.ussg.iu.edu/usail/mail/mime/

%prep
%setup
%patch0 -p1 -b buildfix

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
%doc Changes INSTALL README*
%doc %{_mandir}/man1/mpack.1*
%doc %{_mandir}/man1/munpack.1*
%{_bindir}/mpack
%{_bindir}/munpack

%changelog
* Sun Jan 27 2008 Dag Wieers <dag@wieers.com> - 1.6-2
- Added patch for gcc-3.0+.

* Sun Feb 23 2007 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Thu Feb 22 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
