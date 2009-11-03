# $Id$
# Authority: dag
# Upstream: Chris Dent <cdent$burningchrome,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kwiki-Raw

Summary: Kwiki plugin to provide an action to retrieve the raw wikitext of a page
Name: perl-Kwiki-Raw
Version: 0.02
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Kwiki-Raw/

Source: http://www.cpan.org/modules/by-module/Kwiki/Kwiki-Raw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Kwiki plugin to provide an action to retrieve the raw wikitext of a page.

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
%doc %{_mandir}/man3/Kwiki::Raw.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Kwiki/
#%{perl_vendorlib}/Kwiki/Raw/
%{perl_vendorlib}/Kwiki/Raw.pm

%changelog
* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
