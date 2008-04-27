# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Top clone for MySQL
Name: mytop
Version: 1.4
Release: 2
License: GPL
Group: Applications/Databases
URL: http://jeremy.zawodny.com/mysql/mytop/

Source: http://jeremy.zawodny.com/mysql/mytop/mytop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Time::HiRes), perl(Term::ReadKey), perl(Term::ANSIColor), perl >= 0:5.005
Requires: perl >= 0:5.005, perl(Term::ReadKey)

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
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST README
%doc %{_mandir}/man1/mytop.1*
%{_bindir}/mytop

%changelog
* Sun Apr 27 2008 Dries Verachtert <dries@ulyssis.org> - 1.4-2
- Added perl(Term::ReadKey) dependency, thanks to Michael Mansour.

* Sun Mar 05 2006 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
