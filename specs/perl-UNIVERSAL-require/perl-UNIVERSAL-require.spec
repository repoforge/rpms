# $Id$
# Authority: dag
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-require

Summary: Perl module to require() modules from a variable
Name: perl-UNIVERSAL-require
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-require/

Source: http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-require-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UNIVERSAL-require is a Perl module to require() modules from a variable.

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
%doc Changes MANIFEST META.yml SIGNATURE
%doc %{_mandir}/man3/UNIVERSAL::require.3pm*
%dir %{perl_vendorlib}/UNIVERSAL/
%{perl_vendorlib}/UNIVERSAL/require.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
