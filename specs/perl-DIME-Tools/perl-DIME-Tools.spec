# $Id$
# Authority: dag
# Upstream: Domingo Alcázar Larrea <domingo,alcazar$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DIME-Tools

Summary: Perl module for parsing and generate DIME messages
Name: perl-DIME-Tools
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DIME-Tools/

Source: http://www.cpan.org/authors/id/D/DA/DALCAZAR/DIME/DIME-Tools-0.03.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-DIME-Tools is a Perl module for parsing and generate DIME messages.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST README examples/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/DIME/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
