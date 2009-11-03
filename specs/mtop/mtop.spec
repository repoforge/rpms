# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Tool to monitor a MySQL database
Name: mtop
Version: 0.6.6
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://mtop.sourceforge.net/

Source: http://dl.sf.net/mtop/mtop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
mtop (MySQL top) monitors a MySQL database showing the queries
which are taking the most amount of time to complete. Features
include 'zooming' in on a process to show the complete query
and 'explaining' the query optimizer information.

%prep
%setup

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}
%{__rm} -f %{buildroot}%{perl_vendorlib}/cpan2spec.pl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README*
%doc %{_mandir}/man1/mkill.1*
%doc %{_mandir}/man1/mtop.1*
%{_bindir}/mkill
%{_bindir}/mtop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.6-1.2
- Rebuild for Fedora Core 5.

* Sat Jan 21 2006 Dag Wieers <dag@wieers.com> - 0.6.6-1
- Initial package. (using DAR)
