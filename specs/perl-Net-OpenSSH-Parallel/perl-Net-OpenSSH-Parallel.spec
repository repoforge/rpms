# $Id$
# Authority: gtenagli
# Upstream: Salvador Fandino <sfandino$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-OpenSSH-Parallel

Summary: Perl module named Net-OpenSSH-Parallel
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

%description
Run SSH jobs in parallel.

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
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/OpenSSH/
%{perl_vendorlib}/Net/OpenSSH/Parallel.pm
%{perl_vendorlib}/Net/OpenSSH/Parallel/
%{perl_vendorlib}/Net/OpenSSH/Parallel/*.pm

%changelog
* Wed Aug 10 2011 Giacomo Tenaglia <Giacomo.Tenaglia@cern.ch> - 0.11-1
- Initial packaging
