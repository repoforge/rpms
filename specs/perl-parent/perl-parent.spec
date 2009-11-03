# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name parent

Summary: Establish an ISA relationship with base classes at compile time
Name: perl-parent
Version: 0.223
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/parent/

Source: http://www.cpan.org/authors/id/C/CO/CORION/parent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Establish an ISA relationship with base classes at compile time.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/parent.3pm*
#%{perl_vendorlib}/parent/
%{perl_vendorlib}/parent.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.223-1
- Updated to version 0.223.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.221-1
- Initial package. (using DAR)
