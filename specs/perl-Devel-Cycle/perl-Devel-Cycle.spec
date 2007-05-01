# $Id$
# Authority: dag
# Upstream: Lincoln D. Stein <lstein$cshl,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Cycle

Summary: Perl module to find memory cycles in objects
Name: perl-Devel-Cycle
Version: 1.07
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Cycle/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Cycle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Devel-Cycle is a Perl module to find memory cycles in objects.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Devel::Cycle.3pm*
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/Devel/Cycle.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.07-1
- Initial package. (using DAR)
