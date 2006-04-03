# $Id$
# Authority: dag

Summary: Top clone for MySQL
Name: mytop
Version: 1.4
Release: 1
License: GPL
Group: Applications/Databases
URL: http://jeremy.zawodny.com/mysql/mytop/

Source: http://jeremy.zawodny.com/mysql/mytop/mytop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl-Time-HiRes, perl-Term-ReadKey, perl => 5.6.0, perl-Class-DBI-mysql
Requires: perl-Time-HiRes, perl-Term-ReadKey, perl => 5.6.0, perl-Class-DBI-mysql

%description
mytop is a console-based (non-gui) tool for monitoring the threads and 
overall performance of a MySQL 3.22.x, 3.23.x, and 4.x server. It runs 
on most Unix systems (including Mac OS X) which have Perl, DBI, and 
Term::ReadKey installed. And with Term::ANSIColor installed you even 
get color. If you install Time::HiRes, you'll get good real-time 
queries/second stats. As of version 0.7, it even runs on Windows 
(somewhat).

%prep
%setup

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%{_mandir}/man1/mytop.1*
%{_bindir}/mytop

%changelog
* Sun Mar 05 2006 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
