# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-LibYAML

Summary: Perl module that implements YAML using XS and libyaml
Name: perl-YAML-LibYAML
Version: 0.32
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-LibYAML/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-LibYAML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.3 
BuildRequires: perl(Filter::Util::Call)
Requires: perl >= 2:5.8.3 

%description
perl-YAML-LibYAML is a Perl module that implements YAML using XS and libyaml.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/YAML::XS.3pm*
%doc %{_mandir}/man3/YAML::XS::LibYAML.3pm*
%dir %{perl_vendorarch}/YAML/
%{perl_vendorarch}/YAML/LibYAML.pm
%{perl_vendorarch}/YAML/XS/
%{perl_vendorarch}/YAML/XS.pm
%dir %{perl_vendorarch}/auto/YAML/
%{perl_vendorarch}/auto/YAML/LibYAML/
%{perl_vendorarch}/auto/YAML/XS/
%changelog
* Mon Jul 20 2009 Christoph Maser <cmr@financial.com> - 0.32-1
- Updated to version 0.32.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.26-1
- Initial package. (using DAR)
