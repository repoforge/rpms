# $Id$
# Authority: dries
# Upstream: Salvador Fandiño García <salva$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-Queue

Summary: Limit the number of forked processes that run concurrently
Name: perl-Proc-Queue
Version: 1.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-Queue/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-Queue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Proc::Queue limits the number of forked processes that can
be running concurrently.

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
%doc Changes README
%doc %{_mandir}/man3/Proc::Queue.3pm*
%dir %{perl_vendorlib}/Proc/
%{perl_vendorlib}/Proc/Queue.pm

%changelog
* Tue Mar 17 2009 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Initial package.
