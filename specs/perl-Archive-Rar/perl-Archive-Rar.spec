# $Id$
# Authority: dag
# Upstream: jean-marc boulade <jmbperl$hotmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Rar

Summary: Interface with the 'rar' command
Name: perl-Archive-Rar
Version: 2.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Rar/

Source: http://www.cpan.org/modules/by-module/Archive/Archive-Rar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Simple)

%description
perl-Archive-Rar is a Perl module to interface with the 'rar' command.

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
%doc COPYRIGHT ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Archive::Rar.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Archive/
#%{perl_vendorlib}/Archive/Rar/
%{perl_vendorlib}/Archive/Rar.pm

%changelog
* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release 2.02.

* Fri Feb 22 2008 Dag Wieers <dag@wieers.com> - 1.95-1
- Updated to release 1.95.

* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 1.94-1
- Updated to release 1.94.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.93-1
- Initial package. (using DAR)
