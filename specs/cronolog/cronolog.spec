# $Id$
# Authority: dag

Summary: Log file rotator
Name: cronolog
Version: 1.6.2
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://cronolog.org/

Source: http://cronolog.org/download/cronolog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
cronolog is a simple filter program that reads log file entries from
standard input and writes each entry to the output file specified by
a filename template and the current date and time. When the expanded
filename changes, the current file is closed and a new one opened.

cronolog is intended to be used in conjunction with a Web server,
such as Apache, to split the access log into daily or monthly logs.

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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/cronolog.1m*
%doc %{_mandir}/man1/cronosplit.1m*
%doc %{_infodir}/cronolog.info*
%{_sbindir}/cronolog
%{_sbindir}/cronosplit

%changelog
* Thu Dec 28 2006 Dag Wieers <dag@wieers.com> - 1.6.2-1
- Initial package. (Contributed by Christoper Maser)
