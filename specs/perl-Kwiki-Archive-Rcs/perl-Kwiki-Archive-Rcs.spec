# $Id$
# Authority: dag
# Upstream: Ingy döt Net <INGY$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kwiki-Archive-Rcs

Summary: Kwiki plugin for page archival using RCS
Name: perl-Kwiki-Archive-Rcs
Version: 0.16
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Kwiki-Archive-Rcs/

Source: http://www.cpan.org/modules/by-module/Kwiki/Kwiki-Archive-Rcs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Kwiki) >= 0.38
Requires: perl >= 5.6.1


%description
Kwiki plugin for page archival using RCS.

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
%doc %{_mandir}/man3/Kwiki::Archive::Rcs.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Kwiki/
%dir %{perl_vendorlib}/Kwiki/Archive/
#%{perl_vendorlib}/Kwiki/Archive/Rcs/
%{perl_vendorlib}/Kwiki/Archive/Rcs.pm

%changelog
* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 0.16-1
- Updated to version 0.16.

* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
