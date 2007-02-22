# $Id$
# Authority: dag

Summary: Pack a file in MIME format for mailing and news
Name: mpack
Version: 1.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.ussg.iu.edu/usail/mail/mime/

Source: http://ftp.andrew.cmu.edu/pub/mpack/mpack-%{version}.tar.gz
#Patch1: mpack-1.5-Makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The mpack program encodes the the named file in one or more MIME
messages.  The resulting messages are mailed to one or more
recipients, written to a named file or set of files, or posted 
to a set of newsgroups.  Lighter than Metamail - unmaintained

About MIME: See RFC 1521 and RFC 1522. 
From: http://ftp.andrew.cmu.edu/pub/mpack/

%prep
%setup
#patch1 -p2 -b Makefile

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
%{_bindir}/mpack

%changelog
* Thu Feb 22 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
