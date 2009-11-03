# $Id$
# Authority: dag
# Upstream: ??? <gugod$gugod,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kwiki-RecentChanges

Summary: Kwiki Recent Changes plugin
Name: perl-Kwiki-RecentChanges
Version: 0.14
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Kwiki-RecentChanges/

Source: http://www.cpan.org/modules/by-module/Kwiki/Kwiki-RecentChanges-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Kwiki Recent Changes plugin.

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
%doc %{_mandir}/man3/Kwiki::RecentChanges.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Kwiki/
#%{perl_vendorlib}/Kwiki/RecentChanges/
%{perl_vendorlib}/Kwiki/RecentChanges.pm

%changelog
* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
