# $Id$
# Authority: gtenagli
# Upstream: Salvador Fandino <sfandino$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-OpenSSH-Parallel

Summary: Run SSH jobs in parallel.
Name: perl-Net-OpenSSH-Parallel
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-OpenSSH-Parallel/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SALVA/Net-OpenSSH-Parallel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::OpenSSH) >= 0.39
BuildRequires: rpm-macros-rpmforge

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Net::OpenSSH::Parallel is an scheduler that can run commands in parallel in a
set of hosts through SSH. It tries to find a compromise between being simple to
use, efficient and covering a good part of the problem space of parallel
process execution via SSH.


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Net::OpenSSH::Parallel.3pm*
%doc %{_mandir}/man3/Net::OpenSSH::Parallel::*.3pm*
%dir %{perl_vendorlib}/Net/OpenSSH/
%{perl_vendorlib}/Net/OpenSSH/Parallel.pm
%{perl_vendorlib}/Net/OpenSSH/Parallel/*

%changelog
* Wed Aug 10 2011 Giacomo Tenaglia <Giacomo.Tenaglia@cern.ch> - 0.11-1
- Initial packaging
